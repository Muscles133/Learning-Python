# # blank spot to test code


# import sys
# import csv
# from PIL import Image


# shirt = "shirt.png"

# result = {}


# image = Image.open(shirt)
# #images.append(image)

# result = Image.info(image)
# print(result)


from PIL import Image

def get_image_metadata(image_path):
    with Image.open(image_path) as img:
        # Get the image format (e.g., JPEG, PNG)
        format = img.format
        
        # Get the image mode (e.g., RGB, RGBA)
        mode = img.mode
        
        # Get the image size (width, height)
        width, height = img.size
        
        # Get the image resolution (in DPI)
        x_dpi, y_dpi = img.info.get('dpi', (None, None))
        
        return {
            "Format": format,
            "Mode": mode,
            "Size": f"{width}x{height} pixels",
            "Resolution": f"{x_dpi}x{y_dpi} DPI" if x_dpi and y_dpi else "Not available"
        }

# Example usage
image_path = "before1.jpg"
metadata = get_image_metadata(image_path)

for key, value in metadata.items():
    print(f"{key}: {value}")