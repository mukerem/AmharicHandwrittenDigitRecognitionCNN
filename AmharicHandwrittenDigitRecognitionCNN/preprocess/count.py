import os
from collections import OrderedDict

baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset"
all_files = {}
for root, dirs, files in os.walk(f"{baseDIR}/PreProcessV1/"):
    num = os.path.basename(os.path.normpath(root))

    if num == "PreProcessV1":
        continue
    all_files[num] = len(files)

all_files = OrderedDict(sorted(all_files.items(), key=lambda t: int(t[0])))
all = sum([all_files[i] for i in all_files])
all_files["total"]  = all

f = open("count.json", 'w')
import json
f.write(json.dumps(all_files, indent=4))
f.close()
