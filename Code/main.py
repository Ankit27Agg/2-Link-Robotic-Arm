import math
import matplotlib.pyplot as plt

#Both Arm's length
l1=1.5
l2=2

#no. of divisions for angle(0-90)
n_theta = 10

theta_start = 0
theta_end = 90

#now to store value of all angles in radian
theta1 = []
theta2 = []

#we can't right degree in formula thats why we use radians
for i in range(theta_start, theta_end+1, n_theta):  #(0, 91, 10)
    val = math.radians(i) #to convert into radian
    theta1.append(val)
    theta2.append(val)

#[x0, y0]
x0 = 0
y0 = 0

#for [x1, y1], [x2, y2]

#in this case 100 images will generate
image = 1

for i in theta1:
  for j in theta2:
    x1 = l1*math.cos(i)
    y1 = l1*math.sin(i)

    x2 = x1 + l2*math.cos(j)
    y2 = y1 + l2*math.sin(j)

    #create file for each output image
    fileName = str(image) + '.png'
    image+=1

    #plot the image
    plt.figure()
    plt.plot( [x0,x1],[y0,y1], 'r', linewidth=4) #(x-axis, y-axis, color, width)
    plt.plot( [x1,x2],[y1,y2], 'g', linewidth=4)

    #limits of x-axis and y-axis
    plt.xlim([0,5])
    plt.ylim([0,5])

    #labels
    plt.xlabel('X-AXIS')
    plt.ylabel('Y-AXIS')

    #save all the files
    plt.savefig(fileName)

