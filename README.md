# ImageColorDetector
Simple algorithm to sort every pixel of an image into a certain partition of the 3 dimensional RGB color space and see its distribution.

# Explanation
Many years ago, I thought about how I could take an image, read the pixels, and return the most frequent color that I see. In my naivety, I began defining "classes" of color with a lot of difficulty. For example, the color "green" would be when the g-value was above some high threshold and the r and b values were below a low threshold. The difficulties here is that defining each color is painstaking, especially when it's not a primary color, such as purple or orange, and mistakes were bountiful. Another drawback to this approach is the fact that I only have a set amount of color classes that a pixel can fall in, and making more or less would be laborious.

Years later, using a more mathematical approach, I came up with this idea.
In normal 8-bit image storage like in a JPEG or PNG file, there are 3 axes, R, G, and B that define a color. We can think of these axes just like a normal 3-dimensional basis, think the X,Y, and Z axes in any 3d modelling software.

![Basis.png](Our 3-dimensional normal basis)

Now, we can just imagine our pixel color as some point in the cube = { (r,g,b) s.t. [0<=value<256 for value in (r,g,b)] }.

![Color_Space.png)(Our 3-dimensional color space)
Obviously, we are asking a question about an (almost) continuous space. There are 3^256 isolated points that are unique colors in this cube.
To fix this, we need to associate similar colors into the same "class". To do this is simple, though. We simply need to partition this cube up into n different classes per axis. In the case of n=3, we are making three distinct thresholds that divide the classes in each axis. This will look just like a Rubic's Cube! In a general case of n partitions per axis, we will get 3^n total partitions in our space.

Now, it's just a matter of looping through the pixels of the image and classifying which partition they fall in!

In the end, we use some pretty matplotlib code to display the distribution of colors with a respectively colored bar graph.

#Usage
`python image_detector.py **YOUR_IMAGE_FILE** NUM_PARTITIONS`

#Example
`python image_detector.py train.jpg 5`
This will result in 3^5=243 different partitions of the color space.
