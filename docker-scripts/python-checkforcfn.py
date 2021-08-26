import sys
import json
import yaml
import os

if os.stat(sys.argv[1]).st_size < 5:
	print("Empty file: {}".format(sys.argv[1]))
	sys.exit(1)
	      
with open(sys.argv[1], "r") as file:
	filename, file_extension = os.path.splitext(sys.argv[1])
	if file_extension.lower() == ".yaml" or file_extension == ".yml":
		data = yaml.load(file, Loader=yaml.BaseLoader)
	else:
		data = json.load(file)
	if ("AWSTemplateFormatVersion" in data or "Resources" in data):
		# If we have CFM template fields, sucessfully exit.
		sys.exit(0)
	else:
		# If we don't have CFM template fields, generic error exit. 
		sys.exit(1)
