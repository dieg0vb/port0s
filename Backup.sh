#!/bin/bash
#
# -*- ENCODING: UTF-8 -*-
#
# Copyleft 2015
#
: ${DESTINY:=$HOME/WORKING}
: ${BACKUPFOLDER:=`date +'%Y-%m-%d'`}
: ${RARPASSWORD:=el-que-quieras}
: ${SQLPASSWORD:=el-que-quieras}
 
# Creando carpeta de backup.
cd $DESTINY
mkdir $BACKUPFOLDER
 
# Copiando configuración de Rainlendar2.
mkdir $DESTINY/$BACKUPFOLDER/.config
cp -Rv $HOME/.config/.rainlendar2/ $DESTINY/$BACKUPFOLDER/.config/
 
# Copiando configuración de Firefox.
cp -Rv $HOME/.mozilla/ $DESTINY/$BACKUPFOLDER
 
# Copiando configuración de Opera.
cp -Rv $HOME/.opera/ $DESTINY/$BACKUPFOLDER
 
# Copiando configuración de Chromium.
cp -Rv $HOME/.config/chromium/ $DESTINY/$BACKUPFOLDER/.config/
 
# Copiando configuración y logs de Pidgin.
mkdir $DESTINY/$BACKUPFOLDER/.purple
cp -Rv $HOME/.purple/logs/ $DESTINY/$BACKUPFOLDER/.purple/
 
# Copiando logs de Konversation.
cp -Rv $HOME/.konversation/ $DESTINY/$BACKUPFOLDER
 
# Copiando logs de Kopete.
mkdir -p $DESTINY/$BACKUPFOLDER/.kde/share/apps/kopete/
cp -Rv $HOME/.kde/share/apps/kopete/logs/ $DESTINY/$BACKUPFOLDER/.kde/share/apps/kopete/
 
# Copiando passwords de KWallet.
cp -Rv $HOME/.kde/share/apps/kwallet/ $DESTINY/$BACKUPFOLDER/.kde/share/apps/
 
# Copiando configuración+emails+contactos de KMail.
mkdir -p $DESTINY/$BACKUPFOLDER/.local/share/
cp -Rv $HOME/.local/share/contacts/ $DESTINY/$BACKUPFOLDER/.local/share/
mkdir -p $DESTINY/$BACKUPFOLDER/.kde/share/apps/kmail/mail/
cp -Rv $HOME/.kde/share/apps/kmail/mail/ $DESTINY/$BACKUPFOLDER/.kde/share/apps/kmail/
 
# Exportando alguna base de datos que tengamos.
mysqldump --opt --host=localhost --user=root --password=$SQLPASSWORD dbtest > "$DESTINY/$BACKUPFOLDER/dbtest.sql"
mysqldump --opt --host=localhost --user=root --password=$SQLPASSWORD bnc > "$DESTINY/$BACKUPFOLDER/bnc.sql"
 
# Eliminando el caché de Firefox y Opera que copiamos, pues no lo queremos salvar ya que no es importante.
rm -Rv $DESTINY/$BACKUPFOLDER/.mozilla/firefox/*/Cache
rm -Rv $DESTINY/$BACKUPFOLDER/.opera/cache
 
# Comprimiendo en .RAR todo lo que copiamos antes, con password.
rar a $BACKUPFOLDER.rar -hp$RARPASSWORD $DESTINY/$BACKUPFOLDER
 
# Comprimiendo en .TAR.GZ todo lo que copiamos antes.
#tar czvf $BACKUPFOLDER.tar.gz $BACKUPFOLDER/
 
exit 0
