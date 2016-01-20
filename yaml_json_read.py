import yaml
import json
from pprint import pprint as pp

#Read YAML file
with open("class1_yaml.yml") as f:
    yaml_list = yaml.load(f)

print "Here is the list in YAML format: %s" % (pp(yaml_list))

#Read a json file
with open("class1_json.json") as f:
    json_list = json.load(f)


print "Here is the list in JSON format: %s" % (pp(json_list))


