from PIL import Image
import sys # To get command line arguments (optional)

def remove_white_background(input_path, output_path, white_threshold=235):
    """
    Removes white or near-white background from an image and makes it transparent.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the output image file (should be PNG).
        white_threshold (int): How close to white (0-255) a pixel's RGB values
                               need to be to be considered part of the background.
                               Checks if R, G, and B are all >= this value.
                               Adjust this based on your image's background variation.
                               Higher value (closer to 255) = stricter white.
                               Lower value = includes more light grays/off-whites.
    """
    if not (0 <= white_threshold <= 255):
        print("Error: white_threshold must be between 0 and 255.")
        return
# rgb(40, 42, 54)
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
            if item[0] == 40 and item[1] == 42 and item[2] == 54:
                # If it's close to white, make it fully transparent
                newData.append((255, 255, 255, 0)) # Transparent pixel
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

# --- How to use it ---

# 1. Define input and output file paths
input_image_file = 'Learning_Minecraft_Datapacks\\TikZ_Title_Page\\images\\ml_logo_main.png' # Or .png, .jpeg, etc.
output_image_file = 'output_image_transparent_bg_w.png' # Must be .png

# 2. Set the white threshold (adjust as needed)
#    - If your white background is pure white (255,255,255), threshold=255 might work.
#    - If it's slightly off-white or has JPEG artifacts, lower the threshold.
#    - Start with ~230-250 and see the results.
#    - This value means R, G, and B must ALL be AT LEAST this high.
wh_threshold = 215 # Example: Pixels with R,G,B all >= 240 become transparent

# 3. Call the function
remove_white_background(input_image_file, output_image_file, wh_threshold)

# --- Optional: Command line usage ---
# if __name__ == "__main__":
#     # (Similar command line argument parsing as the black background version,
#     # just calling remove_white_background instead)
#     if len(sys.argv) == 4:
#         input_file = sys.argv[1]
#         output_file = sys.argv[2]
#         try:
#             thresh = int(sys.argv[3])
#             remove_white_background(input_file, output_file, thresh)
#         except ValueError:
#             print("Error: Threshold must be an integer.")
#     elif len(sys.argv) == 3:
#          input_file = sys.argv[1]
#          output_file = sys.argv[2]
#          print("Using default white threshold of 235.")
#          remove_white_background(input_file, output_file) # Use default threshold
#     else:
#          print("Usage: python script_name.py <input_image> <output_image.png> [white_threshold]")
#          print("Example: python remove_white_bg.py photo.jpg photo_transparent.png 245")