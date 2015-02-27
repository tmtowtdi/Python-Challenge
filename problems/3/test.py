
# http://www.pythonchallenge.com/pc/def/equality.html

import pagestring, re

"""
This is another puzzle with a huge mass of text buried in an HTML comment in 
the page source.  Again, I've copied that string into ./pagestring.py - see 
get_pagestring().

The text on the page says:
    One small letter, surrounded by EXACTLY three big bodyguards on each of 
    its sides. 
    
So my guess is that we're looking for three uc letters, a single lc letter, 
and three more uc letters.  The lc letter is the one we want.

Because of the word "EXACTLY", I'd amend that to:
    - one or more lc letters
    - 3 uc letters
    - 1 lc letter   <-- this is the one we want
    - 3 uc letters
    - one or more lc letters

This outputs the string "linkedlist".  Changing the current URL to 
http://www.pythonchallenge.com/pc/def/linkedlist.html produces a text/plain 
document that contains only the string "linkedlist.php", so I change the URL 
to http://www.pythonchallenge.com/pc/def/linkedlist.php to get to the next 
problem.

"""

letters = []
mystr = pagestring.get_pagestring()


pat = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")
letters = pat.findall(mystr)
print( ''.join(letters) )

