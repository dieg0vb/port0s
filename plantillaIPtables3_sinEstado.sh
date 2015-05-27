#!/bin/sh
### BEGIN INIT INFO
# Provides: fwipv4-Stateless
# Required-Start: $network
# Required-Stop: $network
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description Filtro IPV4 Stateless
#
#Equipo de pasarela (eth0 eth1) con salida por la eth0 y lan interna en eth1.
#eth0 10.0.2.113
#eth1 10.4.40.40
#La maquina corre squid3 con dansguardian. Las peticiones naturales desde red interna a http las coge squid en el 8080 y las larga en salida al natural
#firewall sin estado con NAT desde la red local
### END INIT INFO

flush_reglas()
{
#Limpiar todo
iptables -F && echo "Borrando cualquier tipo de definición global"
iptables -X && echo "Borra las reglas definidas por el usuario"
iptables -Z && echo "Pone los contadores de las reglas a 0"
iptables -F -t nat && echo "Borrando reglas tabla NAT"
}
unset_policy()
{
echo "###### Parando FW"
iptables -P INPUT ACCEPT && echo "Aplicando policy INPUT ACCEPT"
iptables -P FORWARD ACCEPT && echo "Aplicando policy FORWARD ACCEPT"
iptables -P OUTPUT ACCEPT && echo "Aplicando policy OUTPUT ACCEPT"
}
set_policy()
{
#Politica por defecto
iptables -P INPUT DROP && echo "Aplicando policy INPUT DROP"
iptables -P FORWARD DROP && echo "Aplicando policy FORWARD DROP"
iptables -P OUTPUT DROP && echo "Aplicando policy OUTPUT DROP"
}
status()
{
echo "################ Tabla NAT ################"
iptables -t nat -Lxnv --line-numbers
echo "################ Globales ################"
iptables -Lxnv --line-numbers
}
reglas()
{
#Reglas NAT
#Para poner la IP publica de la NAT.
iptables -t nat -A POSTROUTING -o eth0 -s 10.4.40.0/24 -j SNAT --to 10.0.2.125
#Permite el trafico icmp redirigido saliente
iptables -A FORWARD -i eth1 -o eth0 -p icmp --icmp-type echo-request -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -p icmp --icmp-type echo-reply -j ACCEPT
#Permite el trafico www redirigido saliente
iptables -A FORWARD -i eth1 -o eth0 -p tcp --dport 80 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -p tcp --sport 80 -j ACCEPT
#Permite el trafico www redirigido saliente
iptables -A FORWARD -i eth1 -o eth0 -p tcp --dport 443 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -p tcp --sport 443 -j ACCEPT
#Permite el trafico dns redirigido saliente
iptables -A FORWARD -i eth1 -o eth0 -p udp --dport 53 -j ACCEPT
iptables -A FORWARD -i eth0 -o eth1 -p udp --sport 53 -j ACCEPT
#Reenvio todo el trafico de www a Squid/Dansguardian (8080), y permito el trafico en entrante y saliente de S/D
iptables -t nat -A PREROUTING -i eth1 -p tcp --dport 80 -j REDIRECT --to-port 8080
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 8080 -j ACCEPT
#Permite trafico Loopback Local
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
#Permito icmp peticiones y respuestas
iptables -A OUTPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-reply -j ACCEPT
#Permitir ssh hacia exterior
iptables -A INPUT -p tcp --sport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT
#Permitir ssh desde exterior
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
#Permitir WWW HTTPS y DNS
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --sport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp --sport 443 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p udp --sport 53 -j ACCEPT
}
case "$1" in
start)
echo "#### Borrando reglas previas"
flush_reglas
set_policy
reglas
echo "Arrancado"
;;
stop)
flush_reglas
unset_policy
echo "Parado"
;;
restart)
$0 stop
$0 start
;;
status)
status
*)
echo "Usar ejecutando: service $0 {start|stop|restart|status}"
;;
esac

 
