
# http://www.pythonchallenge.com/pc/def/channel.html

"""
    Picture is of a pair of jeans, specifically the zipper.

    Title is "now there are pairs".

    The HTML tag has an incorrect double comment that I'm not sure yet whether 
    it's a mistake or a hint:
        <html> <!-- <-- zip -->
        <head>

    There's also a PayPal donation button on this page.  The comments claim 
    that it's not part of the puzzle, just a request for donations, and clicking 
    on it does take me to paypal, pre-filled for the python challenge.  So I 
    think it's a legit donation button, really not a hint.

    I know about zip(), and assume I have to use it, but don't know what I'm 
    supposed to be zipping.  The links in the page source are to the same 
    styles.css I've seen on other pages, the image, which appears to be an 
    image, and the paypal thing.  No other links.

    I'm saving the image to ./channel.jpg.  Opening that in gvim, it doesn't 
    look (just by an eyeball) like anything other than a jpg created with the 
    Gimp.

    The jeans in the image have a button with text on it.  I can only read it 
    by blowing up the image.  It's just the word "SPRINT", twice.  It appears 
    to be the maker of the jeans.

    The jeans are lying on a patterned piece of cloth.  There's what looks like 
    an arrow on the cloth, and it's pointing towards a pattern that looks kind 
    of like the letter "w", or possibly the number "3", but this is starting to 
    feel like stretching.


    *sigh* - there's a Zip file at "channel.zip".  Downloaded.
        The fact that zip() exists, and it combines pairs of things, along with 
        the fact that the page source says "now there are pairs", and contains 
        a "pair" of jeans, really leads to the idea that we'll be using zip() 
        rather than dealing with a zipfile, which is a bit of a cheap red 
        herring, I think.

    The zip file contains a crapton of .txt files.  "readme.txt" contains:
        welcome to my zipped list.
        hint1: start from 90052
        hint2: answer is inside the zip

    The rest of the zipfiles are numbered, 90052.txt etc.  90052.txt contains:
        Next nothing is 94191

    Following the nothings to the next file leads to 46145.txt, which contains:
        Collect the comments.

    So I modified Pyc to get getinfo() on each matching file and store the 
    comments specific to that file.  Printing out all the comments at the end 
    results in:

****************************************************************
****************************************************************
**                                                            **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
**                                                            **
****************************************************************
 **************************************************************

So on to http://www.pythonchallenge.com/pc/def/hockey.html

"""

import pythonchallenge

pyc = pythonchallenge.Pyc()

while(True):
    pyc.read_current_file()

