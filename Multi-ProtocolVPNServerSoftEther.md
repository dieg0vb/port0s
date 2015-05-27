<h1 class="content-title" style="color: #2d2d2d;">How to Setup a Multi-Protocol VPN Server Using SoftEther</h1>
<div class="content-body tutorial-content" style="color: #000000;">
<h3 style="color: #2d2d2d;">Introduction</h3>
This article explains how to install and configure a multi-protocol VPN server using the SoftEther package. We enable and configure OpenVPN and L2TP over IPSec and SSTP VPN Servers on Linux.
<div data-unique="WhatisSoftEther"></div>
<h2 style="color: #2d2d2d;">What is SoftEther</h2>
SoftEther VPN is one of the world's most powerful and easy-to-use multi-protocol VPN software, made by the good folks at the University of Tsukuba, Japan. It runs on Windows, Linux, Mac, FreeBSD and Solaris and is freeware and open-source. You can use SoftEther for any personal or commercial use free of charge.
<div data-unique="Step1:CreateaVirtualServer"></div>
<h2 style="color: #2d2d2d;">Step 1: Create a Virtual Server</h2>
First, you need to create a DigitalOcean Droplet. As mentioned in SoftEther's website, SoftEther will work on almost every Linux distro with kernel v2.4 or above,; however it's recommended to choose one of these distributions: CentOS, Fedora, or Red Hat Enterprise Linux.

Personally I have tried it on Ubuntu, CentOS and Fedora, both 32 and 64 bit editions, and it has worked perfectly.
<div data-unique="Step2:UpdateyourServerSoftware"></div>
<h2 style="color: #2d2d2d;">Step 2: Update your Server Software</h2>
Using the command below, update and upgrade your server software packages to the latest version:

<span style="font-weight: 600;">Debian / Ubuntu:</span>
<pre><code style="color: #111111;">apt-get update &amp;&amp; apt-get upgrade
</code></pre>
<span style="font-weight: 600;">CentOS / Fedora:</span>
<pre><code style="color: #111111;">yum upgrade
</code></pre>
<div data-unique="Step3:DownloadSoftEther"></div>
<h2 style="color: #2d2d2d;">Step 3: Download SoftEther</h2>
You can download the latest SoftEther server package for Linux from their website:

<a style="color: black;" href="http://www.softether-download.com/en.aspx?product=softether">Download SoftEther</a>

Unfortunately, there is no way of getting the latest version through package managers (or even using a single url) at the moment. Therefore you have to browse their website using a desktop browser to download the package. There are a couple of ways of dealing with this: First, browse their website on your own computer and then depending on your server configuration (OS, x86/x64, etc.) find the link to the appropriate package then use <span style="font-weight: 600;">wget</span> to download the package to your server. Alternatively, you can use a terminal based web browser such as <span style="font-weight: 600;">lynx</span> to browse the SoftEther website and download the right package.
<h3 style="color: #2d2d2d;">Here's how to do it using lynx:</h3>
First install lynx on your server:

<span style="font-weight: 600;">Debian / Ubuntu:</span>
<pre><code style="color: #111111;">apt-get install lynx -y
</code></pre>
<span style="font-weight: 600;">CentOS / Fedora:</span>
<pre><code style="color: #111111;">yum install lynx -y
</code></pre>
Now using the command below browse the SoftEther download webpage:
<pre><code style="color: #111111;">lynx http://www.softether-download.com/files/softether/
</code></pre>
<img src="https://assets.digitalocean.com/articles/vpn_softether/img1.png" alt="Browsing SoftEther Files List Using Lynx" />

