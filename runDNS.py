#!/usr/bin/python

import os, time

CONF_DIR = "/etc"

sites = ["foocoop.mx", "api.twitter.com", "github.com"]

r = "no-poll\nserver=8.8.8.8\n\n"

f = open('dnsmasq.conf','w')
f.write(r)
f.close()

r += "interface=wlan0\nno-dhcp-interface=wlan0\n\n"
r += "address=/#/74.125.224.168\n"

for i in range(1,8):
	r += "address=/aeffect0%s/45.0.0.10%s\n"%(i,i)	

cmd = "sudo cp dnsmasq.conf "+CONF_DIR+"/dnsmasq.conf"
os.popen(cmd).read()

cmd = "sudo /etc/init.d/dnsmasq restart"
os.spawnl(os.P_NOWAIT, cmd)

time.sleep(3)

for s in sites:
	cmd = "ping -c 1 "+s+" | grep -o \'([0-9]\\+\\.\\([0-9]\\+\\.*\\)\\+)\' -m 1 | sed \'s/[()]//g\'"
	ip = os.popen(cmd).read()
	if ip:
		pass
		r += "address=/%s/%s"%(s,ip)

time.sleep(3)

f = open('dnsmasq.conf','w')
f.write(r)
f.close()

cmd = "sudo cp dnsmasq.conf "+CONF_DIR+"/dnsmasq.conf"
os.popen(cmd).read()

cmd = "sudo /etc/init.d/dnsmasq restart"
os.popen(cmd).read()
