import re 
count =0
matcher=re.finditer("[^0-9a-zA-Z]","a7b @ka 9Z")#[0-9a-zA-Z]
for match in matcher:
	print(match.start(),"...",match.group())

#0 ...a
#2 ...b

#sandeep=[abc]