This page contains all versions of the SoftEther available. Choose which version you want (in this tutorial we use v2.00-9387-rtm-2013.09.16) and then press Enter to go to the link. Now choose <span style="font-weight: 600;">Linux</span> and in the next page choose <span style="font-weight: 600;">SoftEther VPN Server</span>. Depending on your server hardware architecture, choose a package; the <span style="font-weight: 600;">32bit - Intel x86</span> and <span style="font-weight: 600;">64bit - Intel x64 or AMD64</span> work for DigitalOcean 32bit or 64bit droplets. Finally download the tar file from the next page by pressing the "D" key on the link, and choose "Save to disk" when asked by Lynx. After the file is saved, we can press "Q" to quit Lynx and move on with the installation.
<div data-unique="Step4:InstallandConfigureSoftEther"></div>
<h2 style="color: #2d2d2d;">Step 4: Install and Configure SoftEther</h2>
Now we have to extract the package we received from the SoftEther download page and compile it. The package used in this tutorial is named <span style="font-weight: 600;">softether-vpnserver-v2.00-9387-rtm-2013.09.16-linux-x86-32bit.tar.gz</span> so we will extract it using the command below:
<pre><code style="color: #111111;"> tar xzvf softether-vpnserver-v2.00-9387-rtm-2013.09.16-linux-x86-32bit.tar.gz
</code></pre>
After extracting it, a directory named <span style="font-weight: 600;">vpnserver</span> will be created in the working folder. In order to compile SoftEther, the following tools and packages must be installed on your server:

<span style="font-weight: 600;">make</span>, <span style="font-weight: 600;">gccbinutils (gcc)</span>, <span style="font-weight: 600;">libc (glibc)</span>, <span style="font-weight: 600;">zlib</span>, <span style="font-weight: 600;">openssl</span>, <span style="font-weight: 600;">readline</span>, and <span style="font-weight: 600;">ncurses</span>

Make sure these are installed. You can install all the packages necessary to build SoftEther using the command below:

<span style="font-weight: 600;">Debian / Ubuntu:</span>
<pre><code style="color: #111111;">apt-get install build-essential -y
</code></pre>
<span style="font-weight: 600;">CentOS / Fedora:</span>
<pre><code style="color: #111111;">yum groupinstall "Development Tools"
</code></pre>
<span style="font-weight: 600;">Note:</span> On Fedora, I have found that the <em>gcc</em> package doesn't get installed using the command above so you have to install it manually using <span style="font-weight: 600;">yum install gcc</span>.

Now that we have all the necessary packages installed, we can compile SoftEther using the following command:

First "cd" into <span style="font-weight: 600;">vpnserver</span> directory:
<pre><code style="color: #111111;">cd vpnserver
</code></pre>
And now run "make" to compile SoftEther into an executable file:
<pre><code style="color: #111111;">make
</code></pre>
<img src="http://i.imgur.com/Uh2Gsh1.png" alt="SoftEther License Agreement" />

SoftEther will ask you to read and agree with its License Agreement. Select <span style="font-weight: 600;">1</span> to read the agreement, again to confirm read, and finally to agree to the License Agreement.

SoftEther is now compiled and made into executable files (vpnserver and vpncmd). If the process fails, check if you have all of the requirement packages installed.

Now that SoftEther is compiled we can move the <span style="font-weight: 600;">vpnserver</span> directory to someplace else, here we move it to <span style="font-weight: 600;">usr/local</span>:
<pre><code style="color: #111111;">cd ..
mv vpnserver /usr/local
cd /usr/local/vpnserver/
</code></pre>
And then change the files permission in order to protect them:
<pre><code style="color: #111111;">chmod 600 *
chmod 700 vpnserver
chmod 700 vpncmd
</code></pre>
If you like SoftEther to start as a service on startup create a file named <span style="font-weight: 600;">vpnserver</span> in<span style="font-weight: 600;">/etc/init.d</span> directory and change it to the following:

First create and open the file using <code style="color: #111111;">vi</code> or <code style="color: #111111;">nano</code>:
<pre><code style="color: #111111;">vi /etc/init.d/vpnserver
</code></pre>
And paste the following into the file:
<pre><code style="color: #111111;">#!/bin/sh
# chkconfig: 2345 99 01
# description: SoftEther VPN Server
DAEMON=/usr/local/vpnserver/vpnserver
LOCK=/var/lock/subsys/vpnserver
test -x $DAEMON || exit 0
case "$1" in
start)
$DAEMON start
touch $LOCK
;;
stop)
$DAEMON stop
rm $LOCK
;;
restart)
$DAEMON stop
sleep 3
$DAEMON start
;;
*)
echo "Usage: $0 {start|stop|restart}"
exit 1
esac
exit 0
</code></pre>
Finally save and close the file by pressing <span style="font-weight: 600;">esc</span> and typing <span style="font-weight: 600;">:wq</span> to close vim.

