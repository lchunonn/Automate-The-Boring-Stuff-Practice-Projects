import re
import os
open('test.txt', 'w').write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
f = open('test.txt')
text = f.read()
madlib_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
matches = madlib_regex.findall(text)

for match in matches:
    if match[0].lower() in ['a','e','i','o','u']:
        replacement = input(f"Enter an {match}: ")
    else:
        replacement = input(f"Enter a {match}: ")
    text = text.replace(match, replacement,1)

print(text)

new_f = open('newtest.txt', 'w')
new_f.write(text)
f.close()
new_f.close()
