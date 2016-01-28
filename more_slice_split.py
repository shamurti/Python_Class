#!/usr/bin/env python

#show ip bgp entries:
entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24       157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24     157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"


print "Results of the 'show ip bgp' are: "
print "%-20s %-50s" % ("ip_prefix", "as_path")

e1_list1 = entry1.split() 
ip_prefix = e1_list1[1]
as_path = e1_list1[4:-1]
print "%-20s %-50s" % (ip_prefix,as_path)

e2_list2 = entry2.split() 
ip_prefix = e2_list2[1]
as_path = e2_list2[4:-1]
print "%-20s %-50s" % (ip_prefix,as_path)



e3_list3 = entry3.split() 
ip_prefix = e3_list3[1]
as_path = e3_list3[4:-1]
print "%-20s %-50s" % (ip_prefix,as_path)



e4_list4 = entry4.split() 
ip_prefix = e4_list4[1]
as_path = e4_list4[4:-1]
print "%-20s %-50s" % (ip_prefix,as_path)