We have to make a directory at <span style="font-weight: 600;">/var/lock/subsys</span> if one does not exist:
<pre><code style="color: #111111;">mkdir /var/lock/subsys
</code></pre>
Now change the permission for the startup script and start <span style="font-weight: 600;">vpnserver</span> using command below:
<pre><code style="color: #111111;">chmod 755 /etc/init.d/vpnserver &amp;&amp; /etc/init.d/vpnserver start
</code></pre>
Use the command below make it to run at startup:

<span style="font-weight: 600;">Debian / Ubuntu:</span>
<pre><code style="color: #111111;">update-rc.d vpnserver defaults
</code></pre>
<span style="font-weight: 600;">CentOS / Fedora:</span>
<pre><code style="color: #111111;">chkconfig --add vpnserver 
</code></pre>
SoftEther VPN Server is now installed and configured to run at startup. Finally, we have to check if the VPN server is working:
<pre><code style="color: #111111;">cd /usr/local/vpnserver
./vpncmd
</code></pre>
Now press <span style="font-weight: 600;">3</span> to choose <span style="font-weight: 600;">Use of VPN Tools</span> and then type:
<pre><code style="color: #111111;">check
</code></pre>
If all of the checks pass, then your server is ready to be a SoftEther VPN server and you can move on to the next step. Type "exit" to exit <span style="font-weight: 600;">VPN Tools</span>.

There are two ways to configure SoftEther VPN server: you can use the Windows based server manager to manage and configure any number of SoftEther VPN servers from remotely; or use the built-in <span style="font-weight: 600;">vpncmd</span> tool to configure your servers.

You can download SoftEther Server Manager for Windows using their website and do the configuration using the GUI that it provides, which is a preferable way if you are a Windows user.

Here we use <span style="font-weight: 600;">vpncmd</span> to configure our VPN server.
<div data-unique="Step5:ChangeAdminPassword"></div>
<h2 style="color: #2d2d2d;">Step 5: Change Admin Password</h2>
Now that you have SoftEther VPN server installed, you have to assign an administrator password in order to use with SoftEther. You can do this using <span style="font-weight: 600;">vpncmd</span> which is SoftEther's command line based administration tool:
<pre><code style="color: #111111;">./vpncmd
</code></pre>
Press <span style="font-weight: 600;">1</span> to select "Management of VPN Server or VPN Bridge", then press Enter without typing anything to connect to the localhost server, and again press Enter without inputting anything to connect to server by server admin mode.

Then use command below to change admin password:
<pre><code style="color: #111111;">ServerPasswordSet
</code></pre>
<div data-unique="Step6:CreateAVirtualHub"></div>
<h2 style="color: #2d2d2d;">Step 6: Create A Virtual Hub</h2>
To use SoftEther we must first create a Virtual Hub. Here as an example we create a hub named <span style="font-weight: 600;">VPN</span>, in order to do that enter command below in the <span style="font-weight: 600;">vpncmd</span> tool:
<pre><code style="color: #111111;">HubCreate VPN
</code></pre>
Next you will be asked to enter an administrator password for the hub. This password will be used whenever you are not logged in as <span style="font-weight: 600;">server admin</span> mode, and you want to manage that specific hub.

Now select the Virtual Hub you created using this command:
<pre><code style="color: #111111;">Hub VPN
</code></pre>
<div data-unique="Step7:EnableSecureNAT"></div>
<h2 style="color: #2d2d2d;">Step 7: Enable SecureNAT</h2>
There are two ways of connecting your hubs to the server network: using a Local Bridge connection or using the SecureNAT function.

You can use each one separately, but using these two together will cause problems.

Here we use SecureNAT, which is very easy to setup and works pretty well in most situations. You could also use Local Bridge, but then you have to install and configure a DHCP Server too.

SecureNAT is a combination of Virtual NAT and DHCP Server function. You can enable SecureNAT using the command below:
<pre><code style="color: #111111;">SecureNatEnable
</code></pre>
<div data-unique="Step8:CreateandManageUsers"></div>
<h2 style="color: #2d2d2d;">Step 8: Create and Manage Users</h2>
Now we have to create users for our Virtual Hub to use the VPN. We can create users for our Virtual Hub using the command <span style="font-weight: 600;">UserCreate</span> and view the list of current users by <span style="font-weight: 600;">UserList</span>. Users can be added to groups and can even have different types of authentication modes (including: Password, Certificate, RADIUS, NTLM, etc.).

