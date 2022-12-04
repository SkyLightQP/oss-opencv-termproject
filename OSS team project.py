#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import  Image, ImageDraw, ImageFont
    
image = Image.open(result)
text_input = input('Enter the background country name : ')

def watermark(image):
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = text_input
    font = ImageFont.truetype('./font/Fine College.ttf', 325)
    textwidth, textheight = draw.textsize(text, font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x/2, y/2), text, font=font)
    
    return image

watermark(image)
image.show()
image.save("watermark.jpg")

