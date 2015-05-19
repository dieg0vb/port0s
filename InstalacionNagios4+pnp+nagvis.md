#Instalación nagios4+pnp4nagios+nagvis y alternativa check_MK

##nagios4
`apt-get update`
`apt-get install apache2 libapache2-mod-php5 build-essential libgd2-xpm-dev snmp snmpd php5 snmp-mibs-downloader samba sudo vim`
Creamos el usuario nagios y le asignamos una contraseña:
`useradd nagios`
`passwd nagios`
Añadimos el nuevo usuario en el grupo nagios
`usermod -G nagios nagios`
Creamos el nuevo grupo nagcmd para alojar los comandos usandos por la interfaz web.
`groupadd nagcmd`
Añadimos el usuario en el grupo nagios y apache
`usermod -a -G nagcmd nagios`
`usermod -a -G nagcmd www-data`
Esto último se hace para que desde el GUI de Nagios podamos ejecutar comandos externos sobre host y servicios – usuario apache-.
Para ello los ficheros donde van dichos comandos (/usr/local/nagios/var/rw/) veremos posteriormente que pertenecen a ese grupo “nagcmd”

Descargamos archivos actualizados
`wget http://sourceforge.net/projects/nagios/files/nagios-4.x/nagios-4.0.8/nagios-4.0.8.tar.gz`
`wget http://nagios-plugins.org/download/nagios-plugins-2.0.tar.gz`
`tar xzf nagios-4.0.8.tar.gz`
`cd nagios-4.0.8/`
`./configure -with-command-group=nagcmd`
Muestra un resumen al finalizar
```
*** Configuration summary for nagios 4.0.8 08-12-2014 ***:

 General Options:
 -------------------------
        Nagios executable:  nagios
        Nagios user/group:  nagios,nagios
       Command user/group:  nagios,nagcmd
             Event Broker:  yes
        Install ${prefix}:  /usr/local/nagios
    Install ${includedir}:  /usr/local/nagios/include/nagios
                Lock file:  ${prefix}/var/nagios.lock
   Check result directory:  ${prefix}/var/spool/checkresults
           Init directory:  /etc/init.d
  Apache conf.d directory:  /etc/apache2/conf.d
             Mail program:  /usr/bin/mail
                  Host OS:  linux-gnu
          IOBroker Method:  epoll

 Web Interface Options:
 ------------------------
                 HTML URL:  http://localhost/nagios/
                  CGI URL:  http://localhost/nagios/cgi-bin/
 Traceroute (used by WAP):  /usr/sbin/traceroute


Review the options above for accuracy.  If they look okay,
type 'make all' to compile the main program and CGIs.
##
```
Continuamos compilando
`make all`
`make install`
`make install-init`
`make install-commandmode`
`make install-config`
`make install-webconf`
`make install-exfoliation`
`htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin`
`service apache2 restart`
`cd ..`
`tar zxf nagios-plugins-2.0.tar.gz && cd nagios-plugins-2.0/`
`./configure --with-nagios-user=nagios --with-nagios-group=nagios`
`make`
`make install`

comprobamos que nagios se ha instalado correctamente
`/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg`
no devuelve ningún error y entramos en la interface web para comprobar
Dado que cada vez que cambiamos la configuración de ficheros de Nagios conviene chequearla (y necesitamos “recargar” la configuración) yo acostumbro a crear unos alias para tenerlo más a mano. En el fichero .bashrc de nuestro usuario podemos añadirlos.
ALIAS PARA NAGIOS
`alias comprobarNagios='/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg'`
`alias recargarNagios='/etc/init.d/nagios reload'`
Autoarranque con un demonio
`vi /etc/init.d/nagios`

