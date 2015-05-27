#!/bin/sh
### BEGIN INIT INFO
# Provides: fwipv4-StateCAMBIAR
# Required-Start: $network
# Required-Stop: $network
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description Filtro IPV4 CAMBIAR
### END INIT INFO

##Variables
##
#INT_WAN=eth0
#INT_LAN=eth1
#IP_WAN=10.0.2.150
#IP_LAN=10.4.40.100
##Cargar módulos IPTABLES para soporte NAT e IP conntrack
#modprobe ip_conntrack
#modprobe ip_conntrack_ftp
##Activar reenvio
#echo 1 > /proc/sys/net/ipv4/ip_forward

flush_reglas()
{
echo "###### FLUSH #######"
iptables -F && echo "Borrando cualquier tipo de definición global"
iptables -X && echo "Borrando reglas definidas por el usuario"
iptables -Z && echo "Poniendo contadores de reglas a 0"
iptables -t nat -F && echo "Borrando reglas tabla NAT"
iptables -t nat -X && echo "buscar descripcion"
iptables -t mangle -F && echo "buscar descripcion"
iptables -t mangle -X && echo "buscar descripcion"
}
unset_policy()
{
echo "###### Parando FW ######"
iptables -P INPUT ACCEPT && echo "Aplicando policy INPUT ACCEPT"
iptables -P FORWARD ACCEPT && echo "Aplicando policy FORWARD ACCEPT"
iptables -P OUTPUT ACCEPT && echo "Aplicando policy OUTPUT ACCEPT"
}
set_policy()
{
echo "###### Bloqueo por defecto ######"
iptables -P INPUT DROP && echo "Aplicando INPUT DROP"
iptables -P FORWARD DROP && echo "Aplicando FORWARD DROP"
iptables -P OUTPUT DROP && echo "Aplicando OUTPUT DROP"
}
status()
{
echo "################ Tabla NAT ################"
iptables -t nat -L -xnv --line-numbers
echo "################ Globales ################"
iptables -L -xnv --line-numbers
}
reglasSalida()
{

}
reglasEntrada()
{

}
case "$1" in
start)
flush_reglas
set_policy
reglasSalida
reglasEntrada
echo "___________"
echo "¡Arrancado!"
;;
stop)
flush_reglas
unset_policy
echo "________"
echo "¡Parado!"
;;
restart)
$0 stop
$0 start
;;
status)
status
;;
*)
echo "Usar ejecutando: service $0 {start|stop|restart|status}"
;;
esac
