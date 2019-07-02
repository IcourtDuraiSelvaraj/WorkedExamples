import colorsys

# Define RGB coordinates
r = 0.2
g = 0.4
b = 0.4

# Convert the color from RGB
# coordinates to HSV coordinates
hsv = colorsys.rgb_to_hsv(r, g, b)

# Print the HSV coordinates
print(hsv)