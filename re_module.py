import re

mail = 'shyam10kwd@gmail.com'

pattern = re.compile(r'[a-zA-Z0-9.]+@[a-z0-9]+.[a-z]+')

match = re.match(pattern,mail)
print(match.group())