By using command <span style="font-weight: 600;">UserCreate</span> we create a user named "test":
<pre><code style="color: #111111;">UserCreate test
</code></pre>
The default type of authentication is Password but we can change it to a different type using commands below:

<code style="color: #111111;">UserNTLMSet</code> for NT Domain Authentication

<code style="color: #111111;">UserPasswordSet</code> for Password Authentication

<code style="color: #111111;">UserAnonymousSet</code> for Anonymous Authentication

<code style="color: #111111;">UserRadiusSet</code> for RADIUS Authentication

<code style="color: #111111;">UserCertSet</code> for Individual Certificate Authentication

<code style="color: #111111;">UserSignedSet</code> for Signed Certificate Authentication

In this tutorial we use Password as the user authentication mode for our <span style="font-weight: 600;">test</span> user, so using this command set a password for user <span style="font-weight: 600;">test</span>:
<pre><code style="color: #111111;">UserPasswordSet test
</code></pre>
<div data-unique="Step9:SetupL2TP/IPSec"></div>
<h2 style="color: #2d2d2d;">Step 9: Setup L2TP/IPSec</h2>
To enable L2TP/IPsec VPN server you can use the command below:
<pre><code style="color: #111111;">IPsecEnable
</code></pre>
After entering this command, you will be asked to configure the L2TP server functions:

<span style="font-weight: 600;">Enable L2TP over IPsec Server Function</span>: Choose <span style="font-weight: 600;">yes</span> to enable L2TP VPN over IPSec with pre-shared key encryption. Now you can make VPN connections to this server using iPhone, Android, Windows, and Mac OS X devices.

<span style="font-weight: 600;">Enable Raw L2TP Server Function</span>: This will enable L2TP VPN for clients with no IPSec encryption.

<span style="font-weight: 600;">Enable EtherIP / L2TPv3 over IPsec Server Function</span>: Routers which are compatible with EtherIP / L2TPv3 over IPsec can connect to this server by enabling this function.

<span style="font-weight: 600;">Pre Shared Key for IPsec</span>: Enter a pre-shared key to use with L2TP VPN.

<span style="font-weight: 600;">Default Virtual HUB in a case of omitting the HUB on the Username</span>: Users must specify the Virtual Hub they are trying to connect to by using <span style="font-weight: 600;">Username@TargetHubName</span> as their username when connecting. This option specifies which Virtual Hub to be used if the user does not provide such information. In our case enter <span style="font-weight: 600;">VPN</span>.
<div data-unique="Step10:SetupSSTP/OpenVPN"></div>
<h2 style="color: #2d2d2d;">Step 10: Setup SSTP/OpenVPN</h2>
The SoftEther can clone the functions of Microsoft SSTP VPN Server and OpenVPN Server. But before we enable these we have to generate a self-signed SSL certificate for our server. You can use openssl or SoftEther's own command to generate a SSL certificate.

Here we use SoftEther's <span style="font-weight: 600;">ServerCertRegenerate</span> command to generate and register a self-signed SSL certificate for our server. The argument passed to command is CN (Common Name), and must be set to your host name (FQDN) or IP address:
<pre><code style="color: #111111;">ServerCertRegenerate [CN]
</code></pre>
<span style="font-weight: 600;">Note 1:</span> SoftEther also comes with a built-in <span style="font-weight: 600;">Dynamic DNS</span> function, which can assign a unique and permanent hostname for your server. You can use the hostname assigned by this function for creating a SSL Certificate and connecting to your server.

<span style="font-weight: 600;">Note 2:</span> If you already have a SSL certificate or you have created one using <span style="font-weight: 600;">openssl</span>, it can be added to the server using the command <code style="color: #111111;">ServerCertSet</code>.

Now that we have created the certificate, we have to download the certificate to our clients and add them as trusted. Using the command below, we save the server certificate into a file named <span style="font-weight: 600;">cert.cer</span>:
<pre><code style="color: #111111;">ServerCertGet ~/cert.cer
</code></pre>
Now you can download the certificate to your client using FileZilla or any other SFTP Client.

