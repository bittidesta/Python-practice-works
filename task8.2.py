fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
except:
    fname = "mbox-short.txt"
    fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From'):
        line.rstrip()
        words = line.split()
        if not words[0].startswith('From:'):
            email = words[1]
            print email
            count += 1

print "There were", count, "lines in the file with From as the first word"
