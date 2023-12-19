import re 

# pattern=re.compile("ab")
# matcher=pattern.finditer("abaabababbab")
count =0
matcher=re.finditer("ab","abaabababbab")
for match in matcher:
	count+=1
	print(match.start(),"....",match.end(),"...",match.group())
print(count)

# 0 2 ab
# 3 5 ab
# 5 7 ab
#7 9  ab
#10 12 ab