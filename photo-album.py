import os
import cv2

path="Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in [".gif", ".jpg", ".jpeg", ".JPG"]:
        file_name = path + "/" + file

        print(file_name)
        images.append(file_name)

frame = cv2.imread(images[0])       

height,width,channels = frame.shape
size= (width, height)

out = cv2.VideoWriter("photo-album.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

for i in range(0, 3):
    frame=cv2.imread(images[i])
    out.write(frame)

out.release()       