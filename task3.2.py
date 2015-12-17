try:
    score = raw_input("Enter score:")
    s = float(score) 
except:
    print "Error, please enter numeric value."
    exit()
if s < 0.0 or s > 1.0 :
    print "Please enter value between 0.0 and 1.0"
    exit()
elif s < 0.6 :
    print "F"
elif s >= 0.6 and s < 0.7:
    print "D"
elif s >= 0.7 and s < 0.8:
    print "C"
elif s >= 0.8 and s < 0.9 :
    print "B"
elif s >= 0.9 :
    print "A"
