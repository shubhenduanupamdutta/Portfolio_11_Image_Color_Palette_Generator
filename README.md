# Portfolio_11_Image_Color_Palette_Generator

## Eleventh (11) Portfolio Project: Image Color Palette Generator

### This program takes an image and generates top 10 most prevalent colors in the image.

### I have used pillow library to read the image and numpy to analyze it

### My process flow
 - First  I converted the image to a nested list
 - Then converted the list into a dictionary with count of pixel containing each color
 - Then sorted the dictionary by count of pixels
 - Then I used matplotlib to plot the color codes
 - In first try top 10 color were shades of yellow to further the color range I chose a number to measure similarity
 - 