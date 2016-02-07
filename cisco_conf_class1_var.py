#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_conf_example.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

pfs_grp2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

not_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES-SHA")

print "Here are all the crypto maps configured:"
for i in crypto_map:
    print i.text
    for child in i.children:
        print child.text

print "*******"
print "\ncrypto maps with PFS group2 are:"
for entry in pfs_grp2:
		print entry.text
		for child in entry.children:
			print " {0}".format(child.text)

print "*******"
print "\ncrypto maps not using AES:"
for i in not_aes:
    print i.text
    for child in i.children:
        print " {0}".format(child.text)





