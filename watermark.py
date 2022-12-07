#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import ImageDraw, ImageFont
    
def watermark(image):
    text_input = input('Enter the background country name : ')
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = text_input
    font = ImageFont.truetype('./font/Fine College.ttf', 325)
    textwidth, textheight = draw.textsize(text, font)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x/2, y/2), text, font=font)
    
    image.save("result.jpg")
    
    return image


