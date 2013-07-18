#!/usr/bin/python

import os, time

CONF_DIR = "/opt/local/etc"

sites = ["foocoop.mx", "api.twitter.com", "twitter.com"]
r = "no-poll\nserver=8.8.8.8\n\n#interface=en1\n#no-dhcp-interface=en1\n\n"

f = open('dnsmasq.conf','w')
f.write(r)
f.close()

cmd = "sudo cp dnsmasq.conf "+CONF_DIR+"/dnsmasq.conf"
os.popen(cmd).read()

cmd = "sudo dnsmasq -k "
os.spawnl(os.P_NOWAIT, cmd)

time.sleep(1)

for s in sites:
	cmd = "ping -c 1 "+s+" | grep -o \'([0-9.]\\+)\' | sed \'s/[()]//g\'"
	ip = os.popen(cmd).read()
	if ip:
		pass
		r += "address=/%s/%s"%(s,ip)

time.sleep(1)
cmd = "sudo killall dnsmasq"

f = open('dnsmasq.conf','w')
f.write(r)
f.close()

cmd = "sudo cp dnsmasq.conf "+CONF_DIR+"/dnsmasq.conf"
os.popen(cmd).read()

cmd = "sudo dnsmasq"
os.popen(cmd).read()
