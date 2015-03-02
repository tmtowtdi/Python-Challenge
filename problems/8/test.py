
# http://www.pythonchallenge.com/pc/def/integrity.html

"""
Picture of a bee, part of which is hyperlinked to ../return/good.html.

That hyperlinked URL is password protected.  The realm is "inflate".


This is in a comment in the page:
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
-->


This was way harder than it needed to be.  I figured out that the un and pw 
above were compressed with BZ2, but couldn't get them to decompress.  I was 
trying to change the strings to bytes, break up the header from the data, etc.

The end result was that the code below, which was what I originally tried, 
only works with python2, NOT python3.  

python3 gives a complaint about strings not supporting the buffer interface.  
But it works just fine under python2.

Anyway, logging in with huge:file takes us to
    http://www.pythonchallenge.com/pc/return/good.html

"""

import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

### python 2 works OK like this
print( bz2.BZ2Decompressor().decompress(un) )
print( bz2.BZ2Decompressor().decompress(pw) )

### This encoding crap is what I was trying with python3, but can't get it to 
### work.  I suspect it might be because the header is a string, not bytes, 
### but I couldn't figure out how to get it to work even with breaking out the 
### header and writing it to a file as text, then appending what looks like 
### the data after it as bytes.
#print( bz2.BZ2Decompressor().decompress(un.encode('UTF-8')) )
#print( bz2.BZ2Decompressor().decompress(pw.encode('UTF-8')) )


