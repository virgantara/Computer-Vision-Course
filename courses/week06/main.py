import matplotlib.pyplot as plt
import numpy as np

from scipy import ndimage
import os
import cv2
from util import rgb2gray, gradient_x, gradient_y

input_path = "data"
output_path = "output"
# img_name = ['buku.jpg']
img_name = ["bicycle.bmp", "bird.bmp","buku.jpg", "dog.bmp", "toy_image.jpg"]
ratio = [0.05, 0.05, 0.05, 0.05, 0.01, 0.001]
count = 0 #for equivalent ratio access

for img in img_name :
    #Phase I : Find filtered grdient
    #Load the input images
    file_path = os.path.join(input_path, img)
    input_img = cv2.imread(file_path)
    input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
    # print(input_img.dtype)

    #Convert the image to grayscale
    gray_input_img = rgb2gray(input_img)

    #Apply gaussian blurring
    blur_img = ndimage.gaussian_filter(gray_input_img, sigma = 1.0)

    #Find gradient Fx
    x_grad = gradient_x(blur_img)

    #Find gradient Fy
    y_grad = gradient_y(blur_img)


    
    #Phase II : Find corners
    xx_grad = x_grad * x_grad
    yy_grad = y_grad * y_grad
    xy_grad = x_grad * y_grad
    tuple_data = [] #Contains y, x Co-ordinates and its corner response
    k = 0.04
    max = 0

    for i in range(1, int(input_img.shape[0] - 1)) :
            for j in range(1, int(input_img.shape[1] - 1)) :
                window_x = xx_grad[i-4 : i+5 , j-4 : j+5]
                window_y = yy_grad[i-4 : i+5 , j-4 : j+5]
                window_xy = xy_grad[i-4 : i+5 , j-4 : j+5] 
                sum_xx = np.sum(window_x)
                sum_yy = np.sum(window_y)
                sum_xy = np.sum(window_xy)
                determinant = (sum_xx * sum_yy) - (sum_xy * sum_xy)
                trace = sum_xx + sum_yy
                R = determinant - (k * trace * trace)
                tuple_data.append((i, j, R))
                if(R > max) :
                    max = R
    print(max)
    #L contains y, x co-ordinate(whose value is greater than threshold) and their corner response of those co-ordinates
    L = []
    thres_ratio = ratio[count]
    count+=1
    threshold = thres_ratio * max
    for res in tuple_data :
        i, j, R = res
        if R > threshold :
            L.append([i, j, R])
          
    
    
    #Phase III : Non maximal suppression
    sorted_L = sorted(L, key = lambda x: x[2], reverse = True)
    final_L = [] #final_l contains list after non maximal suppression
    final_L.append(sorted_L[0][:-1])
    dis = 10
    xc, yc = [], []
    for i in sorted_L :
        for j in final_L :
            if(abs(i[0] - j[0] <= dis) and abs(i[1] - j[1]) <= dis) :
                break
        else :
            final_L.append(i[:-1])
            xc.append(i[1])
            yc.append(i[0])
    print(len(sorted_L))
    print(len(final_L))
    
    #Print Final Image
    corner_img = np.zeros(input_img.shape)
    #(input_img.shape[0], input_img.shape[1], 3), dtype = np.uint8)

    for i in final_L :
        y, x = i[0], i[1]
        corner_img[y][x] = 1

    plt.imshow(input_img, cmap = plt.get_cmap('gray'))
    plt.plot(xc, yc, '*', color='red')
    file_output_path = os.path.join(output_path, img.split('.')[0]+"_corners.jpg")
    plt.savefig(file_output_path)
    plt.show()
    