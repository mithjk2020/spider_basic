#!/bin/bash

#to list network interfaces
ifconfig -a
ip addr show

#use "ip route | grep default" to get default gateway

#assigning static ip address
sudo ip addr add 192.162.0.105/24 dev wlp0s20f3
sudo ip route add default via 192.168.0.1 dev wlp0s20f3

#for configuration, open /etc/resolv.conf and modify these lines:
nameserver 8.8.8.8
nameserver 8.8.4.4

#to avoid conflict, ping the new ip address to check for any output
#check now using ipconfig and ping default gateway

#ping remote server
ping www.google.com

#once you press ctrl C to stop display, the last line will show the minimum, >

#traceroute
traceroute www.google.com
