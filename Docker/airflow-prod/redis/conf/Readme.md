Redis configuration file is location @ /etc/redis/redis.conf
=============================================================

Install redis locally or through a docker container
    sudo apt install redis-server

Install redis CLI
------------------
     sudo apt install redis-cli 
     sudo apt install redis-tools

Check redis status
------------------
   systemctl status redis-server

Set redis password 
------------------

  redis config requirepass password
  config get requirepass
