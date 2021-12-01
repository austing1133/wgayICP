William Gay <br />
ICP <br /> <br />
**Image Compression using K-Means Clustering**
<br />

The prupose of this repository is Pattern Recognition's ICP. The project is Image Compression using k-means clustering algorithm. Specifically this will be achieved by splitting the input image into M x N subimages, applying the k-means clustering algorithm to the subimages, and assigning each pixel in subimage to the value of the cluster the given sub image falls into. <br />
<br />
<br />
**Technique/Approach, Problem, and Data**
<br /><br />
In more detail... This project aims to achieve image compression by decreasing the amount of color values in the image while still being able to discern the picture. This method will not decrease the size or dimensions of the picture at that will stay the same. 
<br /><br />
The method of finding a common pixel value for each sub image is achieved using the straightforward k-means clustering algorithm. This algorithm the initial means by picking randomly from from the subimages. The number of means that are chosen is equal to the amount of clusters (means are the values of the clusters). Then iterating through each point, the closest cluster for the given point is chosen. After the initial iteration the sample average is taken of each cluster and a new mean is formed. The previous process is repeated however, the mean may not sit directly on a point for the following iterations. The algorithm completes, and each subimage is filled with the mean of the cluster that it falls into. Thus, the process is now complete.
<br />
<br />
**Experimental Results**
<br /><br />
Base:

![humming_bird_base](https://user-images.githubusercontent.com/56702193/144263538-49ff96a9-4c32-4123-a2c9-9f77185393c0.png)

60 x 60 Sub-Images, 1 Cluster

![hummingbird_60_60_1](https://user-images.githubusercontent.com/56702193/144268745-d2e6bcb5-ea4c-4dc2-bd9e-b565dcd0d30d.png)

60 x 60 Sub-Images, 2 Clusters

![humming_bird_60_60_2](https://user-images.githubusercontent.com/56702193/144268778-e2e858e8-1b89-427a-a79d-b82cac9fbfac.png)

60 x 60 Sub-Images, 5 Clusters

![huming_bird_60_60_5](https://user-images.githubusercontent.com/56702193/144269615-947465d5-956a-418d-b10f-3fd0dac22eaf.png)

20 x 20 Sub-Images, 25 Clusters

![humming_bird_20_20_25](https://user-images.githubusercontent.com/56702193/144268924-872cd779-a459-4644-aa63-c288b4e200de.png)

40 x 40 Sub-Images, 25 Clusters

![humming_bird_40_40_25](https://user-images.githubusercontent.com/56702193/144268929-de6b684d-10fc-4c0e-86fa-ec2c78068c2e.png)

60 x 60 Sub-Images, 25 Clusters

![humming_bird_60_60_25](https://user-images.githubusercontent.com/56702193/144268940-e3f8bbc6-51d9-43b3-84ce-2bfd948e51a1.png)

120 x 120 Sub-Images, 32 Clusters

![humming_bird_120_32](https://user-images.githubusercontent.com/56702193/144268991-56f16c01-9d5f-42e6-ac5a-faca21f6329d.png)

Base

![aquarium_base](https://user-images.githubusercontent.com/56702193/144270921-cfe9406b-0d55-4328-9093-01bfe8da6121.png)

120 x 120 Sub-Images, 10 Clusters

![aquarium_120_120_10](https://user-images.githubusercontent.com/56702193/144270263-4b061d4f-2d09-4ec4-854c-4e4e02c1c063.png)

128 x 256 Sub-Images, 10 Clusters

![aquarium_128_256_10](https://user-images.githubusercontent.com/56702193/144270962-80728941-81ab-4987-ab36-01b0b879cda4.png)

