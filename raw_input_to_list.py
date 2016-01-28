#!/usr/bin/env python

input = raw_input("Enter an IP Network: ")
ip_list = input.split(".")
if len(ip_list)==3:
	ip_list.append('0')
elif len(ip_list)==4:
	ip_list[3]='0'

print ip_list

