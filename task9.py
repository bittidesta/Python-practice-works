fname = raw_input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)
senders = dict()
for line in handle:
    if line.startswith('From'):
        line.rstrip() 
        words = line.split()        
        if not words[0].startswith('From:'):            
            email = words[1]            
            senders[email] = senders.get(email,0) + 1

Hsender = None
Hoccure = None          
for sender,occure in senders.items():
    if Hoccure is None or occure > Hoccure:
        Hoccure = occure
        Hsender = sender
print Hsender,Hoccure
    
    