To make the certificate trusted in Windows, you have to install it in the <span style="font-weight: 600;">Trusted Root Certification Authorities</span> store. Here's an article explaining how (read the <span style="font-weight: 600;">To install a certificate chain</span> part):

<a style="color: black;" href="http://technet.microsoft.com/en-us/library/dd441378(office.13).aspx">Installing a Certificate Chain</a>

Now that we have created and registered a SSL Certificate for our server, we can enable SSTP function with this command:
<pre><code style="color: #111111;">SstpEnable yes
</code></pre>
And to enable OpenVPN:
<pre><code style="color: #111111;">OpenVpnEnable yes /PORTS:1194
</code></pre>
<span style="font-weight: 600;">Note:</span> OpenVPN's default port is 1194, but you can change it to any port you want by changing the <span style="font-weight: 600;">/PORTS:1194</span> part of the command above to your desired port or ports (yes it supports multiple ports).

After you enabled OpenVPN, you can download a sample configuration file for OpenVPN client. Here we create a sample OpenVPN configuration file and save it to<span style="font-weight: 600;">my<em>openvpn</em>config.zip</span>:
<pre><code style="color: #111111;">OpenVpnMakeConfig ~/my_openvpn_config.zip
</code></pre>
Then you can download it using any SFTP client such as FileZilla and apply it to your OpenVPN clients.

SoftEther also provides a dedicated VPN Client software for both Windows and Linux. It supports a SoftEther specific protocol called <span style="font-weight: 600;">Ethernet over HTTPS</span> or <span style="font-weight: 600;">SSL-VPN</span> which is very powerful. It uses HTTPS protocol and port 443 in order to establish a VPN tunnel, and because this port is well-known, almost all firewalls, proxy servers and NATs can pass the packet. In order to use SSL-VPN protocol, you must download and install SoftEther VPN Client, which can be obtained from their website.
<div data-unique="Step11:ConnectingtoSoftEtherVPNServer(ClientConfiguration)"></div>
<h2 style="color: #2d2d2d;">Step 11: Connecting to SoftEther VPN Server (Client Configuration)</h2>
Since SoftEther is a multi-protocol VPN server, there are many ways to connect to it as a client. You can choose any protocol to establish a secure connection to your server, including L2TP, SSTP, OpenVPN and an exclusive to SoftEther protocol named SSL-VPN.

Depending on the client operating system and configurations, you could use any of the mentioned protocols. However, I prefer to use SSL-VPN since it's both secure and fast, and also as mentioned before since it uses a common and well-known port (443 or https-port), it can penetrate most of the firewalls.

Here we use SoftEther's own VPN client software to connect to our server:

First download the SoftEther VPN Client for Linux from SoftEther's website. We can download it using a <span style="font-weight: 600;">lynx</span> browser. Enter this command to open SoftEther's download page:
<pre><code style="color: #111111;">lynx http://www.softether-download.com/files/softether/
</code></pre>
Then just as you did when downloading the Server software, select the latest version (Here we used <span style="font-weight: 600;">v2.00-9387-rtm-2013.09.16</span>). Now choose <span style="font-weight: 600;">Linux</span> and in the next page choose<span style="font-weight: 600;">SoftEther VPN Client</span>. Now depending on your system's hardware architecture, choose a package (The <span style="font-weight: 600;">32bit - Intel x86</span> and <span style="font-weight: 600;">64bit - Intel x64 or AMD64</span> works for DigitalOcean 32bit or 64bit droplets). Finally download the tar file from the next page by pressing the "D" key on the link, and choose <span style="font-weight: 600;">Save to disk</span> when asked by Lynx. After the file is saved, press "Q" to quit Lynx.

Extract the tar file you just downloaded using this command:
<pre><code style="color: #111111;">tar xzvf softether-vpnclient-v2.00-9387-rtm-2013.09.16-linux-x86-32bit.tar.gz
</code></pre>
<span style="font-weight: 600;">Note:</span> Change <code style="color: #111111;">softether-vpnclient-v2.00-9387-rtm-2013.09.16-linux-x86-32bit.tar.gz</code> to your downloaded file's name.

