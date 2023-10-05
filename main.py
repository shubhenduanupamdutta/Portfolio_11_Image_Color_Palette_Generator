from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Image File Path
IMAGE_PATH = 'sample.jpg'
# Number which indicates what difference between two shades is considered same color
COLOR_DIFFERENCE = 25

# Load Image
pixel_list = np.array(Image.open(IMAGE_PATH)).tolist()


def is_same_color(pixel1, pixel2):
    """
    Returns True if both pixels are almost of same color
    """
    for i in range(3):
        if abs(pixel1[i] - pixel2[i]) > COLOR_DIFFERENCE:
            return False
    return True


# convert img_array to a dictionary of colors
color_dict = {}
total_pixel_count = len(pixel_list) * len(pixel_list[0])
for row in pixel_list:
    for pixel in row:
        color_dict[tuple(pixel)] = color_dict.get(tuple(pixel), 0) + 1

color_list = list(color_dict.keys())
# merging similar colors
merged_colors = []
for color in color_list:
    is_merged = False
    for merged_color in merged_colors:
        if is_same_color(color, merged_color):
            try:
                color_dict[tuple(merged_color)] += color_dict[tuple(color)]
                del color_dict[tuple(color)]
            except KeyError:
                pass
            is_merged = True

    if not is_merged:
        merged_colors.append(color)


# update pixel_list with new values
pixel_list = []

# sorting the dictionary by values, taking in top 10
for color, pixel_count in sorted(color_dict.items(), key=lambda item: item[1], reverse=True)[:10]:
    pixel_list.append([color, round(pixel_count * 100 / total_pixel_count, 2)])

# showing top 10 color using imshow

# using repeating color code to plot color
top_color_image_array = np.zeros((500, 500, 3), dtype=np.uint8)
repeat_factor = 50

for i in range(10):
    color = pixel_list[i][0]
    top_color_image_array[i * repeat_factor:(i + 1) * repeat_factor, :, :] = color

print(pixel_list)
plt.imshow(top_color_image_array)
plt.axis('off')
plt.show()

