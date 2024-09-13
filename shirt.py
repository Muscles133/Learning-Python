import sys
from PIL import Image


def main():
    check_agr()

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    shirt_img = "shirt.png"

    try:
        with Image.open(in_file) as im:
            # (width, height) = (im.width//2, im.height//2)
            target_size = (600, 600)
            img_resized = im.resize((im.width // 2, im.height // 2))

            # Calculate dimensions for cropping
            width, height = img_resized.size
            left = 0
            top = (height - target_size[1]) // 2
            right = target_size[0]
            bottom = top + target_size[1]

            # Crop the image
            img_cropped = img_resized.crop((left, top, right, bottom))

            if img_cropped.mode != "RGBA":
                img_cropped = img_cropped.convert("RGBA")

            with Image.open(shirt_img) as shirt:
                if shirt.mode != "RGBA":
                    shirt = shirt.convert("RGBA")

                result = Image.alpha_composite(img_cropped, shirt)
                result = result.convert("RGB")

                result.save(out_file)

    except:
        sys.exit("Failed to write")


def check_agr():
    try:
        if len(sys.argv) == 3:
            if not sys.argv[1].endswith(".jpg"):
                sys.exit("Not a .jpg")
            elif not sys.argv[2].endswith(".jpg"):
                sys.exit("Not a .jpg")
            else:
                return
            
        elif len(sys.argv) >= 2:
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        else:
            sys.exit("Not a jpg file")

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