```
###########
#! /bin/sh
# Feito por DVB
### BEGIN INIT INFO
# Provides:          nagios4
# Required-Start:    $local_fs $remote_fs $syslog $named $network $time
# Required-Stop:     $local_fs $remote_fs $syslog $named $network
# Should-Start:
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: nagios host/service/network monitoring and management system
# Description:       nagios is a monitoring and management system for hosts, services and networks.
### END INIT INFO

set -e

. /lib/lsb/init-functions

DAEMON=/usr/local/nagios/bin/nagios
NAME="nagios4"
DESC="nagios4 monitoring daemon"
NAGIOSCFG="/usr/local/nagios/etc/nagios.cfg"
CGICFG="/usr/local/nagios/etc/cgi.cfg"
NICENESS=5

[ -x "$DAEMON" ] || exit 0



# this is from madduck on IRC, 2006-07-06
# There should be a better possibility to give daemon error messages
# and/or to log things
log()
{
  case "$1" in
    [[:digit:]]*) success=$1; shift;;
    *) :;;
  esac
  log_action_begin_msg "$1"; shift
  log_action_end_msg ${success:-0} "$*"
}

check_started () {
	##nagios3-core can be installed without -cgi
	#if [ -e $CGICFG ];
	#then
	#	check_cmd=$(get_config nagios_check_command $CGICFG)
	#	if [ ! "$check_cmd" ]; then
	#		log 6 "unable to determine nagios_check_command from $CGICFG!"
	#		return 6
	#	fi
	#else
		#use hardcoded default version
		check_cmd="/usr/local/nagios/libexec/check_nagios /usr/local/nagios/var/status.dat 5 '/usr/local/nagios/bin/nagios'"
	#fi

  eval $check_cmd >/dev/null

  if [ -f "$THEPIDFILE" ]; then
    pid="$(cat $THEPIDFILE)"
    if [ "$pid" ] && kill -0 $pid >/dev/null 2>/dev/null; then
      return 0    # Is started
    fi
  fi
  return 1	# Isn't started
}

#
#	get_config()
#
#	grab a config option from nagios.cfg (or possibly another nagios config
#	file if specified).  everything after the '=' is echo'd out, making
#	this a nice generalized way to get requested settings.
#
get_config () {
  if [ "$2" ]; then
    set -- `grep ^$1 $2 | sed 's@=@ @'`
  else
    set -- `grep ^$1 $NAGIOSCFG | sed 's@=@ @'`
  fi
  shift
  echo $*
}

check_config () {
  if $DAEMON -v $NAGIOSCFG >/dev/null 2>&1 ; then
    # First get the user/group etc Nagios is running as
    nagios_user="$(get_config nagios_user)"
    nagios_group="$(get_config nagios_group)"
    log_file="$(get_config log_file)"
    log_dir="$(dirname $log_file)"

    return 0    # Config is ok
  else
    # config is not okay, so let's barf the error to the user
    $DAEMON -v $NAGIOSCFG
  fi
}

check_named_pipe () {
  nagiospipe="$(get_config command_file)"
  if [ -p "$nagiospipe" ]; then
    return 1   # a named pipe exists
  elif [ -e "$nagiospipe" ];then
    return 1
  else
    return 0   # no named pipe exists
  fi
}

if [ ! -f "$NAGIOSCFG" ]; then
  log_failure_msg "There is no configuration file for Nagios 3."
  exit 6
fi

THEPIDFILE=$(get_config "lock_file")
[ -n "$THEPIDFILE" ] || THEPIDFILE='/usr/local/nagios/var/nagios.pid'

start () {

  if [ "$ENABLED" = "no"  ]; then
	  log_warning_msg "Not starting Nagios4 - set ENABLED to yes in /etc/defrault/nagios"
	  exit 0
  fi

  DIRECTORY=$(dirname $THEPIDFILE)
  [ ! -d $DIRECTORY ] && mkdir -p $DIRECTORY
  chown nagios:nagios $DIRECTORY

  if ! check_started; then
    if ! check_named_pipe; then
      log_action_msg "named pipe exists - removing"
      rm -f $nagiospipe
    fi
    if check_config; then
      start_daemon -n $NICENESS -p $THEPIDFILE $DAEMON -d $NAGIOSCFG
      ret=$?
    else
      log_failure_msg "errors in config!"
      log_end_msg 1
      exit 1
    fi
  else
    log_warning_msg "already running!"
  fi
  return $ret
}

stop () {
    killproc -p $THEPIDFILE
    ret=$?
    if [ `pidof nagios | wc -l ` -gt 0 ]; then
        echo -n "Waiting for $NAME daemon to die.."
        cnt=0
        while [ `pidof nagios | wc -l ` -gt 0 ]; do
            cnt=`expr "$cnt" + 1`
            if [ "$cnt" -gt 15 ]; then
                kill -9 `pidof nagios`
                break
            fi
            sleep 1
            echo -n "."
        done
    fi
    echo
    if ! check_named_pipe; then
      rm -f $nagiospipe
    fi
    if [ -n "$ret" ]; then
      return $ret
    else
      return $?
    fi
}

status()
{
  log_action_begin_msg "checking $DAEMON"
  if check_started; then
    log_action_end_msg 0 "running"
  else
    if [ -e "$THEPIDFILE" ]; then
      log_action_end_msg 1 "$DAEMON failed"
      exit 1
    else
      log_action_end_msg 1 "not running"
      exit 3
    fi
  fi
}


reload () {
  # Check first
  if check_config; then
    if check_started; then
      killproc -p $THEPIDFILE $DAEMON 1
    else
      log_warning_msg "Not running."
    fi
  else
    log_failure_msg "errors in config!"
    log_end_msg 6
    exit 6
 fi
}

case "$1" in
  start)
    log_daemon_msg "Starting $DESC" "$NAME"
    start
    log_end_msg $?
    ;;
  stop)
    log_daemon_msg "Stopping $DESC" "$NAME"
    stop
    log_end_msg $?
  ;;
  restart)
    log_daemon_msg "Restarting $DESC" "$NAME"
    stop
    if [ -z "$?" -o "$?" = "0" ]; then
      start
    fi
    log_end_msg $?
  ;;
  reload|force-reload)
    log_daemon_msg "Reloading $DESC configuration files" "$NAME"
    reload
    log_end_msg $?
  ;;
  status)
    status
    ;;
  check)
    check
    ;;
  *)
    log_failure_msg "Usage: $0 {start|stop|restart|reload|force-reload|status}" >&2
    exit 1
  ;;
esac

exit 0
#############
```
permisos ejecución
`chmod +x /etc/init.d/nagios`

