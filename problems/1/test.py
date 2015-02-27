
# http://www.pythonchallenge.com/pc/def/map.html

import re, string

"""
See "code" below for the code from the page that needs to be translated.

Solution logic -- add 2 to the ordinal value of each letter.  If that result 
(ord + 2) takes you past 'z', you rotate back around to 'a' (so 'y' becomes 
'a', and 'z' becomes 'b').

Only translate letters, not spaces or punctuation.

my_attempt() is what I wrote at first.  It works, but its output tells me to try 
string.maketrans, so I created try_maketrans() since I'd never used maketrans()
before.  It works too, returning the same output:

    i hope you didnt translate it by hand. thats what computers are for. 
    doing it in by hand is inefficient and that's why this text is so 
    long. using string.maketrans() is recommended. now apply on the url.

The last part of the puzzle is from the text above -- "now apply on the url".  
We obviously can't translate the whole URL, since "jvvr://" is not a valid 
protocol.

I tried running the whole path portion of the current URL through the 
translator, but that led to a 404.

So I compared the current problem URL with the URL of the first problem:
    0) http://www.pythonchallenge.com/pc/def/0.html
    1) http://www.pythonchallenge.com/pc/def/map.html

Since the only difference between the two is the filename, I ran that ("map") 
through the translator and got "ocr", which leads to the next problem at
    2) http://www.pythonchallenge.com/pc/def/ocr.html
"""

def try_maketrans( code:str ):
    alpha = string.ascii_lowercase  # a-z
    new = alpha[2:] + alpha[0:2]    # c-z + a-b
    trans_dict = code.maketrans(alpha, new)

    for i in code:
        oi = ord(i)
        if oi in trans_dict:
            i = chr(trans_dict[oi])
        print( i, end="" )
    print( "" )

def my_attempt( code:str ):
    min = 97    # a
    max = 122   # z
    for i in code:
        if re.match("\w", i):
            newnum = ord(i) + 2
            if newnum > max:
                diff = newnum - max - 1
                newnum = min + diff
            i = chr(newnum)
        print( i, end="" )
    print( "" )


code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.  bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#my_attempt( code )
#try_maketrans( code )

url = "http://www.pythonchallenge.com/pc/def/map.html"
try_maketrans( url )



