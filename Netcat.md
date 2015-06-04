#Netcat
Netcat puede hacer muchas cosas, su función principal es muy simple:

Crea un socket con el destino indicado si es cliente, o en el puerto indicado, si es servidor
Una vez conectado, envía por el socket todo lo que llegue en su entrada estándar y envía a su salida estándar todo lo que llegue por el socket
Algo tan simple resulta ser extraordinariamente potente y flexible como vas a ver e continuación. Por simplicidad se utilizan conexiones locales aunque, por supuesto, se pueden utilizar entre máquinas diferentes.

Sintaxis
nc [-options] hostname port[s] [ports]
nc -l -p port [-options] [hostname] [port]

Parámetros básicos
-l: modo ‘listen’, queda a la espera de conexiones entrantes.
-p: puerto local
-u: modo UDP
-e: ejecuta el comando dado después de conectar
-c: ejecuta órdenes de shell (hace /bin/sh -c [comando] después de conectar

##Un chat para dos
Servidor
$ nc -l -p 2000

Cliente
$ nc localhost 2000

##Transferencia de ficheros
La instancia de nc que escucha recibe el fichero. El receptor ejecuta:
$ nc -l -p 2000 > fichero.recibido

Y el emisor:
$ nc localhost 2000 < fichero

##Servidor de echo
Ponemos un servidor que ejecuta cat de modo que devolverá todo lo que
se le envíe

$ nc -l -p 2000 -e /bin/cat

Y en otra consola:

$ nc localhost 2000
hola
hola
…

##Servidor de daytime
Exactamente lo mismo que el ejemplo anterior pero ejecutando date en lugar de cat.

$ nc -l -p 2000 -e /bin/date

Y en otra consola:

$ nc localhost 2000
lun feb 10 21:26:48 CET 2014

##shell remota estilo telnet
Servidor
$ nc -l -p 2000 -e /bin/bash

Cliente
$ nc localhost 2000
##Telnet inverso
En esta ocasión es el cliente quien pone el terminal remoto
Servidor
$ nc -l -p 2000

Cliente
$ nc server.example.org 2000 -e /bin/bash

##Cliente de IRC
$ nc irc.freenode.net 6666
NOTICE AUTH :*** Looking up your hostname…
NOTICE AUTH :*** Found your hostname, welcome back
NOTICE AUTH :*** Checking ident
NOTICE AUTH :*** No identd (auth) response
NICK nadie
USER nadie nadie nadie :nadie
:kubrick.freenode.net 001 nadie :Welcome to the freenode IRC Network nadie
:kubrick.freenode.net 002 nadie :Your host is kubrick.freenode.net[kubrick.freenode.net/6666], running version hyperion-1.0.2b
[…]

y a partir de ahí puedes introducir cualquier comando de IRC:

LIST
JOIN #canal
PART #canal
PRIVMSG #canal :mensaje
WHO #canal
QUIT

##Cliente de correo SMTP
Podemos usar netcat para enviar correo electrónico por medio de un servidor SMTP, utilizando el protocolo directamente:

~$ nc mail.servidor.com
220 mail.servidor.com ESMTP Postfix
HELO yo
250 mail.servidor.com
MAIL FROM:guillermito@microchof.com
250 Ok
RCPT TO:manolo@cocaloca.es
250 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
Aviso: su licencia ha caducado. Me deben un pastón.
.
250 Ok: queued as D44314A607
QUIT
221 Bye

##Servidor/cliente HTTP
Es sencillo conseguir un cliente y un servidor HTTP rudimentarios.

Servidor
$ nc -l -p http -c “cat index.html”

Al cual podemos conectar con cualquier navegador HTTP, como por ejemplo firefox.

Cliente
$ echo “GET /” | nc www.google.com 80 > index.html

##Streaming de audio
Un sencillo ejemplo para hacer streaming de un fichero .mp3:

Servidor
$ nc -l -p 2000 < fichero.mp3

y para servir todos los .mp3 de un directorio:

$ cat *.mp3 | nc -l -p 2000

Cliente
$ nc server.example.org 2000 | madplay –

##Streaming de video
Servidor
$ nc -l -p 2000 < pelicula.avi

Cliente
$ nc server.example.org 2000 | mplayer –

##Proxy
Sirva para redirigir una conexión a otro puerto u otra máquina:

$ nc -l -p 2000 -c “nc example.org 22”

El tráfico recibido en el puerto 2000 de esta máquina se redirige a la máquina example.org:22. Permite incluso que la conexión entrante sea UDP pero la redirección sea TCP o viceversa!

##Clonar un disco a través de la red
Esto se debe usar con muchísima precaución. ¡Si no estás 100% seguro, no lo hagas!

Es este ejemplo voy a copiar un pen drive USB que está conectado al servidor a un fichero en el cliente y después lo voy a montar para acceder al contenido.

Servidor
$ dd if=/dev/sda1 | nc -l -p 2000

Cliente
$ nc server.example.org 2000 | dd of=pendrive.dump
$ mount pendrive.dump -r -t vfat -o loop /mnt/usb

##Ratón remoto
Es decir, usar el ratón conectado a una máquina para usar el entorno gráfico de otra. El ejemplo está pensado para Xorg.

Servidor
# nc -l -p 2000 < /dev/input/mice

Cliente
Editar el fichero /etc/X11/xorg.conf y modificar la configuración del ratón para que queda así:

<code>
Section "InputDevice"
    Driver     "mouse"
    ...
    Option    "Device"    "/tmp/fakemouse"
    ....
EndSection
$ mkfifo /tmp/fakemouse
$ nc server.example.org 2000 > /tmp/fakemouse
# /etc/init.d/gdm restart´
</code>

#Medir el ancho de banda
Servidor
$ nc -l -p 2000 | pv > /dev/null

Cliente
$ nc server.example.org 2000 < /dev/zero

#Imprimir un documento en formato PostScript
Funciona en impresoras que soporten el estándar AppSocket/JetDirect, que son la mayoría de las que se conectan por Ethernet.

$ cat fichero.ps | nc -q 1 nombre.o.ip.de.la.impresora 9100
Ver «La Guerra de las Galaxias»
$ nc towel.blinkenlights.nl 23


