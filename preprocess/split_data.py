import csv
import os
import random
import shutil

train_dir = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/PreProcessV3/train"
test_dir = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/PreProcessV3/test"

for root, dirs, files in os.walk(train_dir):
    print(root)
    if root == train_dir:
        continue
    num = os.path.basename(os.path.normpath(root))
    all_files = []

    label = int(num)

    for file in files:
        if file.endswith(".jpg"):
            all_files.append(file)
    random.shuffle(all_files)
    ratio = int(round(0.1 * len(all_files)))
    test = all_files[:ratio]
    # root_path = f"{root}/{num}"
    for image in test:
        src = os.path.join(root, image)
        # print(src)
        dst = f"{test_dir}/{num}/{image}"
        shutil.copy(src, dst)
        os.remove(src)
