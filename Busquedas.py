# -*- coding=utf-8 -*-
# Obtener busquedas por patron y listar permisos
__author__ = 'diego'
import stat
import os
import string
import commands

try:
    # Corremos un FIND y lo asignamos
    patron = raw_input("Introduce e patrón de búsqueda:\n")
    comando = "find " + patron
    comandoSalida = commands.getoutput(comando)
    resultado = string.split(comandoSalida, "\n")

    # Salida de resultados + permisos
    print "================================"
    print "Archivos posibles:"
    print comandoSalida
    print "================================"
    for file in resultado:
        mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE])
        print "\nPermisos del archivo ", file, ":"
        for level in "USR", "GRP", "OTH":
            for perm in "R", "W", "X":
                if mode & getattr(stat,"S_I"+perm+level):
                    print level, " tiene permisos de", perm
                else:
                    print level, " NO tiene permisos de", perm
except:
    print "Se generó una excepción"