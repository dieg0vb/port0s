El primer paso es conectarme desde la red de mi trabajo al ordenador que queremos controlar en remoto. Después, pediremos amablemente a este equipo que sea el quien se conecte con el ordenador de mi casa creando una conexión reversa que luego utilizare desde allí.

&nbsp;
<ul>
	<li>ssh -R 9999:localhost:22 usuario_pc_casa@IP_mi_ordenador</li>
</ul>
Con esto hemos pedido al equipo de la oficina que conecte con el de mi casa y cree un túnel inverso.
Una buena idea es poner esta orden en cron de forma que se ejecute al iniciar el equipo y así siempre tendrás la conexión lista.

&nbsp;

Ahora en mi casa, tengo una conexión entrante desde el equipo de la oficina, pero yo no quiero que me controlen mi equipo desde allí, si no controlar aquel, por lo que voy a conectarme a él empleando esa conexión entrante.

&nbsp;
<ul>
	<li>ssh -p 9999 usuario_pc_oficina@localhost</li>
</ul>
Con ello estoy conectando SSH por el puerto 9999 que es el que creamos con la conexión que realicé desde la oficina a mi casa. El usuario es el del equipo de la oficina y el “host”, el equipo local, que es quien redirige por la conexión entrante al puerto 9999.

&nbsp;

Y listo, ya tengo acceso al equipo de la oficina, ese que esta tan aislado detrás de los cortafuegos de la empresa.
