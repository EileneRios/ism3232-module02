# debug_log.md
# Author: Eilene Rios

## Bug 1
Error type: KeyError: 'amount'
File + line: week8_buggy.py, line 12, in get_total
What the error means: The code tried to look up the key 'amount' in a dictionary that doesn't have that key.
What I told the duck: Total starts at 0, then it loops through each record and adds its 'amount'. When I checked Taylor's it said 'amout' instead of 'amount'.
What I tried: Read the traceback bottom-up to line 12, then added a DEBUG print in the loop. It showed Taylor's record had 'amout'. 
How I fixed it: Corrected the spelling on line 4 to 'amount'

## Bug 2
Error type: TypeError: '>' not supported between instances of 'int' and 'str'
File + line: "/Users/eilene/ism3232/module05_functions/week8_buggy.py", line 16, in is_over_limit
What the error means: Python can’t use > to compare a number with text.
How I fixed it: I took the quotes off '1000' so it's the number 1000

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records / True
Did pytest pass? Yes / No

## AI Literacy Reflection
Did I use AI? Yes
If yes -- exact prompt I used: Based on the code and bug, can you explain what the code and error is saying like I'm explaining it to a duck.
What AI explained: AI helped me put the duck explanation into words and helped me understand the code better line by line.
What I changed myself: I added the DEBUG print and ran it to see each record, fixed the ‘amout’ typo, removed the DEBUG print, and took the quotes off ‘1000’.
Can I explain every fixed line? Yes

## What I learned
I learned to read a traceback from the bottom up, because the last line tells you the error type and the line above it shows where it happened. I also learned that a DEBUG print is an easy way to see what the data looks like right before the code crashes. Explaining code out loud was harder than I expected, but it made me slow down and actually look at each line instead of guessing but to also think logically.