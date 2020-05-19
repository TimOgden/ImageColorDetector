import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np

def partition_slow(img):
	for r in range(img.shape[0]):
		for c in range(img.shape[1]):
			r_index = int(img[r][c][0] / 256 * NUM_PARTITIONS)
			g_index = int(img[r][c][1] / 256 * NUM_PARTITIONS)
			b_index = int(img[r][c][2] / 256 * NUM_PARTITIONS)
			if (r_index, g_index, b_index) in partitions_sums:
				partitions_sums[(r_index, g_index, b_index)] += 1
			else:
				partitions_sums[(r_index, g_index, b_index)] = 1

def partition_fast(img):
	img = img.astype(np.float32)
	img /= 256.
	img *= NUM_PARTITIONS
	img = img.astype(np.int8)
	print(img[10][25])
	print('Shape:', img.shape)
	offset = 256/(NUM_PARTITIONS*2)
	for r in range(NUM_PARTITIONS):
		for g in range(NUM_PARTITIONS):
			for b in range(NUM_PARTITIONS):
				#print(r,g,b)
				partitions_sums[(r,g,b)] = (img==(r,g,b)).all(axis=-1).sum()


NUM_PARTITIONS = int(sys.argv[2]) # This will be how many times the color line will be divided.
# Since there are 3 color lines, there will be a total of NUM_PARTITIONS^3 colors.

img = cv2.cvtColor(cv2.imread(sys.argv[1], cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
print(img.shape)
plt.imshow(img)
plt.show()
partitions_sums = {}
partition_fast(img)



colors = []
sums = []
offset = 256/(NUM_PARTITIONS*2)
for key in partitions_sums.keys():
	color = [((key[0]*256)/NUM_PARTITIONS + offset)/255., 
			((key[1]*256)/NUM_PARTITIONS + offset)/255.,
			((key[2]*256)/NUM_PARTITIONS + offset)/255.]
	colors.append(color)
	sums.append(partitions_sums[key])
sums, colors = zip(*sorted(zip(sums, colors), reverse=True))
plt.bar(range(len(colors)), sums, color=colors, width=1)
plt.tick_params(axis='x', which='both',bottom=False)
plt.show()