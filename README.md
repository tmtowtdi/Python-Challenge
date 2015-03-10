
# Website
http://www.pythonchallenge.com/index.php

Once you're on a challenge page, you can change the path portion of the URL from "pc" to 
"pcc" to get to the solution.  eg:
    http://www.pythonchallenge.com/pc/def/peak.html     (the problem)
    http://www.pythonchallenge.com/pcc/def/peak.html    (link to the solution)
                                     ^

...actually, it looks like you have to solve the challenge first.  I just tried this for 
problem 6, which I haven't solved yet, and it took me to the solution for problem 5, which 
I have.

# Python headers
You need to get the headers with:
    sudo apt-get install python3-dev

You'll need those to install (at least), Pillow.

# Virtual env
Switch to the PyChallenge virtualenv.  I have a bash function named 'virtpyc' that'll make 
that switch.

Once you've changed virtualenv, be sure to run scripts with "python", not my normal "py" 
alias, which points to /usr/bin/python3, and which won't have any of the following 
additional modules installed.

So far, I've installed:
    - PyPNG
    - Pillow

