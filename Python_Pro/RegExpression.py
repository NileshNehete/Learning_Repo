# -*- coding: cp1252 -*-
# serach the 10 digit number from the tuple.

import re
phonebook = ('9850984430','9960633284','98er98443O','99950')
 
matchnum = re.findall("\d{10}",str(phonebook))
print "below matched phone numbers are found"
for phone in matchnum:
    print phone



^w{3}\.[a-z]{10}\.com

'''
abc…	Letters
123…	Digits
\d	Any Digit
\D	Any Non-digit character
.	Any Character
\.	Period
[abc]	Only a, b, or c
[^abc]	Not a, b, nor c
[a-z]	Characters a to z
[0-9]	Numbers 0 to 9
\w	Any Alphanumeric character
\W	Any Non-alphanumeric character
{m}	m Repetitions
{m,n}	m to n Repetitions
*	Zero or more repetitions
+	One or more repetitions
?	Optional character
\s	Any Whitespace
\S	Any Non-whitespace character
^…$	Starts and ends
(…)	Capture Group
(a(bc))	Capture Sub-group
(.*)	Capture all
(abc|def)	Matches abc or def
'''
