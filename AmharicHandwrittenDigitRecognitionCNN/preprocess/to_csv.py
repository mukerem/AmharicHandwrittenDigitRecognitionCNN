import csv
import os
import random
import shutil

baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset"
dir = f"{baseDIR}/Crop/"
path = f"{dir}/digits.csv"
root_path = '/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/Digits/'
all_files = []
for root, dirs, files in os.walk(f"{baseDIR}/Digits/"):
    print(root)
    if root == root_path:
        continue
    num = os.path.basename(os.path.normpath(root))

    label = int(num)
    for file in files:
        if file.endswith(".jpg"):
            image = f"ID_num_{num}_{file}"
            all_files.append((image, label))
            src = os.path.join(root, file)
            dst = f"{baseDIR}/AllDigits/"
            shutil.copy(src, dst)
            old_name = f"{dst}/{file}"
            new_name = f"{dst}/{image}"
            os.rename(old_name, new_name)

random.shuffle(all_files)
with open(path, 'w') as f:
    # create the csv writer
    writer = csv.writer(f)
    header = ['Image_ID', 'Target']
    writer.writerow(header)
    for data in all_files:
    # write a row to the csv file
        writer.writerow(data)