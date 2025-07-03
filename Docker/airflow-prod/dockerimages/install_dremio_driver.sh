#!/usr/bin/env bash

wget -P /tmp https://download.dremio.com/odbc-driver/1.5.4.1002/dremio-odbc-1.5.4.1002-1.x86_64.rpm
ls /tmp
sleep 3
sudo apt-get install alien unixodbc-dev -y
sudo alien /tmp/dremio-odbc-1.5.4.1002-1.x86_64.rpm
sudo dpkg -i /tmp/dremio-odbc_1.5.4.1002-2_amd64.deb