#!/usr/bin/env python

ip = raw_input("\nEnter an IP address in dotted decimal format:  ")

octets = ip.split(".")

print "\nThe octets of the IP address: %s in binary are: \n" % (ip)

print "%20s %20s %20s %20s" % ('first_octet','second_octet','third_octet','fourth_octet')
print "%20s %20s %20s %20s" % (bin(int(octets[0])),bin(int(octets[1])),bin(int(octets[2])),bin(int(octets[3])))


