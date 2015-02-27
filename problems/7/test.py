
# http://www.pythonchallenge.com/pc/def/oxygen.html

"""
Page title is just "smarty"

Page has no text, just a short, wide image (ad-banner-shaped) of a river.
    named "oxygen.png".  Downloaded.

    The image has a gradient bar of various shades of gray through black 
    jammed horizontally into the center.

    it's 629x95 pixels.

There are no image-processing libraries in the core, so I'm going to install 
PyPng.  After setting up the PyChallenge virtualenv (and 'virtpyc' bash 
function -- run that.)



png.Reader returns a four-tuple with info on about the image.  The first two 
elemnts look like width and height, and the fourth is something else I don't 
care about.

The third element is a map object with info on the pixels in the image.

Each iteration through pixel_map (below) contains a bytearray of 2516 integers 
(0 <= X < 256).  The for loop iterates 95 times, and this image is 
95 pixels high, so each iteration is a row of pixels.

The image is 629 pixels wide, and 2516 / 629 == 4, so I'm guessing (because I 
really don't want to go read the PNG standard) that in that list of integers, 
four integers represent a single pixel.

When looking at the gradient bar on row 46, in that list of four integers per 
pixel, the first three integers are always the same value, and the last is 
always 255.  I'm assuming those first three are the color code - the last 255 
is probably the alpha channel.  I'm going to collect the color code for each 
distinct color in the gradient bar.

That weird gradient row is right in the middle, vertically, so we'll check out 
the middle ( h // 2 ).

The pixel data is one big list.  Four integers to one pixel, and the gradient 
blocks in the image are 7 pixels wide.  That's why the range() calls below are 
advancing by 4*7.

Both of my attempts below produce:
    smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]jld

Note that the gradient bar does not extend all the way to the right border of 
the image, so the junk seen above after the ] is expected - it's where the 
gradient bar ends.

Anyway, after copy/pasting that list of integers from the output above and 
passing that through chr(), we get the word
    integrity

So, off to
    http://www.pythonchallenge.com/pc/def/integrity.html


### How far did I get on my own
Almost complete.  I didn't like the idea of guessing at the pixel width of the 
gradient blocks, so instead I recorded the current color and then recorded the 
next gradient when the color changed.

Of course, doing that disallows repeated characters.  So "110", "116", etc in 
the list of ints that I needed to come up with "integrity" were outputting as 
just "10", "16", etc.

When I fell back to skipping 7 pixels to the right at a time, all was fixed.

"""

import png, time

file = "oxygen.png"
fh = open(file, "rb")
r = png.Reader(fh)
w, h, pixel_map, mydict = r.read()

### A list is easier to deal with than a map.
pixel_list = list(pixel_map)

### This was my first attempt
gradients = []
row = 0
for pixel_row in pixel_list:
    row +=1
    if row != h // 2:
        continue
    for i in range( 0, len(pixel_row), 4*7):
        gradients.append( pixel_row[i] )
word = "".join([ chr(g) for g in gradients ])
print( word )

### This is my second attempt, cleaned up a bit.  Just work directly on the 
### correct row instead of iterating them all, looking for the right one.
gradients = []
pixel_row = pixel_list[ h//2 ]
for i in range( 0, len(pixel_row), 4*7):
    gradients.append( pixel_row[i] )
word = "".join([ chr(g) for g in gradients ])
print( word )


### After getting the correct output by running the above, I need to chr the 
### list of ints from the output.
print( "".join([ chr(g) for g in [105, 110, 116, 101, 103, 114, 105, 116, 121] ]) )


