#!/usr/bin/python

import os, time

CONF_DIR = "/etc"

sites = ["foocoop.mx", "api.twitter.com"]

r = "no-poll\nserver=8.8.8.8\n\n"

f = open('dnsmasq.conf','w')
f.write(r)
f.close()

r += "interface=wlan0\nno-dhcp-interface=wlan0\n\n"
r += "address=/#/74.125.224.168\n"

cmd = "sudo cp dnsmasq.conf "+CONF_DIR+"/dnsmasq.conf"
os.popen(cmd).read()

cmd = "sudo /etc/init.d/dnsmasq restart"
os.spawnl(os.P_NOWAIT, cmd)

time.sleep(1)

for s in sites:
	cmd = "ping -c 1 "+s+" | grep -o \'([0-9.]\\+)\' | sed \'s/[()]//g\'"
	ip = os.popen(cmd).read()
	if ip:
		pass
		r += "address=/%s/%s"%(s,ip)

time.sleep(1)

f = open('dnsmasq.conf','w')
f.write(r)
f.close()

cmd = "sudo cp dnsmasq.conf "+CONF_DIR+"/dnsmasq.conf"
os.popen(cmd).read()

cmd = "sudo /etc/init.d/dnsmasq restart"
os.popen(cmd).read()