Creamos un enlace simbólico para que arranque con el sistema y ya debería estar listo
`ln -s /etc/init.d/nagios /etc/rcS.d/S99nagios`

##PNP4Nagios
`apt-get install rrdtool perl-base sudo librrds-perl apache2 php5-gd libpng12-dev libjpeg8-dev libgd2-xpm-dev fping qstat libldap2-dev libmysqlclient-dev libradius1 libradius1-dev libsnmp-base libsnmp15 libsnmp-dev libnet-snmp-perl smbclient samba-common ntp libpq-dev snmp snmpd openssl rrdtool librrds-perl gcc make`
`a2enmod rewrite`
`servive apache2 rertart`

bajamos pnp4nagios
`wget http://sourceforge.net/projects/pnp4nagios/files/PNP-0.6/pnp4nagios-0.6.25.tar.gz`
`tar xfvz pnp4nagios-0.6.25.tar.gz`
`cd pnp4nagios-0.6.25/`
`./configure`

escupe esto

```
** Configuration summary for pnp4nagios-0.6.25 03-01-2015 ***

  General Options:
  -------------------------         -------------------
  Nagios user/group:                nagios nagios
  Install directory:                /usr/local/pnp4nagios
  HTML Dir:                         /usr/local/pnp4nagios/share
  Config Dir:                       /usr/local/pnp4nagios/etc
  Location of rrdtool binary:       /usr/bin/rrdtool Version 1.4.7
  RRDs Perl Modules:                FOUND (Version 1.4007)
  RRD Files stored in:              /usr/local/pnp4nagios/var/perfdata
  process_perfdata.pl Logfile:      /usr/local/pnp4nagios/var/perfdata.log
  Perfdata files (NPCD) stored in:  /usr/local/pnp4nagios/var/spool

  Web Interface Options:
  -------------------------         -------------------
  HTML URL:                         http://localhost/pnp4nagios
  Apache Config File:               /etc/apache2/conf.d/pnp4nagios.conf


  Review the options above for accuracy.  If they look okay,
  type 'make all' to compile.
  ```

continuamos
`make all`
`make fullinstall`

Nos copia el demonio npcd. Configuramos npcd y nagios para arrancar al inicio y reiniciamos los implicados:

`update-rc.d nagios start 20 2 3 4 5 . stop 80 0 1 6`
`update-rc.d npcd start 19 2 3 4 5 . stop 79 0 1 6`
`service npcd restart && service nagios restart && service apache2 restart`

