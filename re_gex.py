'''
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regexs ####

[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

'''



# Important Links about re-gex:
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Regular-Expressions
# https://www.youtube.com/watch?v=K8L6KVGG-7o




import re
text_to_search = ''' abcasdfghjklpoiuytrewqzxcvbnm 
ASDFGHJKLPOUIYTREWQZXCVBNM 
123456789
+)_(*&^%$#@!~

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith

nahid@gmail.com
nghdshWsh@gmail.com
nghdshWsh@gmail.edu
ngh.dshWsh@gmail.edu
nghdsh-Wsh@pakija.edu
nghdsh-Wsh@pakija-mogo.edu
'''

sentence = "This is extremely important as refactors happen. As a library "

# pattern = re.compile(r'abc')
# matches = pattern.finditer(text_to_search)

#matches all the digit
# pattern = re.compile(r'\d')
# matches = pattern.finditer(text_to_search)

#matches all the digit, 3 digits at a time
# pattern = re.compile(r'\d\d\d')
# matches = pattern.finditer(text_to_search)

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu)')
matches = pattern.finditer(text_to_search)
# we can also use findall method what returns only the matched strings
# matches = pattern.findall(text_to_search)

pattern2 = re.compile(r'This')
match = pattern2.match(sentence)
print(match)

for match in matches:
    print(match)

urls = '''
https://www.programiz.com
http://realpython.com
https://github.com

'''
#we can find the sub texts from the results
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)
