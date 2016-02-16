fname = raw_input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)
count = dict()
for line in handle:
    if line.startswith('From'):
        line.rstrip() 
        words = line.split()        
        if not words[0].startswith('From:'):            
            time = words[5]
            hour = time.split(":")[0]
            count[hour] = count.get(hour,0) + 1


for key, val in sorted(count.items()):
    print key, val

    
    

