<h2 style="color: #000000;">TIPO DE CONFIGURACIÓN VPN QUE VAMOS A USAR</h2>
<p style="color: #000000;">Hay distintas formas de configurar un servidor mediante OpenVPN. <strong>Los distintos tipos de configuración existentes son Host to Host, Road to Warrior (Host to LAN) y Net to net</strong>. <strong>Nosotros</strong> <strong>nos focalizaremos en el Road to Warrior o Host to LAN</strong>, por ser el más popular de todos y el que seguramente se adaptar a prácticamente las necesidades de de cualquier usuario.</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/1-Arquitectura-Host-to-Net.jpg" target="_blank"><img class="size-medium wp-image-4401 alignnone" title="1- Arquitectura Host to Net" src="http://geekland.hol.es/wp-content/uploads/2014/01/1-Arquitectura-Host-to-Net-300x200.jpg" alt="1 Arquitectura Host to Net 300x200 Crear y configurar servidor openvpn" width="300" height="200" /></a></p>
<p style="color: #000000;">La configuración <strong>Road to Warrior (Host to LAN mediante túnel) permitirá que múltiples dispositivos u ordenadores se puedan conectar simultáneamente a nuestra red VPN</strong> y compartir recursos e informaciones con la red a que se conectan. Por lo tanto en este caso tenemos varios clientes que se pueden conectar de forma independiente al servidor VPN. Para quien precise de más información acerca de este tipo de configuración puede consultar el siguiente enlace.</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/2-Arquitectura-host-to-host.png" target="_blank"><img class="size-medium wp-image-4402 alignnone" title="2- Arquitectura host to host" src="http://geekland.hol.es/wp-content/uploads/2014/01/2-Arquitectura-host-to-host-300x79.png" alt="2 Arquitectura host to host 300x79 Crear y configurar servidor openvpn" width="300" height="79" /></a></p>
<p style="color: #000000;"><strong>La configuración Host to Host, a diferencia del modo de configuración anterior, únicamente nos permitirá la conexión entre 2 máquinas</strong> o dispositivos conectados a Internet o dentro de una red local. Por lo tanto en este caso solamente existe un cliente y un servidor. Además estás 2 máquinas o dispositivos no podrán compartir recursos e informaciones con otros equipos que estén conectados en la misma red LAN.</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/3-Arquitectura-Net-to-Net.jpg" target="_blank"><img class="size-medium wp-image-4403 alignnone" title="3- Arquitectura Net to Net" src="http://geekland.hol.es/wp-content/uploads/2014/01/3-Arquitectura-Net-to-Net-300x209.jpg" alt="3 Arquitectura Net to Net 300x209 Crear y configurar servidor openvpn" width="300" height="209" /></a></p>
<p style="color: #000000;">Para finalizar tenemos <strong>la configuración Net to Net, Red-red, o LAN to LAN</strong>. Esta configuración mayoritariamente es usada en el mundo empresarial. Esta configuración<strong> lo que hace es unir redes locales (LAN) ubicadas en distintas ubicaciones geográficas</strong>para de esta forma poder compartir información entre todos los clientes de todas las redes. De este modo cada una de las redes locales LAN tiene un punto de acceso o puerta de enlace que proporciona un canal de transmisión seguro entre 2 o más redes.</p>

<h2 style="color: #000000;">ASEGURAR QUE EL SERVIDOR OPENVPN TENGA IP FIJA EN LA RED LOCAL</h2>
<p style="color: #000000;">Es muy importante asegurar que nuestro servidor disponga de una IP interna fija en la red local. Es importante porqué cuando recibamos una petición de los clientes VPN, el router tendrá que saber a que IP interna tiene que redireccionar la petición del cliente VPN.</p>
<p style="color: #000000;"><strong>Para conseguir disponer de un servidor con ip interna fija tan solo tienen que seguir los pasos que se detallan en el siguiente enlance:</strong></p>
<p style="color: #000000;"><a style="color: #0090d3;" title="Configurar IP fija o Estatica con IPv4" href="http://geekland.hol.es/configurar-ip-fija_o_estatica_ipv4/" target="_blank">http://geekland.hol.es/configurar-ip-fija_o_estatica_ipv4/</a></p>

<h6 style="color: #000000;">Nota: El método descrito en el enlace es válido en el caso que estéis usando un servidor sin entorno gráfico. En el caso que el servidor que uséis disponga de entorno gráfico tendréis que configurar este aspecto a través de las interfaces visuales de vuestro gestor de red que probablemente será<a style="color: #0090d3;" title="Proyecto Network Manager" href="https://wiki.gnome.org/Projects/NetworkManager" target="_blank">network manager</a> o <a style="color: #0090d3;" title="Proyecto Wicd" href="http://wicd.sourceforge.net/" target="_blank">wicd</a>.</h6>
<p style="color: #000000;">Una vez terminados la totalidad de pasos mi servidor tendrá una IP fija que en mi caso será la <strong><span style="color: #0090d3;">192.168.1.188</span></strong>. Esta IP es la que deberemos usar para que el router redireccione las peticiones de los clientes al servidor OpenVPN.</p>

<h2 style="color: #000000;">REDIRECCIONAMIENTO DINÁMICO NO-IP</h2>
<p style="color: #000000;">Cuando tengamos nuestro servidor VPN funcionando, lo más probable es que tengamos conectarnos desde el exterior de nuestra local red local mediante el servidor VPN.</p>
<p style="color: #000000;">Para conectarnos a nuestra red local tendremos que saber nuestra IP Pública pero desafortunadamente en la gran mayoría de casos la IP que tenemos es dinámica. Por lo tanto se puede dar perfectamente el caso que en el momento de conectarnos no sepamos la IP Pública de nuestro servidor.</p>
<p style="color: #000000;"><strong>Para</strong> solucionar este problema tenemos que <strong>asociar la IP Pública de nuestro servidor a un dominio</strong>. Para poder realizar este paso tan solo <strong>tienen que seguir las indicaciones del siguiente enlace:</strong></p>
<p style="color: #000000;"><a style="color: #0090d3;" title="Encontrar servidor con DNS dinamico" href="http://geekland.hol.es/encontrar-servidor-con-dns-dinamico/" target="_blank">http://geekland.hol.es/encontrar-servidor-con-dns-dinamico/</a></p>
<p style="color: #000000;">Una vez realizados estos pasos tendréis vuestra IP Pública asociada a un dominio. En mi caso mi IP Pública está asociada al dominio <strong><span style="color: #0090d3;">geekland.sytes.net</span></strong></p>

<h2 style="color: #000000;">INSTALACIÓN DEL SERVIDOR</h2>
<p style="color: #000000;">La instalación del servidor la vamos a realizar en un sistema operativo Debian Wheezy. <strong>La totalidad del procedimiento descrito tiene que funcionar en cualquier distribución que derive de Debian</strong> como pueden ser <a style="color: #0090d3;" title="Website de Ubuntu" href="http://www.ubuntu.com/" target="_blank">Ubuntu</a>, <a style="color: #0090d3;" title="Website de Crunchbang" href="http://crunchbang.org/" target="_blank">Crunchbang</a>, <a style="color: #0090d3;" title="Website de Mint" href="http://www.linuxmint.com/" target="_blank">Linux Mint</a>, <a style="color: #0090d3;" title="Website de Kubuntu" href="http://www.kubuntu.org/" target="_blank">Kubuntu</a>, etc.</p>
<p style="color: #000000;">Para instalar el servidor OpenVPN lo primero que tenemos que hacer es <strong>abrir una terminal</strong>. Dentro de la terminal <strong>teclean el siguiente comando</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">sudo apt-get install openvpn openssl</span></strong></pre>
</blockquote>
<p style="color: #000000;">Ahora ya tenemos instalado el servidor.</p>

<h2 style="color: #000000;">CREAR UNA AUTORIDAD DE CERTIFICACIÓN</h2>
<p style="color: #000000;">OpenVPN es un protocolo de VPN basado SSL/TLS mediante certificados y claves RSA creadas mediante openssl. Por lo tanto el nivel de seguridad proporcionado por OpenVPN es muy elevado.</p>
<p style="color: #000000;">Al ser un protocolo que funciona bajo certificados y claves necesitaremos crear una autoridad de certificación para a posteriori generar los certificados.</p>

