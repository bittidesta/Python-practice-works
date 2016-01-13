fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File can not be found'
    exit()
for line in fh:
    line = line.rstrip()
    print line.upper()
