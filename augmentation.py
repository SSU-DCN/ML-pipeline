import time
import os
from PIL import Image
import sys

print("Process Start.")

start_time = time.time()

###### 증강할 데이터셋 위치 ######
path = "/root/nfs-storage/before/before-augmentation/"
##################################

file_lst = os.listdir(path)
print(file_lst)

for file in file_lst:
    filepath = path + '/' + file
    print(file)

    path2 = path + file
    file_lst2 = os.listdir(path2)
    COUNT = 1
    for file2 in file_lst2:
        filepath2 = path2 + '/' + file2
        image_filename = filepath2

        ##### 결과 저장 폴더 위치#####
        out_dir ="/root/nfs-storage/before/storage/augmented-data/"
        ##############################

        ##### 이미지 한장 당 증강할 수 #####
        limit_per_one = 50
        ####################################


        out_dir2 = out_dir + file
        if file not in os.listdir(out_dir):
            os.mkdir(out_dir2)

        image = Image.open(image_filename)
        Xdim, Ydim = image.size

        temp_new_file_name = "%05d.png" %COUNT
        COUNT += 1

        image.save(out_dir2 + "/" + temp_new_file_name)
        image.close()

        FILELIST = [temp_new_file_name]

        for i in range(len(FILELIST)):
            image = Image.open(out_dir2 + "/" + FILELIST[i])
            new_temp_name = "%05d.png" %COUNT
            COUNT += 1
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
            image.save(out_dir2 + "/" + new_temp_name)
            image.close()
            FILELIST.append(new_temp_name)

        for i in range(len(FILELIST)):
            image = Image.open(out_dir2 + "/" + FILELIST[i])
            new_temp_name = "%05d.png" % COUNT
            COUNT += 1
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image.save(out_dir2 + "/" + new_temp_name)
            image.close()
            FILELIST.append(new_temp_name)

        for i in range(len(FILELIST)):
            image = Image.open(out_dir2 + "/" + FILELIST[i])
            new_temp_name = "%05d.png" % COUNT
            COUNT += 1
            image = image.convert('1')
            image.save(out_dir2 + "/" + new_temp_name)
            image.close()
            FILELIST.append(new_temp_name)

        COUNT2 = 1


        for el in FILELIST:
            for i in range(180):
                if COUNT2 > limit_per_one - 8:
                    break
                image = Image.open(out_dir2 + "/" + el)
                new_temp_name = "%05d.png" % COUNT
                COUNT2 += 1
                COUNT += 1
                image = image.rotate(i+1)
                image = image.resize((Xdim, Ydim))
                image.save(out_dir2 + "/" + new_temp_name)
                image.close()


        print(file + "의 " + file2 + " "  +str(limit_per_one) + "장 증강 완료")

print("Process Done.")

end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