abrimos localhost/pnp4nagios  y nos dice todo OK pero debemos renombrar/borrar un archivo de instalación
`mv  /usr/local/pnp4nagios/share/install.php  /usr/local/pnp4nagios/share/install.php.inicial`
Volvemos a cargar la página y veremos que nos da otro error:
```
Please check the documentation for information about the following error:
perfdata directory “/usr/local/pnp4nagios/var/perfdata/” is empty. Please check your Nagios config. Read FAQ online
```

Este es normal ya que no hemos acabado la configuración. Vamos con ello…
En el directorio /usr/local/pnp4nagios/etc tenemos dos ficheros de ejemplo para hacer copy/paste.
Del fichero nagios.cfg-sample copiamos la siguiente configuración a el fichero /usr/local/nagios/etc/nagios.cfg

`vim /usr/local/nagios/etc/nagios.cfg`

añadimos
```
# Bulk / NPCD mode
#
process_performance_data=1

# *** the template definition differs from the one in the original nagios.cfg
#
service_perfdata_file=/usr/local/pnp4nagios/var/service-perfdata
service_perfdata_file_template=DATATYPE::SERVICEPERFDATA\tTIMET::$TIMET$\tHOSTNAME::$HOSTNAME$\tSERVICEDESC::$SERVICEDESC$\tSERVICEPERFDATA::$SERVICEPERFDATA$\tSERVICECHECKCOMMAND::$SERVICECHECKCOMMAND$\tHOSTSTATE::$HOSTSTATE$\tHOSTSTATETYPE::$HOSTSTATETYPE$\tSERVICESTATE::$SERVICESTATE$\tSERVICESTATETYPE::$SERVICESTATETYPE$
service_perfdata_file_mode=a
service_perfdata_file_processing_interval=15
service_perfdata_file_processing_command=process-service-perfdata-file

# *** the template definition differs from the one in the original nagios.cfg
#
host_perfdata_file=/usr/local/pnp4nagios/var/host-perfdata
host_perfdata_file_template=DATATYPE::HOSTPERFDATA\tTIMET::$TIMET$\tHOSTNAME::$HOSTNAME$\tHOSTPERFDATA::$HOSTPERFDATA$\tHOSTCHECKCOMMAND::$HOSTCHECKCOMMAND$\tHOSTSTATE::$HOSTSTATE$\tHOSTSTATETYPE::$HOSTSTATETYPE$
host_perfdata_file_mode=a
host_perfdata_file_processing_interval=15
host_perfdata_file_processing_command=process-host-perfdata-file
```

Ahora otro fichero
`vim /usr/local/nagios/etc/objects/commands.cfg`

añadimos

```
# Bulk with NPCD mode
#
define command {
 command_name process-service-perfdata-file
 command_line /bin/mv /usr/local/pnp4nagios/var/service-perfdata /usr/local/pnp4nagios/var/spool/service-perfdata.$TIMET$
}
define command {
command_name process-host-perfdata-file
command_line /bin/mv /usr/local/pnp4nagios/var/host-perfdata /usr/local/pnp4nagios/var/spool/host-perfdata.$TIMET$
}
```

Reiniciamos el demonio npcd de pnp4nagios y el propio Nagios, no es instantáneo el pintado de graficas darle unos minutos
`service npcd restart && service nagios restart`

Nos faltaría ahora una cosa importante. Poder acceder directamente desde el Host / Servicio en Nagios a las gráficas correspondientes
de este sin tener que ir a el interface de PNP4 para localizarlo. Siguiendo las instrucciones de la documentación nos vamos
directamente a configurarlo para POPUPs. Creamos unos “templates” para aplicarlos luego a los objetos.
En el fichero /usr/local/nagios/etc/objects/templates.cfg añadimos

`vim /usr/local/nagios/etc/objects/templates.cfg`

```
#
define host {
 name host-pnp
 action_url /pnp4nagios/index.php/graph?host=$HOSTNAME$&srv=_HOST_' class='tips' rel='/pnp4nagios/index.php/popup?host=$HOSTNAME$&srv=_HOST_
 register 0
}
define service {
 name srv-pnp
 action_url /pnp4nagios/index.php/graph?host=$HOSTNAME$&srv=$SERVICEDESC$' class='tips' rel='/pnp4nagios/index.php/popup?host=$HOSTNAME$&srv=$SERVICEDESC$
 register 0
}
#
```

