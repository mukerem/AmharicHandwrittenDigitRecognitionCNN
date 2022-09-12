import os
sure = input("Are you sure? Enter Y/y")
if not sure.lower() == "y":
    exit(0)
baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/Digits/"

fnames = list(range(1, 11))+list(range(20, 101, 10))+ [1000]

START = 100
END = 100

LEVEL = [1,2,3,4,5]
START = 1
END = 464
IMAGE_LIST = range(START, END+1)
# IMAGE_LIST = [1,101,201,301,401]

for num in fnames:
    for COUNTER in IMAGE_LIST:
        for level in LEVEL:
            path = f"{baseDIR}{num}/{COUNTER}_{level}.jpg"
            try:
                os.remove(path)
            except:
                print(path)
                pass

