import cv2
import sys
import matplotlib.pyplot as plt
import numpy as np
NUM_PARTITIONS = int(sys.argv[2]) # This will be how many times the color line will be divided.
# Since there are 3 color lines, there will be a total of NUM_PARTITIONS^3 colors.

img = cv2.cvtColor(cv2.imread(sys.argv[1], cv2.IMREAD_COLOR), cv2.COLOR_BGR2RGB)
print(img.shape)
plt.imshow(img)
plt.show()
partitions_sums = {}
for r in range(img.shape[0]):
	for c in range(img.shape[1]):
		r_index = int(img[r][c][0] / 256 * NUM_PARTITIONS)
		g_index = int(img[r][c][1] / 256 * NUM_PARTITIONS)
		b_index = int(img[r][c][2] / 256 * NUM_PARTITIONS)
		if (r_index, g_index, b_index) in partitions_sums:
			partitions_sums[(r_index, g_index, b_index)] += 1
		else:
			partitions_sums[(r_index, g_index, b_index)] = 1

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
print(len(sums))
plt.bar(range(len(colors)), sums, color=colors, width=1)
[i.set_color(colors[c]) for c,i in enumerate(plt.gca().get_xticklabels())]
plt.tick_params(axis='x', which='both',bottom=False)
plt.show()