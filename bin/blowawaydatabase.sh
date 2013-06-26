#!/bin/sh

function drop_create_db() {
  ##get database name!
  dbname=`cat /etc/django/multi/settings.ini | grep "^DATABASE_NAME:" | awk '{print $2}'`
  if [ ! -z $dbname ]; then
    echo "Dropping database: $dbname"
    dropdb $dbname
    createdb $dbname
    ##user permissions should still be ok??
  else
    echo "Couldn't find DATABASE_NAME in /etc/django/multi/settings.ini...."
  fi
}

echo "Warning, about to drop/create database on localhost!"
while true; do
    read -p "Shall I continue?" yn
    case $yn in
        [Yy]* )drop_create_db; break;;
	[Nn]* )exit;;
	* ) echo "Enter (Y)es or (N)o.";;
    esac
done
