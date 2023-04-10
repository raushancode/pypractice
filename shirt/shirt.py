import sys
from PIL import Image, ImageOps
from os.path import splitext


def main():

    check_arguments()

    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    # get the size of shirt
    size = shirt.size
    # resize muppet image,variable to fit the shirt
    muppet = ImageOps.fit(imagefile, size)
    # paste shirt in muppet
    '''wherein the first shirt represents the image to overlay and the second shirt represents
     a “mask” indicating which pixels in photo to update.'''
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

def check_arguments():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # elif not sys.argv[1:2].endswith(".jpg") or sys.argv[1:2].endswith(".jpeg") or sys.argv[1:2].endswith(".bmp"):
    #     sys.exit("Invalid output")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if chk_ext(file1[1]) == False:
        sys.exit("invalid Input")
    if chk_ext(file2[1]) == False:
        sys.exit("Invalid Output")
    if file1[1] != file2[1]:
        sys.exit("Input and output have different extensions")

def chk_ext(file):
    # print(file)
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    else:
        return False

if __name__ == "__main__":
    main()


