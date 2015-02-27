
# http://www.pythonchallenge.com/pc/def/linkedlist.php

"""
You can run this as-is and just let it go.


Title of the page is "follow the chain"

The image on this page is hyperlinked to
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

HTML comment in page source says:
    urllib may help. DON'T TRY ALL NOTHINGS, since it will never 
    end. 400 times is more than enough.

Clicking the image leads to a page with "The next nothing is <numbers>"
    So I have to keep finding those <numbers>, putting them in as the nothing 
    argument, and following that URL.

http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044 
contains "Yes.  Divide by two and keep going."  
So http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022 is back 
to "The next nothing is <numbers>".  So I'm going to have to special-case this 
nonsense.

http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=82682
contains
    There maybe misleading numbers in the 
    text. One example is 82683. Look only for the next nothing and the next nothing is 63579
...my regex does catch that properly, but we definitely can't shorten it to just 
look for numbers.

http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831
This is the payoff URL.  My script dies here because none of the regexen match, 
and the contents of this page are:
    peak.html

So moving on to http://www.pythonchallenge.com/pc/def/peak.html
"""

import pychallenge, requests

pyc = pychallenge.Pyc()

while(True):
    resp = pyc.get_url()
    pyc.find_nothing( resp )
    pyc.set_url()