Ejemplo de como añadir host-pnp y srv-pnp a un host y servicio
```
define host{
 use linux-server,host-pnp
 host_name localhost
 alias localhost
 address 127.0.0.1
 }
define service{
 use local-service,srv-pnp
 host_name localhost
 service_description PING
 check_command check_ping!100.0,20%!500.0,60%
 }
```

ahora Es necesario copiar un fichero a la configuración web de Nagios y las rutas de la doc. de PNP4Nagios no coinciden con las nuestras. Copiamos el fichero correctamente de los fuentes de pnp4nagios:

`cp /root/pnp4nagios-0.6.25/contrib/ssi/status-header.ssi /usr/local/nagios/share/ssi/`
`service npcd restart && service nagios restart`

ahora comprobamos que todo esta correcto en pnp4nagios
`cd /usr/local/pnp4nagios/`
`wget http://verify.pnp4nagios.org/verify_pnp_config`
`perl verify_pnp_config --mode bulk+npcd --config=/usr/local/nagios/etc/nagios.cfg --pnpcfg=/usr/local/pnp4nagios/etc`

que da un par de warnings de:
```
#[WARN]  'process_perf_data 1' is set for 1 hosts/services which are not providing performance data!
```
pero por inet no le dan importancia a esto

#Se instalamos _check_mk_ podemos olvidarnos de esto de agregar y configurar templates ya que lo hace todo el.

`wget http://mathias-kettner.de/download/check_mk-1.2.6b7.tar.gz`
`tar xvzf check_mk-1.2.6b7.tar.gz`
`cd check_mk-1.2.6.b7`
`./setup.sh`

hará preguntas y las acepto todas salvo estas:
> Nagios command pipe
> ( default  –> /var/log/nagios/rw/nagios.cmd): /usr/local/nagios/var/rw/nagios.cmd
> RRD files
> ( default  –> /var/lib/nagios/rrd): /usr/local/pnp4nagios/var/perfdata
>

`service npcd restart && service nagios restart && service apache2 restart`

ahora al entrar nos da un problema apache, dice que no tenemos mod_python instalado
aquí los manuales que he encontrado para no-debian compilan my_python antiguo y no se que ya que está descontinúado en favor del mod_wsi creo
pero por probar hago un:

`apt-get install libapache2-mod-python`
`service apache2 restart`

si no instalamos sudo tendremos un error aquí ya que WATO necesita sudo y debería añadir estas líneas a /etc/sudoeres
```
Defaults:www-data !requiretty
www-data ALL = (root) NOPASSWD: /usr/bin/check_mk --automation *
```

##Instalación de Nagvis

`apt-get install php-gettext php-net-socket php-pear php5-sqlite graphviz php5-gd rsync`
`cd`
`wget http://sourceforge.net/projects/nagvis/files/NagVis%201.8/nagvis-1.8rc3.tar.gz`
`tar xzf nagvis-1.8rc3.tar.gz`
`cd nagvis-1.8rc3`
`./install.sh`

(todo aceptar)

`cd`
`service apache2 restart`

abrimos navegador con /nagvis y admin:admin
el apache que corre esta debian es 2.2 y fuese 2.4 debemos poner esto en el apache2.conf
```
#AllowOverride None
  Require all granted
```

Lo primero que tendremos que hacer en Nagvis será probar que funiona el acceso a los datos de nuestro nagios a través de mklivestatus.
Ir a un mapa existente (p.e. “Demo1. Datacenter Hamburg”).

Menu Edut map / lock-unlock all
Menu Edit Map / Map Options / listbox “backend_id” y selecciona live_1 (save).
Menu  Edit Map / Add Icon / Host, situa el puntero en el map, selecciona un un host en el “listbox” (tendrás al menos tu localhost) y listo.
Menu Edut map / lock-unlock all  para quitar el modo edición.
Ahora ya podemos crear nuevos mapas usando imágenes que subamos y empezar a situar nuestros objetos en estas. Al crear nuestro mapa usaremos el backend “live_1”
Nagvis incluye muchos mapas que están bien para echarle un ojo inicialmente pero que generan mucha confusión así que mejor que los borres.
