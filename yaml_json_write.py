import yaml
import json
import os.path


# Add dictionary to the list
yj_dict = {
    'ip_addr' : '10.1.1.1',
    'router' : 'rtr-1',
    'attribs' : range(4)
}

yj_list = [
    range(10),
    yj_dict,
    'This is Radio Clash',
    'Spaceman',
    '54'
]


#Print the number of elements in the list
print "Number of elements in the list are: %s" % (len(yj_list))

 
#Write the list to a file with yaml format

if os.path.exists("/home/nzamanzadeh/Python_Class/class1_yaml.yml"):
    print "YAML file already exists"
    
else:
    with open("class1_yaml.yml", "w") as f:
        f.write(yaml.dump(yj_list, default_flow_style=False))
    print "class1_yaml file contents are: %s" % (yaml.dump(yj_list, default_flow_style=False))

#write the list to a file with json format
if os.path.exists("/home/nzamanzadeh/Python_Class/class1_json.json"):
    print "JSON file already exists"

else:
    with open("class1_json.json", "w") as f:
        json.dump(yj_list, f)

