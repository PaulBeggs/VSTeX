from PIL import Image

def remove_white_background(input_path, output_path, rgb_values, changed_rgb):
    """
    Removes white or near-white background from an image and makes it transparent.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the output image file (should be PNG).
        rgb_values (tuple): the 3 values for red green and blue pixels that are
                            needing to be changed in the document.
    """
    try:
        # Open the image
        img = Image.open(input_path)

        # Ensure image is in RGBA format
        img = img.convert("RGBA")

        # Get the image data
        datas = img.getdata()

        newData = []
        for item in datas:
            # Check if the pixel is close to white based on the threshold
            # item[0] = Red, item[1] = Green, item[2] = Blue
            # Check if R, G, AND B are ALL >= white_threshold
            if item[0] == rgb_values[0] and item[1] == rgb_values[1] and item[2] == rgb_values[2]:
                # If it's close to white, make it fully transparent
                newData.append((changed_rgb[0], changed_rgb[1], changed_rgb[2], 255)) # Transparent pixel
            else:
                # Otherwise, keep the original pixel, making sure it's opaque
                newData.append((item[0], item[1], item[2], 255)) # Opaque pixel

        # Update image data
        img.putdata(newData)

        # Save the new image as PNG
        img.save(output_path, "PNG")
        print(f"Successfully processed '{input_path}' and saved as '{output_path}'")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# 1. Define input and output file paths
input_image_file = 'Learning_Minecraft_Datapacks\\TikZ_Title_Page\\images\\mwe_Page_22_m.png'
output_image_file = 'new_rgb_file.png'

# 2. Set RGB values
rgb_values = (0, 0, 0)
changed_rgb = (248, 248, 242)

# 3. Call the function
remove_white_background(input_image_file, output_image_file, rgb_values, changed_rgb)