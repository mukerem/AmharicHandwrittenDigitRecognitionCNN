import cv2
import os

saveBaseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/PreProcessDataset"
def resize_crop_inverse(path, num, file):
    im = cv2.imread(path)
    crop_img = im[:-10, 10:]

    imS = cv2.resize(crop_img, (32, 32))
    imagem = cv2.bitwise_not(imS)

    dir = f"{saveBaseDIR}/{num}"
    if not os.path.isdir(dir):
        os.mkdir(dir)
    new_path = os.path.join(dir, file)
    # print(new_path)
    cv2.imwrite(new_path, imagem)
 

baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset"
dir = f"{baseDIR}/Crop/"
path = f"{dir}/digits.csv"
root_path = '/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/Digits/'
all_files = []
include = ["112", "273", "274", "275"]
for root, dirs, files in os.walk(f"{baseDIR}/Digits/"):
    if root == root_path:
        continue
    num = os.path.basename(os.path.normpath(root))

    for file in files:
        if not file[:3] in include:
            continue
        if file.endswith(".jpg"):
            path = os.path.join(root, file)
            resize_crop_inverse(path, num, file)
