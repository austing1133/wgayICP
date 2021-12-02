
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage import color
from skimage import io

#Read the input image and prepare for processing
def read_image(img_name):

    img = io.imread(img_name)
    img = color.rgb2gray(img)

    print(img.shape)

    #Note: the number being divided here MUST be able to divide the pixel dimension of the picture evenly. In other words, be a product of the dimensions of the picture.
    #In this picture the dimensions are 768,1024. 128 goes into 768 6 times evenly (128*6=768 or 768/128=6) must be a whole number. You can also tell from this that you will have 128 tiles across each having a 6 pixel width.
    M = img.shape[0]//60
    N = img.shape[1]//60

    tiles = [img[x:x+M, y:y+N] for x in range (0, img.shape[0], M) for y in range(0, img.shape[1], N)]
    tiles = np.array(tiles, dtype=object)

    return img, tiles, M, N        

#Reassembles the Tiles to form a new images with the output values of the K-Means Clustering Algorithm
def create_new_img(img, tiles, M , N):
    
    new_img = np.ones_like(img)

    count = 0
    for x in range (0, img.shape[0], M):
        for y in range(0, img.shape[1], N):
            new_img[x:x+M,y:y+N] = tiles[count]
            count += 1

    return new_img

#Calculates the distance between two points
def calc_distance(x1, x2, y1, y2):
    result = np.square(x1 - x2) + np.square(y1 - y2)
    result = np.sqrt(result)
    return result

#Initializes the initial means used in the k-means algorithm
def initialize(tiles, clusters):

    points = np.reshape(tiles, (tiles.shape[0], tiles.shape[1] * tiles.shape[2]))

    print("tiles")
    print(tiles.shape[0])
    print(tiles.shape[1])
    print(tiles.shape[2])

    m, n = points.shape
    means = np.zeros((clusters, n))

    for i in range(clusters):
        random0 = int(np.random.random(1)*15)
        random1 = int(np.random.random(1)*15)
        random2 = int(np.random.random(1)*20)
        means[i, 0] = points[random1, random0]
        means[i, 1] = points[random2, random0]
    
    return points, means

#runs the k-means algorithms
def k_means(points, means, clusters):
    #the max number of iterations the k-means algorithm goes through
    iterations = 10

    m, n = points.shape
    #This will hold the information for which cluster each point falls into as the algorithm runs.
    holder = np.zeros(m)

    while(iterations > 0):

        for j in range(len(points)):

            min_value = 50
            temp = None

            #Determines which cluster each point falls into for each iterations of the algorithm.
            for k in range(clusters):

                x1 = points[j,0]
                y1 = points[j,1]
                x2 = means[k,0]
                y2 = means[k,1]

                if (calc_distance(x1,x2,y1,y2) < min_value):
                    min_value = calc_distance(x1,x2,y1,y2)
                    temp = k
                    holder[j] = k
        
        #Calculates the new sample average for each cluster.
        for k in range(clusters):
            sumx = 0
            sumy = 0
            count = 0
            for j in range(len(points)):
                if (holder[j] == k):
                    sumx += points[j,0]
                    sumy += points[j,1]
                    count += 1       
            if count == 0:
                count = 1
            means[k,0] = float(sumx / count)
            means[k,1] = float(sumy / count)
        iterations -= 1

    #returns the sample average of each cluster and the final cluster that each point belongs to.
    return means, holder
        
#Compresses the image and assigns a single value for each tile
def compress_image(means, holder, tiles):
    values = np.array(means)
    recovered = values[holder.astype(int), :]
    
    recovered = np.reshape(recovered, (tiles.shape[0], tiles.shape[1], tiles.shape[2]))
    #Assigns the new value to every pixel in the tile.
    for i in range(recovered.shape[0]):
        for k in range(recovered.shape[1]):
            for j in range(recovered.shape[2]):
                recovered[i,k,j] = recovered[i,0,0]

    return recovered


clusters = 100
image, tiles, M, N = read_image('hummingbird.jpg')
points, means = initialize(tiles, clusters)
means, index = k_means(points, means, clusters)
altered_img = compress_image(means, index, tiles)
new_img = create_new_img(image, altered_img, M, N)
plt.figure(0)
plt.imshow(image)
plt.gray()
plt.figure(1)
plt.imshow(new_img)
plt.show()