
# http://www.pythonchallenge.com/pc/return/5808.html

"""
title: odd even
pic: (cave.jpg) blurry, long-exposure pic of people in what might be an 
open-air market (downloaded)

Page contains no comments, but it does have a font tag that's not doing 
anything that I find suspicious.  This is the entire contents of 
<body>...</body>:
    <br><br>
	<center>
	<img src="cave.jpg" width="640" height="480" border="0"/>
	<br>
	<br>
    <font color="gold" size="+1"></font>

Run this, see "out.png", which contains the word "evil"

So, on to
    http://www.pythonchallenge.com/pc/return/evil.html

"""

from PIL import Image, ImageDraw
import re

input_filename = 'cave.jpg'

im              = Image.open(input_filename)
width, height   = im.size

even        = Image.new( 'RGB', (width,height), (0,0,0) )
odd         = Image.new( 'RGB', (width,height), (0,0,0) )
even_draw   = ImageDraw.Draw(even)
odd_draw    = ImageDraw.Draw(odd)


def make_hex_color(r, g, b):
    pat = re.compile("^0x")
    rhex = pat.sub( "", hex(r) )
    bhex = pat.sub( "", hex(g) )
    ghex = pat.sub( "", hex(b) )
    return "#" + rhex.zfill(2) + bhex.zfill(2) + ghex.zfill(2)


cnt = 0
for w in range(0,width):
    for h in range(0,height):
        r, g, b = im.getpixel( (w,h) )
        cnt += 1

        if not w % 2 and not h % 2:
            outw = w/2
            outh = h/2
            out = even_draw
        elif not w % 2 and h % 2:
            outw = w/2
            outh = (h-1)/2
            out = odd_draw
        elif w % 2 and not h % 2:
            outw = (w-1)/2
            outh = h/2
            out = even_draw
        else:
            outw = (w-1)/2
            outh = (h-1)/2
            out = odd_draw

        out.point( [(outw,outh)], make_hex_color(r, g, b) )

even.save( "even.png", "PNG" )
odd.save( "odd.png", "PNG" )
