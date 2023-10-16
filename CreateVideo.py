import os, cv2

path = "Images"

images = []

#print(os.listdir(path))

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = f"{path}/{file}"
        print(file_name)

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
width, height, channel = frame.shape
size = (width, height)

print(size)

# cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
    
for i in range(0, count-1):
    img = cv2.imread(images[i])
    out.write(img)

out.release()

print("Done")