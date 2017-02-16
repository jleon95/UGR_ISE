#!/bin/bash/
sudo sed -i s/"PasswordAuthentication no"/"PasswordAuthentication yes"/
/etc/ssh/sshd_config
sudo service ssh restart
echo "Password access enabled."
sleep 10
sudo sed -i s/"PasswordAuthentication yes"/"PasswordAuthentication no"/
/etc/ssh/sshd_config
sudo service ssh restart
echo "Password access disabled." 
