import re
fname = raw_input("Enter file name: ")
if len(fname) < 1: fname = "regex-sum.txt"
b = open(fname)
nums =(re.findall('[0-9]+', b.read()))
print sum(map(int,nums))
