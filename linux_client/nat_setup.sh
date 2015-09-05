#!/bin/bash

# set up NAT to route traffic through radio
echo 1 > /proc/sys/net/ipv4/ip_forward
/sbin/iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
/sbin/iptables -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
/sbin/iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

# set up dnsmasq
mv dnsmasq-merki.conf /etc/dnsmasq.d/98-merki.conf