Now just as we did with the server, we have to compile and make vpnclient an executable file by running these commands (make sure you have the development tools mentioned in <span style="font-weight: 600;">Step 4</span> installed on client):
<pre><code style="color: #111111;">cd vpnclient
make
</code></pre>
Enter <span style="font-weight: 600;">1</span> three times when asked to read and accept the License Agreement, and then move the files to another directory and change permissions:
<pre><code style="color: #111111;">cd ..
mv vpnclient /usr/local
cd /usr/local/vpnclient/
chmod 600 *
chmod 700 vpnclient
chmod 700 vpncmd
</code></pre>
Then start the VPN client service using this command:
<pre><code style="color: #111111;">./vpnclient start
</code></pre>
To configure our client, we're going to use <code style="color: #111111;">vpncmd</code>. While you're in the <span style="font-weight: 600;">vpnclient</span> directory enter this command to run <code style="color: #111111;">vpncmd</code> tool:
<pre><code style="color: #111111;">./vpncmd
</code></pre>
Choose <span style="font-weight: 600;">2</span> to enter <span style="font-weight: 600;">Management of VPN Client</span> mode, and then press enter to connect to and manage the local VPN client you just installed.

SoftEther uses Virtual Adapters to establish a connection to our VPN server, using this command create a Virtual Adapter named <span style="font-weight: 600;">myadapter</span>:
<pre><code style="color: #111111;">NicCreate myadapter
</code></pre>
Now using this command, create a new VPN connection named <span style="font-weight: 600;">myconnection</span>:
<pre><code style="color: #111111;">AccountCreate myconnection
</code></pre>
Then enter your SoftEther VPN server's IP and Port number. The port number could be any port that you have set as listening on your server. By default, SoftEther listens on these four ports: 443, 992, 1194, 5555. Here as an example where we use port 443:
<pre><code style="color: #111111;">Destination VPN Server Host Name and Port Number: [VPN Server IP Address]:443
</code></pre>
<span style="font-weight: 600;">Note:</span> Instead of an IP Address, you could also enter you server's fully qualified domain name (FQDN).

Now enter the name of the Virtual Hub you're trying to connect to on your server. In our case it is named <span style="font-weight: 600;">VPN</span>:
<pre><code style="color: #111111;">Destination Virtual Hub Name: VPN
</code></pre>
Then enter the username of a user you created in your server. We created a user called <span style="font-weight: 600;">test</span>:
<pre><code style="color: #111111;">Connecting User Name: test
</code></pre>
And finally enter the name of the Virtual Hub you just created:
<pre><code style="color: #111111;">Used Virtual Network Adapter Name: myadapter
</code></pre>
Now our VPN connection has been created and it's ready to be connected. One last step is to change the Authentication mode to <span style="font-weight: 600;">Password</span> since that's how we configured our user's authentication mode in the server:
<pre><code style="color: #111111;">AccountPasswordSet myconnection
</code></pre>
When asked for, enter <span style="font-weight: 600;">standard</span> as password authentication method:
<pre><code style="color: #111111;">Specify standard or radius: standard
</code></pre>
Finally we can connect our connection-- use this command to do that:
<pre><code style="color: #111111;">AccountConnect myconnection
</code></pre>
You can see the connection status using this command:
<pre><code style="color: #111111;">AccountStatusGet myconnection
</code></pre>
<span style="font-weight: 600;">Note:</span> In order to make your connection to the server more secure and prevent man-in-the-middle attacks, it's best to use a SSL certificate to identify your server. This can be done easily using SoftEther. To do that, first you must download the cert file to your client as explained in <span style="font-weight: 600;">Step 10</span> and then using <span style="font-weight: 600;">CertAdd</span> add it to your client's trusted certificates. Then, using command <code style="color: #111111;">AccountServerCertEnable</code> enable certificate verification for your VPN connection.
<div data-unique="FinishingUp"></div>
<h2 style="color: #2d2d2d;">Finishing Up</h2>
In this article, we went through the process of setting up a SoftEther VPN Server using<span style="font-weight: 600;">vpncmd</span> which is a command line administration utility provided by SoftEther. All the things done here could also be done using <span style="font-weight: 600;">SoftEther Server Manager for Windows</span>, and it's even easier to setup a SoftEther VPN Server using that tool. So I recommended you to use it if you have a Windows machine.

That's it. We have successfully installed and configured a multi-protocol VPN server using SoftEther. Now clients can connect to our server using L2TP, IPSec, SSTP, OpenVPN, etc.

</div>
