from PIL import Image
import numpy as np

# Load your image; replace 'minecraft_logo.png' with your image file.
img = Image.open("Learning_Minecraft_Datapacks\\TikZ_Title_Page\\images\\right_face.png")
img = img.resize((16, 16))
data = np.array(img)

# Process the image data: remove alpha channel and convert each pixel to a simple RGB tuple.
matrix = []
for row in data:
    new_row = []
    for pixel in row:
        # Create a tuple with just the first three values (R, G, B) as Python ints.
        new_row.append((int(pixel[0]), int(pixel[1]), int(pixel[2])))
    matrix.append(new_row)

# Print the 16x16 matrix row by row.
print("RGB Matrix:")
for row in matrix:
    print(row)