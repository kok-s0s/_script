# Created by: kok-s0s
# Last Modified at: Tue Jan  9 13:27:43 2024
# File Name: image_handle.py

import argparse
import os
from PIL import Image, ImageEnhance


def get_default_output_path(input_path, extension):
    input_dir, input_filename = os.path.split(input_path)
    filename_without_extension, _ = os.path.splitext(input_filename)
    output_filename = f"{filename_without_extension}_output.{extension}"
    return os.path.join(input_dir, output_filename)


def resize_image(input_path, output_path, new_size):
    with Image.open(input_path) as img:
        resized_img = img.resize(new_size)
        resized_img.save(output_path)


def adjust_brightness_contrast(
    input_path, output_path, brightness_factor, contrast_factor
):
    with Image.open(input_path) as img:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_factor)

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast_factor)

        img.save(output_path)


def rotate_image(input_path, output_path, angle):
    with Image.open(input_path) as img:
        rotated_img = img.rotate(angle)
        rotated_img.save(output_path)


def jpeg_to_png(input_path, output_path):
    with Image.open(input_path) as img:
        img.save(output_path, format="PNG")


def png_to_jpeg(input_path, output_path):
    with Image.open(input_path) as img:
        rgb_img = img.convert("RGB")
        rgb_img.save(output_path, format="JPEG")


def gif_to_jpeg(input_path, output_path):
    with Image.open(input_path) as img:
        img.convert("RGB").save(output_path, format="JPEG")


def jpeg_to_ico(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format="ICO", sizes=[(32, 32)])
        print(f"Conversion successful: {output_path}")
    except Exception as e:
        print(f"Conversion failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="Image Conversion CLI")
    parser.add_argument("input_path", help="Input image file path")
    parser.add_argument("-o", "--output_path", help="Output image file path")

    parser.add_argument(
        "-r",
        "--resize",
        nargs=2,
        type=int,
        metavar=("width", "height"),
        help="Resize image",
    )
    parser.add_argument("-b", "--brightness", type=float, help="Adjust brightness")
    parser.add_argument("-c", "--contrast", type=float, help="Adjust contrast")
    parser.add_argument("-t", "--rotate", type=float, help="Rotate image")
    parser.add_argument(
        "-j2p", "--jpeg_to_png", action="store_true", help="Convert JPEG to PNG"
    )
    parser.add_argument(
        "-p2j", "--png_to_jpeg", action="store_true", help="Convert PNG to JPEG"
    )
    parser.add_argument(
        "-g2j", "--gif_to_jpeg", action="store_true", help="Convert GIF to JPEG"
    )
    parser.add_argument(
        "-j2i", "--jpeg_to_ico", action="store_true", help="Convert JPEG to ICO"
    )

    args = parser.parse_args()

    if not args.output_path:
        # If output path not specified, create a default output path
        conversion_type = None
        for action in parser._actions:
            if action.dest in [
                "jpeg_to_png",
                "png_to_jpeg",
                "gif_to_jpeg",
                "jpeg_to_ico",
            ]:
                if getattr(args, action.dest):
                    conversion_type = action.dest
                    break
        if conversion_type:
            args.output_path = get_default_output_path(
                args.input_path, conversion_type.split("_")[-1]
            )

    if args.resize:
        resize_image(args.input_path, args.output_path, tuple(args.resize))
    elif args.brightness or args.contrast:
        adjust_brightness_contrast(
            args.input_path,
            args.output_path,
            args.brightness or 1.0,
            args.contrast or 1.0,
        )
    elif args.rotate:
        rotate_image(args.input_path, args.output_path, args.rotate)
    elif args.jpeg_to_png:
        jpeg_to_png(args.input_path, args.output_path)
    elif args.png_to_jpeg:
        png_to_jpeg(args.input_path, args.output_path)
    elif args.gif_to_jpeg:
        gif_to_jpeg(args.input_path, args.output_path)
    elif args.jpeg_to_ico:
        jpeg_to_ico(args.input_path, args.output_path)
    else:
        print("No conversion specified. Use --help for options.")


if __name__ == "__main__":
    main()
