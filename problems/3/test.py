
# http://www.pythonchallenge.com/pc/def/equality.html

import pagestring

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

My first reaction is a regex, but I think that if I go that route, I'll have 
two problems.  I need a parser.

OTOH, my parser isn't returning the correct answer, and SO is full of people 
doing this with a regex, so I may have overthought.  Fix this to use a regex.

STATES
    - 1
        - start_tag_cnt == 0
        - Look for 1 lc letter
            - increment start_tag_cnt
        - Look for 3 uc letters
            - increment start_tag_cnt for each consecutive uc letter.  
            - If it gets to 4, we change state to mid_letter
    - 2
        - In this state we're looking for one lc letter.  Anything else 
          resets.
        - If we find a lc letter, set cand_letter and change state to end_tag.
    - 3
        - end_tag_cnt == 0
        - Look for 3 uc letters
            - inc end_tag_count for each one found
        - Look for 1 lc letter
            - WE'RE DONE - cand_letter is one of the letters we want.  Append 
              it to letters and reset_state_found().

            - Since the candidate letter we just found was lc, it might also 
              represent the first lc letter we're looking for in state 1.  
              reset_state_found() resets state but sets start_tag_cnt to 1 
              instead of 0.  I'm currently unclear of the rules.

This all seems perfectly cromulent, and the output is "inklet", which seems 
reasonable, but http://www.pythonchallenge.com/pc/def/inklet.html is a 404.

"""

letters = []
state = pagestring.State()
mystr = pagestring.get_pagestring()

for i in mystr:
    #print( i, "state", state.state )
    if state.state == 1:
        #print( "\t", state.start_tag_cnt )
        if state.start_tag_cnt == 0:
            if i.islower():
                state.start_tag_cnt = 1
        else:
            if i.isupper():
                state.start_tag_cnt += 1
                if state.start_tag_cnt == 4:
                    state.state = 2
            else:
                state.reset()
    elif state.state == 2:
        if i.islower():
            state.cand_letter = i
            state.state = 3
        else:
            #print( "\tresetting from state 2" )
            state.reset()
    elif state.state == 3:
        #print( "\t", state.end_tag_cnt )
        if state.end_tag_cnt < 3:
            if i.isupper():
                state.end_tag_cnt += 1
            else:
                state.reset()
        else:
            if i.islower():
                ### done
                letters.append( state.cand_letter )
            #state.reset_found()
            state.reset()

print( "".join(letters) )

