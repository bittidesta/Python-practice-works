fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File can not be found'
    exit()
lst = list()
for line in fh:
    line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print lst
