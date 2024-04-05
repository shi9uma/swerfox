# -*- coding: utf-8 -*-

'''
app: mtf
author: shiguma
repo: https://github.com/shi9uma/swerfox.git
description: 无糖木桶饭！
'''

# 麻了, 我真不想在我这 b 2060 笔记本上装 cuda 环境，老是到 c 盘去拉 shit

import tools

import torch
import cv2
from segment_anything import sam_model_registry
from segment_anything import SamAutomaticMaskGenerator

# path
root_path = tools.ROOTPATH
checkpoint_path = tools.xpath(root_path, 'test/sam_vit_h_4b8939.pth')
src_sw_img_path = tools.xpath(root_path, 'test/sw.jpg')

DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
MODEL_TYPE = "vit_h"

sam = sam_model_registry[MODEL_TYPE](checkpoint=checkpoint_path)
sam.to(device=DEVICE)

mask_generator = SamAutomaticMaskGenerator(sam)
image_bgr = cv2.imread(src_sw_img_path)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
result = mask_generator.generate(image_rgb)


exit()
from PIL import Image, ImageDraw

# Load the original image
original_image_path = '/mnt/data/b_7c750d714725e245a84db9d4b27aff2a.jpg'
original_image = Image.open(original_image_path)

# Calculate stripe height
stripe_height = original_image.height // 3

# Create a new image with stripes
striped_image = Image.new("RGB", (original_image.width, original_image.height))
draw = ImageDraw.Draw(striped_image)

# Define the colors for the pride flag stripes
colors = ('#FFC0CB', '#FFFFFF', '#87CEFA')  # Pink, White, Blue

# Draw the stripes
for i, color in enumerate(colors):
    draw.rectangle(
        [(0, stripe_height * i), (original_image.width, stripe_height * (i+1))],
        fill=color
    )

# Save the new image
striped_background_path = '/mnt/data/striped_background.jpg'
striped_image.save(striped_background_path)
striped_background_path


# First, we'll create the striped background as before
def create_striped_background(image_size):
    stripe_height = image_size[1] // 3
    striped_bg = Image.new("RGB", image_size)
    draw = ImageDraw.Draw(striped_bg)
    colors = ('#FFC0CB', '#FFFFFF', '#87CEFA')  # Pink, White, Blue
    for i, color in enumerate(colors):
        draw.rectangle([(0, stripe_height * i), (image_size[0],
                       stripe_height * (i+1))], fill=color)
    return striped_bg

def extract_character(original_img):
    r, g, b, a = original_img.split()
    character_img = Image.new("RGBA", original_img.size)
    character_img.paste(original_img, (0, 0), a)
    return character_img



def combine_images(character_img, striped_bg):
    striped_bg = striped_bg.resize(character_img.size)
    striped_bg = striped_bg.convert("RGBA")
    final_img = Image.alpha_composite(striped_bg, character_img)
    return final_img


original_image = Image.open(original_image_path).convert("RGBA")
striped_bg = create_striped_background(original_image.size)
character_img = extract_character(original_image)
final_image = combine_images(character_img, striped_bg)

final_image_path = '/mnt/data/final_striped_character_image.png'
final_image.save(final_image_path, format="PNG")

final_image_path
