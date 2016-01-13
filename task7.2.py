fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    print 'File can not be found'
    exit()
entry = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue    
    line = line.rstrip()
    line = line[20:]
    line = float(line)
    entry = entry + 1
    total = total + line
    
average = float(total/entry)
print average
