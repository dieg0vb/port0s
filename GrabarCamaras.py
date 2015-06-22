#!/usr/bin/python3
# -*- coding=utf-8 -*-

#Nombre: GrabarCamaras.py
#Autor: yo
#Origen: ratos muertos
#Lenguaje: python3
#Licencia: GPL3
#Propósito: Grabar continuamente cámaras(solo lo he probado con ip-camaras) y guardar los vídeos en el formato x:
#Dependencias: python3
######
#uso:
#Se añade en el directorio del script un archivo con el siguiente contenido, una línea por cada cámara:
# input	   output	log	workdir

#rtsp://192.168.1.200/video.mjpg camara1.ogv	camara1.log	/tmp
#rtsp://192.168.1.201/video.mjpg camara2.ogv	camara2.log /tmp

#Comentarios:
#versión 0.1 Tiene muchísimo que pulir y tengo que añadir que informe de errores por correo, y alguna cosilla más, pero me parece una versión funcional y puede que a alguien le sirva para automatizar un poco si tiene cámaras.
#versión 0.2: Simplificado a fondo, pero el log lo he sustituido por el paquete logging y no lo termino de hacer bien, aun subiré algo más completito cuando lo tenga

import time, re, subprocess, os 
import logging as log

def parseListConfigFile(filepath,column_name=None):
    """ lee, linea por linea y devuelve un Array por cada o un dict,
        de un fichero que son varias columnas """
    #import re
    if type(column_name) == list or type(column_name) == tuple:
        for c in column_name:
            if not type(c) == str:
                raise RuntimeError('Bad Input')
    elif type(column_name) == str: # esto no es reentrante...
        column_name = [column_name]
    elif column_name != None:
       raise RuntimeError('Bad input')

    file = open(filepath,'r')
    lineas = []
    for line in file.readlines():
        if re.match('\s*#+.*',line) == None and re.match('\s+',line) == None:
            mo = re.match('(.*)\s*#+.*',line) # limpiamos los comentarios
            if mo != None:
                line = mo.group(1)
            words = re.findall('\S+',line) # lista de palabras
            if column_name != None:
                dic = {}
                for el, indice in enumerate(column_name):
                    dic[indice] = words[el]
                for i in range(len(column_name)):
                    words.pop(0)
                lineas.append([dic])
                lineas[len(lineas)-1].extend(words)
            else:
                lineas.append(words)
    file.close()
    if column_name != None and len(column_name) == 1: # esto no es reentrante
        column_name = column_name[0]
    return lineas

class camarad():
    """ clase que controla la camara
        opciones que se pasan:
        workdir == donde guarda las cosas
        input == camara
        output == nombre del fichero de destino(se le añade fecha)
        timerecord == el tiempo en horas que crea un nuevo archivo
        """
    supported_av = ['ffmpeg','avconv']
    LOGFILE = None
    OK = False
    # TODO usar la opcion name
    option = {   'logfile':None, \
                 'workdir':os.getenv('PWD'), \
                   'input':None, \
                  'output':None, \
                 'timerecord':None, \
            'supported_av':['ffmpeg','avconv']}

    def test_camara(self,camara=None):
        listcall = []
        listcall.append(self.AV[:2] + "probe")
        if camara == None:
            listcall.append(self.option['input'])
        else:
            listcall.append(camara)
        nul = open(os.devnull,'w')
        ret  = subprocess.call(listcall,stdout= nul,stderr=nul)
        nul.close()
        if ret == 0:
            ret = True
        else:
            ret = False
        return ret

    def __init__(self,camara=None,*args,**kwargs):
        """ inicio y configuración de opciones"""
        # TODO opciones
        args = kwargs.keys()
        for ind in args: # lista de opciones
            self.option[ind] = kwargs[ind] 
        if camara == None and self.option['input'] == None:
            raise RuntimeError('No camara passed')
        if self.option['output'] == None:
            raise RuntimeError('No archivo de destino pasado')
        if camara != None:
            self.option['input'] = camara
        self.info()
        self.AV = self.osvideo_converter()
        self.OK = self.test_camara()
        if not self.OK:
            raise RuntimeError('No input recogniced')

    def osvideo_converter(self):
        """ devuelve una cadena con el tipo de conversor instalado en el sistema """
        path = re.findall(':([^:]*)',os.defpath)
        for sup in self.supported_av:
            for cam in path:
                if os.path.isfile(os.path.join(cam,sup)):
                    return sup
        else:
            raise RuntimeError("Any video converter supported")

    def info(self):
        """ Pinta la información de la clase"""
        print("Info de clase")
        print('name: ' +self.option['input'])
        dic = self.option.keys()
        for opt in dic:
            print(opt + " = " + str(self.option[opt]))
        print("")

    def fecha(self,fecha='full'): # TODO bien
        dat = time.localtime()
        if fecha == 'full':
            return "%i:%02i:%02i::%02i:%02i:%02i" % (dat.tm_year,dat.tm_mon,dat.tm_mday,dat.tm_hour,dat.tm_min,dat.tm_sec)
        elif fecha == 'hour':
            return "%i:%02i:%02i" % (dat.tm_year,dat.tm_mon,dat.tm_mday)
        else:
            raise RuntimeError

    def record(self):
        if type(self.option['logfile']) == str:
            log.basicConfig(filename=self.option['logfile'])
        log.info('started ' + self.option['input'])
        if self.option['workdir'] != None and os.getenv('PWD') != self.option['workdir']:
            log.info('Cambiando al directorio ' + self.option['workdir'])
            os.chdir(self.option['workdir'])
        logfile = open(self.option['logfile'],'a')
        while 1:
            i = 1
            while not self.test_camara():
                self.OK = False
                time.sleep(5 * i)
                if i < 12:
                    i += 1
                log.error('intentando reconectar...')
            self.OK = True
            av_options = [self.AV]
            av_options += ['-loglevel 16 -i ' + self.option['input']+' -map 0'] 
            # opciones para  flujos
            try: # añadimos la fecha
                gr = re.match('((.*/)*)*(.+)(\..+)',self.option['output']).groups()
                output = gr[-2]+'['+self.fecha()+']'+gr[-1]
            except:
                output = self.option['output']
            av_options += [output]
            # tiempo
            if self.option['timerecord'] != None:
                av_options += ['-t '+str(self.option['timerecord'])+":00:00"]
            print(' '.join(av_options))
            log.info('Iniciando la grabación')
            err = subprocess.call(' '.join(av_options), stdout=logfile, stderr=logfile, shell=True)
        logfile.close()
        if type(self.option['logfile']) == str:
            log.close()

if __name__=='__main__':
    # Ficheros donde se guardan las cámaras y opciones
    CAMOPT = 'camaras.txt'
    options = ('input','output','logfile','workdir')
    lista = parseListConfigFile(CAMOPT,options)
    for i in range(len(lista)):
        if os.fork() == 0:
            X = camarad(lista[i][0]['input'],**lista[i][0])
            X.record()
        else:
            pass
    print('exit')

