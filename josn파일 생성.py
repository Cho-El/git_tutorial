import json
from collections import OrderedDict

file_data = OrderedDict()

file_data["name"] = "Computer"
file_data["language"] = "kor"

print(json.dumps(file_data, ensure_ascii= False, indent="\t"))

with open('words.json', 'w', encoding = "utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii = False, indent = "\t")