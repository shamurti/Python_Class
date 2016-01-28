
#!/usr/bin/env python
'''
	This program will take a /24 IP Network input and print the list regardless of entry
	forms: 10.2.2. or 10.2.3 or 10.2.3.0
''' 
#Request IP Network input
a = raw_input("Enter an IP Network: ")

# Create list
octets = a.split(".")

#Make 3 octets
octets = octets[:3]

#Append 4th 0 Octet
octets.append('0')

#print result
print "Octets of the IP Network entered are: %s" % (octets)

#Join octets and create IP Network format 
ip_netw = ".".join(octets)

print "%20s %20s %20s" % ('NETWORK_NUMBER','FIRST_OCTET_BINARY','FIRST_OCTET_HEX') 

#Use conversion from hex to\from bin
first_bin = bin(int(octets[0]))
first_hex = hex(int(octets[0]))

print "%20s %20s %20s" % (ip_netw,first_bin,first_hex)





