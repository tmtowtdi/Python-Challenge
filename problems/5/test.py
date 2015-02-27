
# http://www.pythonchallenge.com/pc/def/peak.html

"""
Page has a pic of a hill, with the text "pronounce it".

Page source contains HTML comment:
    peak hell sounds familiar ?

So I changed the URL to
    http://www.pythonchallenge.com/pc/def/pickle.html
    (which is one hell of a stretch).

So http://www.pythonchallenge.com/pc/def/pickle.html contains the text
    yes! pickle!

    with nothing else interesting in the page source. (JDB)

The source of the original page (peak.html) also contains this:
    <peakhell src="banner.p"/>
which contains a bunch of encoded crap I'd original taken to be some sort of 
inlining of the image on the page, but I'm starting to guess it's a pickled 
object.  I've saved that to ./banner.p

Unpickling that file works.  It contains a list of lists of tuples:
   [[(' ', 95)],
    [(' ', 14), ('#', 5), (' ', 70), ('#', 5), (' ', 1)],
    [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
    [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
    [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
    [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
    [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
    [(' ', 15), ('#', 4), (' ', 71), ('#', 4), (' ', 1)],
...etc...

I'd originally thought this looked kind of like a linked list, but the numbers 
and values don't make any sense in that context.

(this bit I had to look up, since I couldn't figure out what to do with the 
un-pickled data.)
What it is is a list of rows meant to be output.  Each sublist is one row.

So the first row consists of 95 spaces.
The next row is 14 spaces, 5 hashes, 70 spaces, 5 hashes, and 1 space.  etc.

Print it out like that and we get:
              #####                                                                      ##### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
               ####                                                                       #### 
      ###      ####   ###         ###       #####   ###    #####   ###          ###       #### 
   ###   ##    #### #######     ##  ###      #### #######   #### #######     ###  ###     #### 
  ###     ###  #####    ####   ###   ####    #####    ####  #####    ####   ###     ###   #### 
 ###           ####     ####   ###    ###    ####     ####  ####     ####  ###      ####  #### 
 ###           ####     ####          ###    ####     ####  ####     ####  ###       ###  #### 
####           ####     ####     ##   ###    ####     ####  ####     #### ####       ###  #### 
####           ####     ####   ##########    ####     ####  ####     #### ##############  #### 
####           ####     ####  ###    ####    ####     ####  ####     #### ####            #### 
####           ####     #### ####     ###    ####     ####  ####     #### ####            #### 
 ###           ####     #### ####     ###    ####     ####  ####     ####  ###            #### 
  ###      ##  ####     ####  ###    ####    ####     ####  ####     ####   ###      ##   #### 
   ###    ##   ####     ####   ###########   ####     ####  ####     ####    ###    ##    #### 
      ###     ######    #####    ##    #### ######    ###########    #####      ###      ######


So on to http://www.pythonchallenge.com/pc/def/channel.html

"""

import pickle, pprint

fh = open("banner.p", "rb")
rslt = pickle.load(fh)
fh.close
#pprint.pprint( rslt )   # the thing I think is a linked list.

for item in rslt:
    print( "".join(i[0] * i[1] for i in item) ) #print characters



