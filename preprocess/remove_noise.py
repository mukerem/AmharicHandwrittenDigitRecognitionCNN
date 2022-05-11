import os
import json
baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/PreProcessV1/"

f = open("major_noise.json", "r")
major = json.load(f)
f.close()

for num in major:
    for image in major[num]:
        path = f"{baseDIR}{num}/{image}.jpg"
        try:
            os.remove(path)
        except:
            print(path)
        pass

f = open("minor_noise.json", "r")
minor = json.load(f)
f.close()

for num in minor:
    for image in minor[num]:
        path = f"{baseDIR}{num}/{image}.jpg"
        try:
            os.remove(path)
        except:
            print(path)
        pass