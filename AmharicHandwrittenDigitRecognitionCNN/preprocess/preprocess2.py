import cv2
import os

saveBaseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/PreProcessDatasetWithOriginalSize"
def resize_crop_inverse(path, num, file):
    im = cv2.imread(path)
    crop_img = im[:-10, 10:]

    imagem = cv2.bitwise_not(crop_img)

    dir = f"{saveBaseDIR}/{num}"
    if not os.path.isdir(dir):
        os.mkdir(dir)
    new_path = os.path.join(dir, file)
    cv2.imwrite(new_path, imagem)
 

baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset"
root_path = '/home/andalus/Documents/MSc/Thesis/Hand written/Dataset/Digits/'
all_files = []
for root, dirs, files in os.walk(f"{baseDIR}/Digits/"):
    if root == root_path:
        continue
    num = os.path.basename(os.path.normpath(root))

    for file in files:
        if file.endswith(".jpg"):
            path = os.path.join(root, file)
            resize_crop_inverse(path, num, file)
