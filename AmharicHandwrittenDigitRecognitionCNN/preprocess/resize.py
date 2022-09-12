import cv2
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
baseDIR = "/home/andalus/Documents/MSc/Thesis/Hand written/Dataset"
path = f"{baseDIR}/Digits/1/11_5.jpg"

im = cv2.imread(path)
crop_img = im[:-10, 10:]
# crop_img = im[:, :]
# cv2.imshow("input", crop_img)
imS = cv2.resize(crop_img, (32, 32))
imagem = cv2.bitwise_not(imS)
cv2.imwrite("inverse.jpg", imagem)
# cv2.imshow("output", imagem)
# cv2.waitKey(0) 