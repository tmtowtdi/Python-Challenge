
### http://www.pythonchallenge.com/pc/def/ocr.html

import pagestring

"""
The pic on the page is of a book, and the URL is "ocr".  But the pic of the 
book is way too blurry for OCR, and the text on the page says:
    recognize the characters. maybe they are in the book, <br>but MAYBE they 
    are in the page source.

So Ctrl-U shows me:
    <!--
    find rare characters in the mess below:
    -->

    <!--
    Huge long mess of characters
    -->

Since the huge long mess of characters is so long, and it's messing up the 
readability of this file, I copied it into ./pagestring.py.  I put the 
findrare() function in there too for good measure.

Running that long string through the findrare() function returns a dict 
strutured as char: occurences.  

Running through each character in that long string again, and only printing 
out characters that appear in that string a single time results in:
    equality

So the next problem is at:
    http://www.pythonchallenge.com/pc/def/equality.html

"""
pagestring = pagestring.get_pagestring()
rare_chars = findrare( pagestring )

for i in pagestring:
    if rare_chars[i] == 1:
        print( i, end="" )
print( "" )


