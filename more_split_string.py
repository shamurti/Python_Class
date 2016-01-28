
cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"
cisco_ios_list = cisco_ios.split(",")

ios_version = cisco_ios_list[2]
ios = ios_version.strip("Version")
print "ios_vesion= %s" % (ios)

