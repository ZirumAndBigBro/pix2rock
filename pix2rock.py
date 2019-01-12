#Pix2rock
#Python 3.6.2
#script BigБро
#idea Zirum

# example result in result.txt
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#for npc: rock 730293 / small rock 730291

from PIL import Image
from random import randint

im = Image.open('result.bmp','r')
width, height = im.size
pix_val = list(im.getdata())
pix_val_flat = [x for sets in pix_val for x in sets]

#insert your bottom left start point
x0=1622
y0=1707
z0=150


# Item size
iw = 8 #width rock 730293(8) / small rock 730291(4)
ih = 8 #height rock 730293(8) / small rock 730291(4)
il = 8 #depth rock 730293(8) / small rock 730291(4)

file = open ('result.txt', 'w')
for h in range (0, height):
  for w in range (0, width):
    color_black = pix_val_flat[(3*w+h*width*3)] < 50 and pix_val_flat[(3*w+h*width*3)+1] < 50 and pix_val_flat[(3*w+h*width*3)+2] < 50
    if color_black:
     x = x0+w*iw 
     y = y0+(height-h-1)*ih
     z = z0
     h0 = (randint(0,120))
     file.write('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>\n'.format(h0, x, y, z))
file.close()