<h6 style="color: #000000;">Nota: La principal función de una autoridad de certificación es la de emitir y revocar certificados digitales para terceros. Para quien necesite más información puede consultar el siguiente <a style="color: #0090d3;" title="Explicación de lo que es una autoridad de certificación" href="https://es.wikipedia.org/wiki/Autoridad_de_certificaci%C3%B3n" target="_blank">enlace</a>.</h6>
<h5 style="color: #000000;">Crear el certificado raíz ca para firmar y revocar los certificados de los clientes</h5>
<p style="color: #000000;">Para poder emitir y revocar la claves <strong>necesitamos crear nuestra propia autoridad certificadora</strong> y disponer de nuestro certificado raíz <strong><span style="color: #0090d3;">ca.ctr</span></strong> y de nuestra clave <strong><span style="color: #0090d3;">ca.key</span></strong> para poder crear y firmar las claves de los clientes y del servidor.</p>
<p style="color: #000000;">Para realizar este paso, y el resto de pasos, ejecutoriaremos los scripts que OpenVPN trae incorporados de seri<strong>e</strong>. Para ello tenemos que crear una carpeta con nombre <strong><span style="color: #0090d3;">easy-rsa</span></strong>dentro de la ubicación <strong><span style="color: #0090d3;">/etc/openvpn</span></strong>. <strong>Para ello abrimos una terminal y tecleamos el siguiente comando</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">cd /etc/openvpn</span></strong></pre>
<pre><strong><span style="color: #0090d3;">mkdir easy-rsa</span></strong></pre>
</blockquote>
<p style="color: #000000;">Seguidamente tenemos que<strong> copiar los scripts de configuración</strong> de OpenVPN, <strong>que se hallan en</strong> la ubicación <strong><span style="color: #0090d3;">/usr/share/doc/openvpn/examples/easy-rsa/2.0/</span></strong>, <strong>dentro de la carpeta</strong> <strong><span style="color: #0090d3;">easy-rs</span><span style="color: #0090d3;">a</span></strong> que acabamos de crear. Para ello en la terminal tecleamos el siguiente comando:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">cp -r /usr/share/doc/openvpn/examples/easy-rsa/2.0/* easy-rsa</span></strong></pre>
</blockquote>
<p style="color: #000000;">Una captura de pantalla los pasos realizados hasta el momento se puede ver a continuación:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/4-Ejemplos-copiados.png" target="_blank"><img class="size-medium wp-image-4404 alignnone" title="4- Ejemplos copiados" src="http://geekland.hol.es/wp-content/uploads/2014/01/4-Ejemplos-copiados-300x195.png" alt="4 Ejemplos copiados 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>
<p style="color: #000000;">En el caso que que vuestra distro trabaje con la versión 3 de easy-rsa, en el momento de introducir el último comando, obtendréis un error parecido al siguiente error:</p>
<p style="color: #000000;"><span style="color: #ff0000;"><strong>cp: no se puede efectuar `stat’ sobre «/usr/share/doc/openvpn/examples/easy-rsa/2.0/*»: No existe el archivo o el directorio</strong></span></p>
<p style="color: #000000;">Los pasos a realizar para solucionar este error son los siguientes. En la terminal escriben el siguiente comando para instalar el paquete easy-rsa.</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">apt-get install easy-rsa</span></strong></pre>
</blockquote>
<p style="color: #000000;">Seguidamente borran la carpeta easy-rsa que habíamos creado inicialmente introduciendo el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">rm -R /etc/openvpn/easy-rsa</span></strong></pre>
</blockquote>
<p style="color: #000000;">Finalmente para obtener los scripts para la creación de claves en la terminal introducimos el siguiente comando:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">make-cadir /etc/openvpn/easy-rsa</span></strong></pre>
</blockquote>
<h6 style="color: #000000;">Nota: Algunas de las distros que funcionan con easy-rsa 3.0 son Ubuntu 14.04, Linux Mint 16, etc.</h6>
<p style="color: #000000;"><strong>Para ejecutar los scripts que acabamos de copiar o de obtener, tenemos que ir a la ubicación donde los guardamos</strong>. Para ello ingresamos el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">cd /etc/openvpn/easy-rsa</span></strong></pre>
</blockquote>
<p style="color: #000000;"><strong>Antes de ejecutar los scripts editaremos el fichero vars para modificar una serie de parámetros</strong>. Para modificar el fichero vars se tiene que introducir el siguiente comando en la terminal:</p>

<pre style="color: #000000;"><strong><span style="color: #0090d3;">nano vars</span></strong></pre>
<h5 style="color: #000000;">Tamaño de las claves</h5>
<p style="color: #000000;">Una vez abierto el editor de texto tenemos que <strong>localizar y modificar la siguiente línea</strong>:</p>
<p style="color: #000000;"><strong><span style="color: #0090d3;">export_KEY_SIZE=1024</span></strong></p>
<p style="color: #000000;">Una vez encontrada la sustituyen <strong>por la siguiente linea</strong>:</p>
<p style="color: #000000;"><strong><span style="color: #0090d3;">export_KEY_SIZE=2048</span></strong></p>

<h6 style="color: #000000;">Nota: Con esta modificación estamos incrementando el tamaño de la claves privadas (.key) que vamos a generar y también del parámetro de Diffie Hellman. Con esta modificación incrementarios del tamaño de las claves de 1024 bits a 2048 bits. También seria posible usar 4096 bits. Este parámetro no tiene porqué penalizar en exceso el rendimiento del servidor. Únicamente penalizará el proceso autentificación Handshake de SSL/TLS.</h6>
<h5 style="color: #000000;">Datos de la entidad emisora de los certificados</h5>
<p style="color: #000000;"><strong>Seguidamente tenemos que introducir los datos de la entidad emisora de los certificados</strong> que seremos nosotros mismos Para ello tenemos que localizar las siguientes lineas:</p>
<p style="color: #000000;"><span style="color: #0090d3;">export KEY_COUNTRY=”US”</span>
<span style="color: #0090d3;">export KEY_PROVINCE=”CA”</span>
<span style="color: #0090d3;">export KEY_CITY=”SanFrancisco”</span>
<span style="color: #0090d3;">export KEY_ORG=”Fort-Funston”</span>
<span style="color: #0090d3;">export KEY_EMAIL=”me@myhost.mydomain”</span>
<span style="color: #0090d3;">export KEY_EMAIL=mail@host.domain</span>
<span style="color: #0090d3;">export KEY_CN=Changeme</span>
<span style="color: #0090d3;">export KEY_CN=Changeme</span>
<span style="color: #0090d3;">export KEY_OU=Changeme</span></p>
<p style="color: #000000;">Una vez localizadas las lineas tan solo se tienen reemplezar el contenido por defecto por nuestros datos reales. En mi caso los datos a rellenar podrían ser:</p>
<p style="color: #000000;"><span style="color: #0090d3;">export KEY_COUNTRY=”ES” “<span style="color: #000000;">Poner las 2 iniciales de tu país</span>”</span>
<span style="color: #0090d3;">export KEY_PROVINCE=”CA” “<span style="color: #000000;">Poner las 2 iniciales de tu provinci</span>a”</span>
<span style="color: #0090d3;">export KEY_CITY=”s*******a” “<span style="color: #000000;">Poner el nombre de tu ciudad</span>”</span>
<span style="color: #0090d3;">export KEY_ORG=”geekland” “<span style="color: #000000;">Poner el nombre de la organización</span>”</span>
<span style="color: #0090d3;">export KEY_EMAIL=”xxxxxxx@gmail.com” “<span style="color: #000000;">Usar vuestra dirección de email</span>”</span>
<span style="color: #0090d3;">export KEY_EMAIL=xxxxxxx@gmail.com “<span style="color: #000000;">Usar vuestra dirección de email</span>”</span>
<span style="color: #0090d3;">export KEY_CN= wheezy “<span style="color: #000000;">Usar el nombre del host del servidor</span>”</span>
<span style="color: #0090d3;">export KEY_NAME=vpnkey “<span style="color: #000000;">Designa el nombre de la entidad certificadora que se creará</span>”</span>
<span style="color: #0090d3;">export KEY_OI=IT “<span style="color: #000000;">Departamento de la empresa</span>”</span></p>

<h6 style="color: #000000;">Nota: Dentro de este fichero también podemos configurar el tiempo de validez que tendrá nuestra entidad certificadora y el tiempo de validez que tendrán los certificados y claves que crearemos. El valor estándar de validez son 3650 días que no voy a tocar.</h6>
<p style="color: #000000;"><strong>Una vez modificado el archivo vars guardamos los cambios y lo cerramos</strong>. Ahora tendremos que exportar sus variables. Para exportar sus variables tenemos que teclear el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><span style="color: #0090d3;"><strong>source ./vars</strong></span></pre>
</blockquote>
<p style="color: #000000;">Seguidamente ejecutaremos el script <strong><span style="color: #0090d3;">clean-all</span></strong>. El script clean-all borrará la totalidad de claves que podrían existir en la ubicación <strong><span style="color: #0090d3;">/etc/openvpn/easy-rsa/keys</span></strong>. Para ejecutar el script tenemos que teclear el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">./clean-all</span></strong></pre>
</blockquote>
<p style="color: #000000;"><strong>El siguiente paso es generar los parámetros de Diffie Hellman</strong>. Los parámetros de Diffie Hellman se utilizarán para poder intercambiar las claves ente cliente y servidor de forma segura. Para poder realizar este paso <strong>tenemos que teclear el siguiente comando en la terminal</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">./build-dh</span></strong></pre>
</blockquote>
<p style="color: #000000;">Al terminar el proceso dentro de la ubicación <strong><span style="color: #0090d3;">/etc/openvpn/easy-rsa/keys</span></strong> se habrá creado el archivo <strong><span style="color: #0090d3;">dh2048.pe</span><span style="color: #0090d3;">m</span></strong> que contiene los parámetros Diffie Hellman.</p>

<h6 style="color: #000000;">Nota: Para quien requiera información adicional de los parámetros de Diffie Hellman puede consultar el siguiente <a style="color: #0090d3;" title="Explicación de los parámetros de Diffie-Hellman" href="https://es.wikipedia.org/wiki/Diffie-Hellman" target="_blank">enlace</a>. Este parámetro se usará poder un intercambio de claves entre 2 participantes de forma segura.</h6>
<p style="color: #000000;">En la siguiente captura de pantalla podrán ver una muestra de los pasos realizados hasta el momento:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/5-Creando-buildi-heaffy.png" target="_blank"><img class="size-medium wp-image-4405 alignnone" title="5- Creando Diffie Hellman" src="http://geekland.hol.es/wp-content/uploads/2014/01/5-Creando-buildi-heaffy-300x195.png" alt="5 Creando buildi heaffy 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>
<p style="color: #000000;">Finalmente <strong>vamos a a crear el certificado y la clave privada de nuestra propia autoridad certificadora</strong>. <strong>Para ello tenemos que teclear el siguiente comando en la terminal</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">./build-ca</span></strong></pre>
</blockquote>
<p style="color: #000000;">Durante el proceso de creación se les hará una serie de preguntas para incorporar información dentro del certificado que se creará. Como anteriormente hemos editado el fichero <strong><span style="color: #0090d3;">vars</span></strong> ahora solo nos tenemos que limitar a aceptar el valor por defecto de las preguntas que nos hacen.</p>
<p style="color: #000000;">Al terminar el proceso dentro de la ubicación<strong><span style="color: #0090d3;"> /etc/openvpn/easy-rsa/keys</span></strong> se ha creado<span style="color: #0090d3;"><strong>ca.crt</strong></span> y <span style="color: #0090d3;"><strong>ca.key</strong></span>:</p>
<p style="color: #000000;"><span style="color: #0090d3;"><strong>ca.crt:</strong></span> Es el <strong>certificado raíz público</strong> de la autoridad de certificación (CA)
<span style="color: #0090d3;"><strong>ca.key:</strong></span> Este fichero contiene <strong>la clave privada de la autoridad de certificación</strong> (CA). Este archivo debe mantenerse protegido y no debe estar al alcance de terceros.</p>
<p style="color: #000000;">Una vez creado el certificado y la clave de vuestra autoridad certificador la pantalla de vuestro ordenador tiene que presentar el siguiente estado:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/6-Entidad-certificadora-creada.png" target="_blank"><img class="size-medium wp-image-4408 alignnone" title="6- Entidad certificadora creada" src="http://geekland.hol.es/wp-content/uploads/2014/01/6-Entidad-certificadora-creada-300x195.png" alt="6 Entidad certificadora creada 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>

<h2 style="color: #000000;">CREAR EL CERTIFICADOS Y LA CLAVE DEL SERVIDOR OPENVPN</h2>
<p style="color: #000000;">A estas alturas ya lo tenemos todo listo<strong> para poder crear el certificado y clave de nuestro servidor</strong>. Para ello <strong>introducimos el siguiente comando en la terminal</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">./build-key-server whezzyVPN</span></strong></pre>
</blockquote>
<h6 style="color: #000000;">Nota: whezzy VPN es el nombre del servidor. Vosotros tenéis que introducir el nombre que vosotros queráis.</h6>
<p style="color: #000000;">Una vez introducido este comando se nos hará una serie de preguntas. Simplemente tienen que contestar el valor por defecto ya que anteriormente hemos modificado el archivo <strong><span style="color: #0090d3;">vars</span></strong>.</p>
<p style="color: #000000;">Al terminar el proceso dentro de la ubicación <strong><span style="color: #0090d3;">/etc/openvpn/easy-rsa/key</span><span style="color: #0090d3;">s</span></strong> se habrán creado los siguientes archivos:</p>
<p style="color: #000000;"><span style="color: #0090d3;"><strong>whezzyVPN.key:</strong></span> Este fichero contiene la <strong>clave privada del servidor</strong>. Este archivo no debe estar al alcance de nadie.</p>
<p style="color: #000000;"><span style="color: #0090d3;"><strong>whezzyVPN.crt:</strong></span> Este fichero corresponde al <strong>certificado público del servidor</strong>.</p>
<p style="color: #000000;"><span style="color: #0090d3;"><strong>whezzyVPN.csr:</strong></span> Este <strong>archivo es la petición de certificado que se envía a la autoridad de certificación</strong>. Mediante la información que contiene el archivo .csr, la autoridad de certificación podrá realizar el certificado del servidor una vez hayan realizado las comprobaciones de seguridad pertinentes.</p>
<p style="color: #000000;">Una vez creado el certificado y la clave del servidor la pantalla de vuestro ordenador tiene que presentar el siguiente estado:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/7-Certificador-y-clave-servidor-creado.png" target="_blank"><img class="size-medium wp-image-4406 alignnone" title="7- Certificador y clave servidor creado" src="http://geekland.hol.es/wp-content/uploads/2014/01/7-Certificador-y-clave-servidor-creado-300x195.png" alt="7 Certificador y clave servidor creado 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>

<h2 style="color: #000000;">CREAR EL CERTIFICADO Y LAS CLAVES DE LOS CLIENTES</h2>
<p style="color: #000000;"><strong>El siguiente paso es crear los certificados y las claves de los clientes</strong> que se podrán conectar al servidor VPN. <strong>Para ello tenemos que teclear el siguiente comando en la terminal</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">./build-key usuariovpn</span></strong></pre>
</blockquote>
<h6 style="color: #000000;">Nota: <span style="color: #0090d3;">usuariovpn</span> es el nombre de usuario que vamos a crear. En vuestro caso tendréis que reemplazar usuariovpn por el nombre que queráis.</h6>
<p style="color: #000000;">Una vez introducido este comando se nos hará una serie de preguntas. Simplemente tienen que contestar el valor por defecto ya que anteriormente hemos editado el fichero <strong><span style="color: #0090d3;">vars</span></strong>.</p>
<p style="color: #000000;">Al terminar el proceso dentro de la ubicación <span style="color: #0090d3;"><strong>/etc/openvpn/easy-rsa/keys</strong></span> se habrán creado los siguientes archivos</p>
<p style="color: #000000;"><strong><span style="color: #0090d3;">usuariovpn.key:</span></strong> Este fichero contiene la <strong>clave privada del cliente</strong>. Este archivo no debe estar al alcance de nadie.
<strong><span style="color: #0090d3;">usuariovpn.crt:</span></strong> Este fichero corresponde corresponde al <strong>certificado público del servidor</strong>.
<strong><span style="color: #0090d3;">usuariovpn.csr:</span></strong> Este archivo es<strong> la petición de certificado que es envía a la autoridad de certificación</strong>. Mediante la información contenida en el archivo .csr, la autoridad de certificación podrá realizar el certificado del cliente una vez hayan realizado las comprobaciones de seguridad pertinentes.</p>

<h6 style="color: #000000;">Nota: El procedimiento de generación de clientes se deberá repetir tantas veces como clientes queráis que tenga el servidor OpenVPN.</h6>
<p style="color: #000000;">Una vez creado el certificado y la clave del cliente, la pantalla de vuestro ordenador tiene que presentar el siguiente estado:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/8-Certificados-y-claves-clientes-creados.png" target="_blank"><img class="size-medium wp-image-4407 alignnone" title="8- Certificados y claves clientes creados" src="http://geekland.hol.es/wp-content/uploads/2014/01/8-Certificados-y-claves-clientes-creados-300x195.png" alt="8 Certificados y claves clientes creados 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>

<h2 style="color: #000000;">FORTIFICAR LA SEGURIDAD DEL SERVIDOR OPENVPN CON TLS-AUTH</h2>
<h6 style="color: #000000;">Nota: Esto paso en principio no es necesario pero lo realizaremos para incrementar la seguridad de nuestro servidor VPN.</h6>
<p style="color: #000000;">Ahora <strong>generamos otra clave. Esta clave nos servirá para agregar soporte para usar la autentificación TLS</strong> y de este modo fortificar la seguridad del servidor VPN. Para generar la clave para poder fortificar el servidor se tiene que introducir el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">cd /etc/openvpn/easy-rsa/keys</span></strong></pre>
</blockquote>
<p style="color: #000000;">Una vez hemos accedido a la ubicación <strong><span style="color: #0090d3;">/etc/opnevpn/easy-rsa/keys</span></strong> tecleamos el siguiente comando:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">openvpn --genkey --secret ta.key</span></strong></pre>
</blockquote>
<p style="color: #000000;">Justo al ejecutar el comando, Como se puede ver en la captura de pantalla, se generará una clave con el nombre <strong><span style="color: #0090d3;">ta.key</span></strong> en la misma ubicación dónde hemos aplicado el comando.</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/9-Autentificaci%C3%B3n-TLS.png" target="_blank"><img class="size-medium wp-image-4409 alignnone" title="9- Autentificación TLS" src="http://geekland.hol.es/wp-content/uploads/2014/01/9-Autentificaci%C3%B3n-TLS-300x195.png" alt="9 Autentificación TLS 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>
<p style="color: #000000;"><strong>La clave creada servirá para introducir una firma digital HMAC en todas las transacciones del protocolo handshake de SSL/TLS entre el cliente y el servidor. De esta forma podremos verificar la integridad de los paquetes intercambiados entre el cliente y el servidor VPN, y en el caso que un cliente intente conectarse al servidor VPN sin poseer la clave para firmar los paquetes la conexión se rechazará automáticamente</strong>. Además con el uso de autentificación TLS también conseguiremos prevenir los siguientes ataques:</p>

<ol style="color: #000000;">
	<li>Ataques de denegación de servicio <a style="color: #0090d3;" title="Explicación de un ataque de denegación de servicio" href="https://es.wikipedia.org/wiki/Ataque_de_denegaci%C3%B3n_de_servicio" target="_blank">DoS</a>.</li>
	<li>Ataques de denegación de servicio por inundación UDP al puerto del VPN.</li>
	<li>Escaneo de puertos en nuestro servidor para intentar averiguar vulnerabilidades.</li>
</ol>
<h2 style="color: #000000;">UBICACIÓN DE LAS CLAVES GENERADAS</h2>
<p style="color: #000000;">A estas alturas hemos generado multitud de claves y certificados. Si se han seguido los pasos detalladamente, la totalidad de claves se hallan en la ubicación <span style="color: #0090d3;">/etc/openvpn/easy-rsa/keys</span>.</p>
<p style="color: #000000;">Anteriormente ya he detallado el uso de cada una de la claves. Seguidamente pasaré a detallar la ubicación de cada una de las claves:</p>

<table style="color: #000000;" width="613" cellspacing="0" cellpadding="4"><colgroup> <col width="102" /> <col width="213" /> <col width="214" /> <col width="51" /></colgroup>
<tbody>
<tr valign="TOP">
<td width="102">
<p align="CENTER"><em><strong>Archivo</strong></em></p>
</td>
<td width="213">
<p align="CENTER"><em><strong>Descripción</strong></em></p>
</td>
<td width="214">
<p align="CENTER"><em><strong>Ubicación</strong></em></p>
</td>
<td width="51">
<p align="CENTER"><em><strong>Secreto</strong></em></p>
</td>
</tr>
<tr class="alternate" valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;"><em>dh2048.pem</em></span></p>
</td>
<td width="213">
<p align="CENTER">Parámetros Diffie Hellman</p>
</td>
<td width="214">
<p align="CENTER">Servidor (<span style="color: #0090d3;">/etc/openvpn</span>)</p>
</td>
<td width="51">
<p align="CENTER">Sí</p>
</td>
</tr>
<tr valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;"><em>ca.crt</em></span></p>
</td>
<td width="213">
<p align="CENTER">Certificado raíz de la entidad certificadora</p>
</td>
<td width="214">
<p align="CENTER">Servidor (<span style="color: #0090d3;">/etc/openvpn</span>) y cliente</p>
</td>
<td width="51">
<p align="CENTER">No</p>
</td>
</tr>
<tr class="alternate" valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;"><em>ca.key</em></span></p>
</td>
<td width="213">
<p align="CENTER">Clave de la entidad certificadora</p>
</td>
<td width="214">
<p align="CENTER">Servidor (<span style="color: #0090d3;">/etc/openvpn</span>)</p>
</td>
<td width="51">
<p align="CENTER">Sí</p>
</td>
</tr>
<tr valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;"><em>whezzyVPN.key</em></span></p>
</td>
<td width="213">
<p align="CENTER">Clave del servidor VPN</p>
</td>
<td width="214">
<p align="CENTER">Servidor (<span style="color: #0090d3;">/etc/openvpn</span>)</p>
</td>
<td width="51">
<p align="CENTER">Sí</p>
</td>
</tr>
<tr class="alternate" valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;">whezzyVPN.crt</span></p>
</td>
<td width="213">
<p align="CENTER">Certificado del servidor VPN</p>
</td>
<td width="214">
<p align="CENTER">Servidor (<span style="color: #0090d3;">/etc/openvpn</span>) y cliente</p>
</td>
<td width="51">
<p align="CENTER">No</p>
</td>
</tr>
<tr valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;">whezzyVPN.csr</span></p>
</td>
<td width="213">
<p align="CENTER">Archivo de petición de certificado</p>
</td>
<td width="214">
<p align="CENTER">Servidor (<span style="color: #0090d3;">/etc/openvpn</span>)</p>
</td>
<td width="51">
<p align="CENTER">No</p>
</td>
</tr>
<tr class="alternate" valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;">usuariovpn.key</span></p>
</td>
<td width="213">
<p align="CENTER">Clave privada del cliente VPN</p>
</td>
<td width="214">
<p align="CENTER">Cliente</p>
</td>
<td width="51">
<p align="CENTER">Sí</p>
</td>
</tr>
<tr valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;">usuariovpn.crt</span></p>
</td>
<td width="213">
<p align="CENTER">Certificado del cliente VPN</p>
</td>
<td width="214">
<p align="CENTER">Cliente</p>
</td>
<td width="51">
<p align="CENTER">No</p>
</td>
</tr>
<tr class="alternate" valign="TOP">
<td width="102">
<p align="CENTER"><span style="color: #0090d3;">usuariovpn.csr</span></p>
</td>
<td width="213">
<p align="CENTER">Archivo de petición de certificado</p>
</td>
<td width="214">
<p align="CENTER">Servidor (<span style="color: #0090d3;">/etc/openvpn</span>)</p>
</td>
<td width="51">
<p align="CENTER">No</p>
</td>
</tr>
</tbody>
</table>
<h6 style="color: #000000;">Nota: Tienen que trasladar cada una de las llaves mencionadas en las ubicaciones que se detallan en el cuadro. Recuerden transmitir y trasladar las claves y certificados del servidor al cliente por un canal seguro.</h6>
<h2 style="color: #000000;">ASEGURAR QUE LAS PETICIONES DNS SE REALIZAN POR EL VPN</h2>
<p style="color: #000000;">Otro punto a contemplar para asegurar que nuestro servidor VPN sea seguro es que nadie pueda capturar nuestras peticiones DNS para saber donde nos estamos conectando.</p>

<h6 style="color: #000000;">Nota: Quien no sepa que son las peticiones DNS puede consultar el siguiente <a style="color: #0090d3;" title="Elegir el mejor servidor DNS" href="http://geekland.hol.es/elegir-el-mejor-servidor-dns/" target="_blank">enlace</a>.</h6>
<p style="color: #000000;"><strong>Para que nadie capture nuestras peticiones DNS lo que realizaremos es canalizar la totalidad de nuestras peticiones a través del túnel del servidor OpenVPN</strong>. Así las peticiones DNS se enviarán al servidor VPN de forma cifrada y será el servidor OpenVPN el encargado de resolverlas. <strong>Para poder realizar lo que acabo de describir lo primero que tienen que realizar es instalar dnsmasq</strong>. Para poder instalar dnsmasq teclean el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">apt-get install dnsmasq</span></strong></pre>
</blockquote>
<p style="color: #000000;">Una vez instalado dnsmasq lo tenemos que configurar para que escuche las peticiones DNS dirigidas al servidor VPN. Para ello <strong>accedemos al archivo de configuración introduciendo el siguiente comando en la terminal</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">nano /etc/dnsmasq.conf</span></strong></pre>
</blockquote>
<p style="color: #000000;">Una vez abierto el editor de texto <strong>introducen las siguientes líneas</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">listen-address=127.0.0.1,10.8.0.1</span></strong></pre>
<pre><strong><span style="color: #0090d3;">bind interfaces</span></strong></pre>
</blockquote>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/10-configuraci%C3%B3n-dnsmasq.png" target="_blank"><img class="size-medium wp-image-4410 alignnone" title="10- configuración dnsmasq" src="http://geekland.hol.es/wp-content/uploads/2014/01/10-configuraci%C3%B3n-dnsmasq-300x195.png" alt="10 configuración dnsmasq 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>

<h6 style="color: #000000;">Nota: Introduciendo la primera línea lo que estamos haciendo es que Dnsmasq solamente tenga en cuenta las peticiones DNS que se dirijan a las interfaces <span style="color: #0090d3;">[lo]: 127.0.0.1</span> y <span style="color: #0090d3;">[tun0]: 10.8.0.1</span> que es la de nuestro servidor VPN.</h6>
<h6 style="color: #000000;">Nota: Con la segunda línea estamos habilitando que dnsmasq tenga la capacidad de escuchar solo determinadas interfaces como por ejemplo las dos que hemos definido antes. La <span style="color: #0090d3;">[lo] 127.0.0.1</span> y la<span style="color: #0090d3;">[tun0] 10.8.0.1</span></h6>
<p style="color: #000000;">Ahora tan solo tienen que <strong>guardar los cambios y salir del archivo de configuración</strong>. La configuración ha terminado y solamente hace falta reiniciar los servicios openvpn y dnsmasq. Para ello teclean los siguientes comandos en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">/etc/init.d/openvpn restart</span></strong></pre>
<pre><strong><span style="color: #0090d3;">/etc/init.d/dnsmasq restart</span></strong></pre>
</blockquote>
<p style="color: #000000;">Es posible que cuando reinicien los servicios o arranquen el sistema vean un error parecido al de la captura de la pantalla:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/11-error-dnsmasq.png" target="_blank"><img class="size-medium wp-image-4411 alignnone" title="11- error dnsmasq" src="http://geekland.hol.es/wp-content/uploads/2014/01/11-error-dnsmasq-300x195.png" alt="11 error dnsmasq 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>
<p style="color: #000000;"><span style="color: #0090d3;"><strong>Starting DNS forwarder and DHCP server: dnsmasq</strong></span>
<span style="color: #0090d3;"><strong>dnsmasq: failed to creat listening to socket for 10.8.0.1: No se puede asignar la dirección solicitada.</strong></span></p>
<p style="color: #000000;">Esto error es debido a que Dnsmaq arranca antes de que se cree la interfaz <strong><span style="color: #0090d3;">[tun0]</span></strong>. Por lo tanto cuando intenta escuchar la interfaz <strong><span style="color: #0090d3;">[tun0]</span></strong> nos dará el error porqué <strong><span style="color: #0090d3;"> [tun0]</span></strong> no existe. Para solucionar este problema y que dnsmasq puede realizar su función tan solo tiene que modificar el archivo <strong><span style="color: #0090d3;">/etc/rc.local</span></strong>. Para ello en la terminal escriben:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">nano /etc/rc.local</span></strong></pre>
</blockquote>
<p style="color: #000000;">Se abrirá el editor de textos y ahora, debajo de las reglas de iptables tan solo tienen que escribir:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">/etc/init.d/dnsmasq restart</span></strong></pre>
</blockquote>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/12-fichero-rc.local_.png" target="_blank"><img class="size-medium wp-image-4412 alignnone" title="12- fichero rc.local" src="http://geekland.hol.es/wp-content/uploads/2014/01/12-fichero-rc.local_-300x195.png" alt="12 fichero rc.local  300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>
<p style="color: #000000;">Una vez realizado este paso guardan el fichero y salen. Introduciendo esta linea lo que estamos haciendo es reiniciar el servicio dnsmasq una vez se han ejecutado la totalidad de scripts de inicio (init). De este modo cuando se reinicialice dnsmasq la interfaz <strong><span style="color: #0090d3;">[tun0]</span></strong> ya estará levantada.</p>

<h6 style="color: #000000;">Nota: Para que dnsmasq funcione tienen que tener configurado el servidor VPN tal y como se detalla en el apartado Configurar el servidor.</h6>
<h2 style="color: #000000;">CONFIGURAR EL SERVIDOR OPENVPN</h2>
<p style="color: #000000;">Existen ficheros de configuración standard que deberían funcionar out of the box y que podemos aprovechar para realizar nuestra configuración. <strong>Los ficheros de ejemplo que podemos usar para ver la totalidad de opciones que tenemos disponibles se hallan comprimidos en la siguiente ubicación ubicación:</strong></p>
<p style="color: #000000;"><span style="color: #0090d3;"><strong>/usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz</strong></span></p>
<p style="color: #000000;">Para consultarlos teclear el siguiente comando para acceder a la ubicación de este archivo:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">cd /usr/share/doc/openvpn/examples/sample-config-files</span></strong></pre>
</blockquote>
<p style="color: #000000;">Seguidamente copiamos el archivo comprimido que dispone de los archivos de muestra de configuración en la ubicación <span style="color: #0090d3;">/etc/openvpn</span>. Para ello tecleamos el siguiente comando:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">cp -a /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz /etc/openvpn/</span></strong></pre>
</blockquote>
<p style="color: #000000;">Seguidamente accedemos a la ubicación donde hemos copiado el archivo comprimido que contiene los archivos de configuración:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">cd /etc/openvpn</span></strong></pre>
</blockquote>
<p style="color: #000000;">Para descomprimir el archivo que contiene los archivos de configuración tecleamos:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">gunzip server.conf.gz</span></strong></pre>
</blockquote>
<p style="color: #000000;"><strong>Una vez descomprimido el archivo ya podemos consultar los ejemplos de configuración tanto del cliente como del servidor</strong>. Para ver y modificar la configuración estándar para adaptarla a nuestras necesidades tienen que<strong> teclear el siguiente comando en la terminal</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">nano server.conf</span></strong></pre>
</blockquote>
<p style="color: #000000;">Se abrirá el editor de texto en el que podrán ver de forma detallada las opciones de configuración de ejemplo del servidor. Ahora tendréis que c<strong>omprobar que la totalidad de parámetros que se muestran en la tabla de este apartado estén dentro del fichero de configuración</strong> de ejemplo que es el que vamos a usar. En el caso de que los parámetros estén comentados habrá que descomentarlos, en el caso que no existen se deberán añadir y/o modificar.</p>

<table style="color: #000000;" width="643" cellspacing="0" cellpadding="0"><colgroup> <col width="159" /> <col width="483" /></colgroup>
<tbody>
<tr>
<th width="159">
<p align="LEFT"><strong>Parámetro</strong></p>
</th>
<th width="483">
<p align="LEFT"><strong>Descripción</strong></p>
</th>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>dev tun</em></span></td>
<td width="483">Dispositivo virtual en el cual se creara el túnel.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>proto udp</em></span></td>
<td width="483">Protocolo de la conexión VPN. También podríamos usar el tcp.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>port 1194</em></span></td>
<td width="483">Puerto de escucha del servicio. El puerto de escucha se puede modificar.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>ca ca.crt</em></span></td>
<td width="483">Certificado de la autoridad certificadora que creamos.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>cert whezzyVPN.crt</em></span></td>
<td width="483">Certificado del servidor que hemos creado.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>key whezzyVPN.key</em></span></td>
<td width="483">Clave privada del servidor que hemos creado.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>dh dh2048.pem</em></span></td>
<td width="483">Carga de los parámetro de Diffie Hellman.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>Server 10.8.0.0 255.255.255.0</em></span></td>
<td width="483">Indicamos que a los clientes del VPN se les asignará IP del tipo<span style="color: #0090d3;">10.8.0.0/24</span></td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>ifconfig-pool-persist ipp.txt</em></span></td>
<td width="483">Se crea un fichero <span style="color: #0090d3;">ipp.txt</span> en el que se registran las IP de los clientes que se conectan al servidor VPN.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>push “route 192.168.1.0 255.255.255.0”</em></span></td>
<td width="483"><span style="color: #000000;">Con esta línea hacemos que los paquetes que tengan como destino la red <span style="color: #0090d3;">192.168.1.0</span> viajen por la interfaz del túnel (<span style="color: #0090d3;">tun0</span>). De esta forma el cliente VPN se podrá comunicar con cualquier máquina de la red<span style="color: #0090d3;">192.168.1.0</span>.</span></td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>keepalive 10 120</em></span></td>
<td width="483">El servidor VPN enviará un ping cada 10 segundos y como máximo esperará 120 segundos para que el cliente de una contestación.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>tls-aut ta.key 0</em></span></td>
<td width="483">Activación de la autentificación TLS en el servidor.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>comp-lzo</em></span></td>
<td width="483">Activar compresión LZO para la transmisión de datos.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>max-clients 10</em></span></td>
<td width="483">Número máximo de clientes que se pueden conectar de forma simultanea. El valor se puede modificar según las necesidades.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>user nobody</em></span></td>
<td width="483">Para limitar los privilegios del demonio de VPN hacemos que funcione con el usuario <span style="color: #0090d3;">nobody</span>.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>group nogroup</em></span></td>
<td width="483">Para limitar los privilegios del demonio de VPN hacemos que funcione con el grupo <span style="color: #0090d3;">nogroup</span>.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>push “redirect-gateway def1”</em></span></td>
<td width="483">Para que la totalidad de tráfico vaya a través de nuestro VPN</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>push “dhcp-option DNS 10.8.0.1”</em></span></td>
<td width="483">Estamos definiendo que las peticiones DNS de los clientes se hagan a través del servidor VPN ubicado en <span style="color: #0090d3;">10.8.0.1</span></td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>cipher AES-256-CBC</em></span></td>
<td width="483">Por defecto el algoritmo de cifrado de OpenVPN es Blowfish con un tamaño de clave de 128 bits. Quien crea que no es suficiente puede añadir esta línea para cambiar el algoritmo de cifrado a AES con un clave de cifrado de 256 bits. Para ver todos los algoritmos de cifrado disponibles teclear <span style="color: #0090d3;"><strong>openvpn –show-ciphers</strong></span> en la terminal.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>persist-key</em></span></td>
<td width="483">En caso que el servidor OpenVPN se caiga las claves no tendrán que ser analizadas de nuevo.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>persist-tun</em></span></td>
<td width="483">El dispositivo <span style="color: #0090d3;">tun0</span> no tendrá que ser reabierto ni cerrado en el caso que tengamos que reiniciar el servidor.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>status openvpn-status-log</em></span></td>
<td width="483">Log donde se guardará información respecto al túnel creado.</td>
</tr>
<tr class="alternate">
<td width="159"><em><span style="color: #0090d3;">plugin /usr/lib/openvpn/openvn-auth-pam.so</span><span style="color: #0090d3;">/etc/pam.d/login</span></em></td>
<td width="483">Activación del script encargado de realizar la autenticación del usuario y del cliente. (Ver el apartado “Autentificación del cliente mediante usuario y password”)</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>verb 3</em></span></td>
<td width="483">Grado de detalle del estado del túnel en los logs.</td>
</tr>
</tbody>
</table>
<p style="color: #000000;">Una vez tenemos listo el fichero de configuración tan solo tenemos que guardar los cambios y cerrarlo.</p>

<h6 style="color: #000000;">Nota: Si queremos que los clientes que estan conectados al servidor VPN puedan comunicarse entre ellos tenemos que añadir la frase <span style="color: #0090d3;">client-to-client</span> en el fichero de configuración del servidor.</h6>
<h6 style="color: #000000;">Nota: Si leéis con detalle el fichero de configuración podréis aplicar configuraciones distintas a las que se detallan en el post.</h6>
<h6 style="color: #000000;">Nota: La configuración propuesta en este apartado se tendrá que adaptar a las características de vuestra red y a vuestras necesidades.</h6>
<h2 style="color: #000000;">CONFIGURAR EL CLIENTE OPENVPN</h2>
<p style="color: #000000;">Una vez configurado el servidor ahora pasaremos a configurar el cliente. Para ello dentro de la ubicación <strong><span style="color: #0090d3;">/etc/openvpn</span></strong> <strong>tecleamos el siguiente comando</strong>:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">nano client.conf</span></strong></pre>
</blockquote>
<p style="color: #000000;">Se abrirá el fichero de configuración en el que podrán ver un ejemplo de configuración para un cliente estándar. <strong>Aseguramos que el fichero de configuración estándar tenga los parámetros que se muestran en la tabla de este apartado</strong>. En caso de no tenerlos habrá que añadirlos manualmente, en el caso de que los parámetros estén comentados habrá que descomentarlos y en el caso que no existan se deberán añadir y/o modificar.</p>

<table style="color: #000000;" width="643" cellspacing="0" cellpadding="0"><colgroup> <col width="159" /> <col width="483" /></colgroup>
<tbody>
<tr>
<th width="159">
<p align="LEFT"><strong>Parámetro</strong></p>
</th>
<th width="483">
<p align="LEFT"><strong>Descripción</strong></p>
</th>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>dev tun</em></span></td>
<td width="483">Dispositivo virtual en el cual se creara el túnel.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>proto udp</em></span></td>
<td width="483">Protocolo de transmisión de paquetes del servidor VPN. Se puede usar TCP.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>remote geekland.sytes.net 1194</em></span></td>
<td width="483"><span style="color: #000000;">Dirección IP pública/Host DNS dinámico y puerto de escucha del servidor VPN. El puerto <span style="color: #0090d3;">1194</span> se puede cambiar. Si lo cambiamos deberemos adaptar el resto de configuraciones al nuevo puerto</span></td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>resolv-retry infinite</em></span></td>
<td width="483">El cliente intentará de forma indefinida resolver la dirección o nombre de host indicado por la directiva remote (<span style="color: #0090d3;">geeekland.sytes.net</span>).</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>nobind</em></span></td>
<td width="483"><span style="color: #000000;">A los clientes se les asignará puertos dinámicos (no privilegiados) cuando haya retorno de paquetes del servidor al cliente.</span></td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>user nobody</em></span></td>
<td width="483">Para limitar los privilegios de los clientes que se conectan al VPN les asignamos el usuario <span style="color: #0090d3;">nobody</span>. (no necesario para windows)</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>group nogroup</em></span></td>
<td width="483">Para limitar los privilegios de los clientes que se conectan al VPN les asignamos el grupo <span style="color: #0090d3;">nogroup</span>. (no necesario para windows)</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>persist-key</em></span></td>
<td width="483">En caso que el servidor OpenVPN sea reiniciado no se tendrán que volver a leer las claves.</td>
</tr>
<tr class="alternate">
<td width="159"><em><span style="color: #0090d3;">persist-tun</span></em></td>
<td width="483">El dispositivo <span style="color: #0090d3;">tun0</span> no tendrá que ser reabierto ni cerrado en el caso que tengamos que reiniciar el cliente Vpn.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>ca ca.crt</em></span></td>
<td width="483">Certificado de la autoridad certificadora que creamos</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>cert usuariovpn.crt</em></span></td>
<td width="483">Certificado del cliente</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>key usuariovpn.key</em></span></td>
<td width="483">Clave privada del cliente</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>ns-cert-type server</em></span></td>
<td width="483">Para prevenir ataques man in the middle. Con esta frase hacemos que los clientes solo puedan aceptar un certificado de servidor del tipo servidor “<span style="color: #0090d3;">nsCertType=server</span>”. En este campo podríamos aplicar otras alternativas similares como por ejemplo “<span style="color: #0090d3;">remote-cert-tls server</span>“.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>tls-auth ta.key 1</em></span></td>
<td width="483">Activación de la autentificación TLS en el cliente.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>cipher AES-256-CBC</em></span></td>
<td width="483">Por defecto el algoritmo de cifrado de OpenVPN es Blowfish con un tamaño de clave de 128 bits. Quien crea que no es suficiente puede añadir esta línea para cambiar el algoritmo de cifrado a AES con un clave de cifrado de 256 bits. Para ver todos los algoritmos de cifrado disponibles teclear <strong><span style="color: #0090d3;">openvpn –show-ciphers</span></strong> en la terminal.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>auth-user-pass</em></span></td>
<td width="483">Para indicar que el cliente tiene que introducir un nombre de usuario y un password.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>auth-nocache</em></span></td>
<td width="483">Para evitar que los password queden almacenados en la memoria cache de los clientes.</td>
</tr>
<tr>
<td width="159"><span style="color: #0090d3;"><em>comp-lzo</em></span></td>
<td width="483">Activar compresión LZO para la transmisión de datos.</td>
</tr>
<tr class="alternate">
<td width="159"><span style="color: #0090d3;"><em>verb 3</em></span></td>
<td width="483">Grado de detalle del estado del túnel</td>
</tr>
</tbody>
</table>
<h2 style="color: #000000;">AUTENTIFICACIÓN DEL CLIENTE MEDIANTE LOGIN Y PASSWORD</h2>
<p style="color: #000000;">A pesar de toda la seguridad que hemos implementado hasta el momento podría darse el caso que alguien robará nuestro ordenador. <strong>Si alguien robará nuestro ordenador, teléfono o tablet podría encontrarse con la totalidad de nuestras claves criptográficas y de esta forma podría acceder fácilmente a nuestra red.</strong></p>
<p style="color: #000000;"><strong>Para solucionar este problema vamos a introducir un usuario y un password para los clientes de nuestro servidor vpn</strong>. Para ello tan solo tenemos que añadir uno o los usuarios que queramos.</p>
<p style="color: #000000;">Para añadir un usuario, como por ejemplo el <span style="color: #ff0000;">usuariovpn2</span>, tienen que teclear el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">useradd <span style="color: #ff0000;">usuariovpn2</span> -M -s /bin/false</span></strong></pre>
</blockquote>
<p style="color: #000000;">Una vez creado el usuario tenemos que definir un password del <span style="color: #ff0000;">usuariovpn2</span>. Para ello tecleamos el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">passwd <span style="color: #ff0000;">usuariovpn2</span></span></strong></pre>
</blockquote>
<p style="color: #000000;">Una vez introducido el comando nos pedirá que introduzcamos la clave de usuario y después nos pedirá confirmación.</p>
<p style="color: #000000;">En el caso que a posteriori se precise eliminar el <span style="color: #ff0000;">usuariovpn2</span> tan solo tienen que introducir el siguiente comando en la terminal:</p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">deluser <span style="color: #ff0000;">usuariovpn2</span></span></strong></pre>
</blockquote>
<p style="color: #000000;">Seguidamente en la siguiente captura de pantalla pueden ver un resumen de los pasos realizados:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/13-Creaci%C3%B3n-y-eliminaci%C3%B3n-de-usuarios.png" target="_blank"><img class="size-medium wp-image-4413 alignnone" title="13- Creación y eliminación de usuarios" src="http://geekland.hol.es/wp-content/uploads/2014/01/13-Creaci%C3%B3n-y-eliminaci%C3%B3n-de-usuarios-300x195.png" alt="13 Creación y eliminación de usuarios 300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>

<h6 style="color: #000000;">Nota: Para que la autentificación mediante usuario y password funcione tienen que tener configurado el servidor y el cliente tal y como se detalla en los apartados Configurar el servidor y configurar el cliente.</h6>
<h2 style="color: #000000;">CONFIGURAR IPTABLES PARA EL ENRUTAMIENTO DE PETICIONES</h2>
<p style="color: #000000;"><strong>Cuando el servidor OpenVPN reciba las peticiones de los clientes se deberán enrutar adecuadamente, y además tendremos que tener configurar el firewall de nuestro equipo para que permita el tráfico a través del túnel que se ha creado ente el cliente y el servidor</strong>.</p>
<p style="color: #000000;">Para ello <strong>lo primero que tenemos que hacer es habilitar el IP forwarding</strong>. Para habilitar el IP Forwading de forma permanente <strong>tecleamos el siguiente comando en la terminal:</strong></p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">nano /etc/sysctl.conf</span></strong></pre>
</blockquote>
<p style="color: #000000;">Se abrirá el editor de textos y seguidamente tendremos que <strong>localizar la siguiente linea:</strong></p>
<p style="color: #000000;"><strong><span style="color: #0090d3;">#net.ipv4.ip_forward=1</span></strong></p>
<p style="color: #000000;">Una vez localizada tan solo hay que <strong>descomentarla de forma que quede de la siguiente forma:</strong></p>
<p style="color: #000000;"><span style="color: #0090d3;"><strong>net.ipv4.ip_forward=1</strong></span></p>
<p style="color: #000000;">Guardamos los cambios y cerramos el archivo.</p>
<p style="color: #000000;"><strong>Una vez habilitado el Ipforwarding tenemos que permitir el tráfico por nuestro túnel VPN</strong>, y además tenemos que hacer que los clientes VPN puedan acceder a redes externas públicas y otras subredes dentro de la red VPN. <strong>Para poder conseguir esto en la terminal escriben el siguiente comando:</strong></p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">nano /etc/rc.local</span></strong></pre>
</blockquote>
<p style="color: #000000;"><strong>Una vez se abra el editor de textos tienen que escribir las siguientes reglas en nuestro firewall</strong></p>

<blockquote style="color: #777777;">
<pre><strong><span style="color: #0090d3;">iptables -A FORWARD -i eth0 -o tun0 -m state --state ESTABLISHED,RELATED -j ACCEPT</span></strong></pre>
<pre><strong><span style="color: #0090d3;">iptables -A FORWARD -s 10.8.0.0/24 -o eth0 -j ACCEPT</span></strong></pre>
<pre><strong><span style="color: #0090d3;">iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE</span></strong></pre>
</blockquote>
<h6 style="color: #000000;">Nota: En función de las características de vuestra red y configuración de vuestro firewall es posible que tenga que implementar reglas adicionales a las que se muestran en este ejemplo.</h6>
<p style="color: #000000;"><strong>Con la primera de las reglas</strong> estamos permitiendo el tráfico por el dispositivo virtual en que que se crea el túnel.</p>
<p style="color: #000000;"><strong>Con la segunda de las reglas</strong> estamos permitiendo que los paquetes provenientes de<strong><span style="color: #0090d3;">10.8.0.0/24</span></strong> pueden enviarse o salir por la interfaz de salida <strong><span style="color: #0090d3;">eth0</span></strong>.</p>
<p style="color: #000000;"><strong>Con la tercera de las reglas</strong> estamos diciendo al servidor OpenVPN que cuando reciba una petición de cualquiera de los clientes, proceda el mismo a resolverla y enviarla en representación del cliente.</p>
<p style="color: #000000;">Una vez finalizando el proceso guardan el archivo y cierran el editor de textos. Antes de cerrar el archivo el fichero <strong><span style="color: #0090d3;">/etc/rc.local</span></strong> tendrá un aspecto parecido al siguiente:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/12-fichero-rc.local_.png" target="_blank"><img class="size-medium wp-image-4412 alignnone" title="12- fichero rc.local" src="http://geekland.hol.es/wp-content/uploads/2014/01/12-fichero-rc.local_-300x195.png" alt="12 fichero rc.local  300x195 Crear y configurar servidor openvpn" width="300" height="195" /></a></p>

<h2 style="color: #000000;">CONFIGURAR EL ROUTER Y ABRIR EL PUERTO DEL SERVIDOR OPENVPN</h2>
<p style="color: #000000;">Ya<strong> para finalizar solo nos falta configurar nuestro router, para que redirija las peticiones de los clientes al servidor Opevpn, y abrir el puerto del servidor OpenVPN</strong>. Para realizar esto tenemos que <strong>abrir nuestro navegador y teclear nuestra puerta de entrada</strong>. Una vez realizado esto, tal y como se puede ver en la captura de pantalla, se abrirá una ventana en que nos pedirá nuestro nombre de usuario y contraseña:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/14-Acceder-al-Router.png" target="_blank"><img class="size-medium wp-image-4414 alignnone" title="14- Acceder al Router" src="http://geekland.hol.es/wp-content/uploads/2014/01/14-Acceder-al-Router-300x175.png" alt="14 Acceder al Router 300x175 Crear y configurar servidor openvpn" width="300" height="175" /></a></p>
<p style="color: #000000;">Una vez introducida la información accederemos a la configuración de nuestro router. Seguidamente, tal y como se puede ver en la captura de pantalla, tenemos que acceder a los menús <strong><span style="color: #0090d3;">Advanced / NAT / Virtual Servers</span></strong>:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/15-Acceder-a-Virtual-Servers.png" target="_blank"><img class="size-medium wp-image-4415 alignnone" title="15- Acceder-a-Virtual-Servers" src="http://geekland.hol.es/wp-content/uploads/2014/01/15-Acceder-a-Virtual-Servers-300x169.png" alt="15 Acceder a Virtual Servers 300x169 Crear y configurar servidor openvpn" width="300" height="169" /></a></p>
<p style="color: #000000;">Seguidamente presionamos el botón <strong><span style="color: #0090d3;">Add</span></strong> y nos aparecerá la siguiente pantalla:</p>
<p style="color: #000000;"><a style="color: #0090d3;" href="http://geekland.hol.es/wp-content/uploads/2014/01/16-Abrir-puerto.png" target="_blank"><img class="size-medium wp-image-4416 alignnone" title="16- Abrir puerto" src="http://geekland.hol.es/wp-content/uploads/2014/01/16-Abrir-puerto-300x175.png" alt="16 Abrir puerto 300x175 Crear y configurar servidor openvpn" width="300" height="175" /></a></p>
<p style="color: #000000;">Tal y como se puede ver en la captura de pantalla, en <strong>en el campo</strong> <strong><span style="color: #0090d3;">custom server</span></strong> hay que<strong>escribir un nombre cualquiera</strong>. En mi caso como se puede ver en la captura de pantalla he escrito <strong><span style="color: #0090d3;">OpenVPN</span></strong>. Seguidamente <strong>en el campo</strong> <strong><span style="color: #0090d3;">Server IP Address</span></strong> tenemos que<strong>escribir la IP del servidor OpenVPN</strong>. En mi caso tal y como se puede ver en la captura de pantalla es la <span style="color: #0090d3;"><strong>192.168.1.188</strong>. </span>Finalmente tal y como se puede ver en la captura de imagen<strong>seleccionamos el protocolo</strong> <strong><span style="color: #0090d3;">UDP</span></strong> <strong>y escribimos el puerto de nuestro servidor OpenVPN</strong> (<strong><span style="color: #0090d3;">1194</span></strong>) en los puertos internos y externos.</p>
<p style="color: #000000;"><strong>Presionamos el botón</strong> <strong><span style="color: #0090d3;">Apply/Save</span></strong> y de esta forma todas las peticiones exteriores que lleguen a nuestro router por el puerto <strong><span style="color: #0090d3;">1194</span></strong> serán redirigidas a nuestro servidor OpenVPN.</p>

<h2 style="color: #000000;">COMO CONECTARNOS AL SERVIDOR OPENVPN</h2>
<p style="color: #000000;">En las próximas semanas publicaré una serie de post en los que explicaré de forma detallada los pasos a seguir para conectarnos a nuestro servidor Openvpn en el caso de estar usando los siguientes sistemas operativos:</p>

<ol style="color: #000000;">
	<li><strong><span style="color: #0090d3;">Linux</span></strong></li>
	<li><strong><span style="color: #0090d3;">Android</span></strong></li>
	<li><a style="color: #0090d3;" title="Conectarse a un servidor OpenVPN en Windows" href="http://geekland.hol.es/conectarse-servidor-openvpn-en-windows/" target="_blank"><strong><span style="color: #0090d3;">Windows</span></strong></a></li>
	<li><a style="color: #0090d3;" title="Conectarse a un servidor OpenVPN en iOS" href="http://geekland.hol.es/conectarse-a-un-servidor-openvpn-en-ios/" target="_blank"><strong><span style="color: #0090d3;">iOS</span></strong></a></li>
</ol>
<p style="color: #000000;">De este modo podremos comprobar fácilmente el funcionamiento de nuestro servidor Openvpn.</p>

<h2 style="color: #000000;">SEGURIDAD QUE NOS APORTARÁ EL SERVIDOR OPENVPN</h2>
<p style="color: #000000;">Si se configura el servidor Openvpn, tal y como se detalla en el post, se obtendrá un nivel de seguridad muy elevado y resultará prácticamente invulnerable frente a ataques.</p>
<p style="color: #000000;">La seguridad que aportará el servidor OpenVPN que acabamos de configurar estará compuesta por 3 capas:</p>
<p style="color: #000000;"><strong>Capa 1 “Autentificación TLS”:</strong> Con la autentificación TLS estamos introduciendo una firma digital HMAC a los paquetes antes de empezar la autentificación reciproca entre cliente y servidor. Si no se pasa el test de la firma HMAC, no se llegará ni a iniciar el proceso de autenticación entre cliente y servidor.</p>
<p style="color: #000000;"><strong>Capa 2 “SSL/TLS”:</strong> Mediante las herramientas de seguridad proporcionadas SSL/TLS se realiza el proceso de autentificacion bidireccional entre el cliente y el servidor OpenVPN mediante claves criptográficas.</p>
<p style="color: #000000;"><strong>Capa 3 “Cifrado”:</strong> Dispone de varios tipos de cifrado disponibles en la transmisión de datos entre el cliente y el servidor. Además podemos aplicar medidas para los privilegios del demonio de OpenVPN sean los mínimos para poder realizar la función que tiene que realizar.</p>
<p style="color: #000000;">Todas estas características, más las que se detallan en el post, hacen que OpenVPN sea una opción muy válida para la transmisión segura de datos sensibles. Por esto motivo OpenVPN es el protocolo que utilizan muchas organizaciones en el mundo empresarial. Además OpenVPN es una solución multiplataforma y dentro de lo que cabe no es difícil de configurar si lo comparamos con por ejemplo <a style="color: #0090d3;" title="Explicación de lo que es Ipsec" href="https://es.wikipedia.org/wiki/IPSEC" target="_blank">Ipsec</a>.</p>
<p style="color: #000000;">En lo que a seguridad se refiere también tenemos que destacar que aparte de las 3 capas de seguridad, también hemos implementado un método para que los clientes del VPN tengan que introducir un usuario y un Password. Además la totalidad del tráfico, incluyendo la resolución de las peticiones DNS, será a través del servidor OpenVPN que acabamos instalar y de configurar.</p>
<p style="color: #000000;">Cabe decir que actualmente no se conocen vulnerabilidades importantes en este tipo de servidor VPN. Es posible que se descubran vulnerabilidades pero si vamos aplicando las actualizaciones de seguridad no deberíamos tener problema alguno en lo que a seguridad se refiere.</p>
