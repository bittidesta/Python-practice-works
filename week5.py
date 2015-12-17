# py
try:
        
        hrs = raw_input("EnterHour:")
        h = float(hrs)
        rate = raw_input("EnterRate:")
        r = float(rate)
        print r, h
        if h <= 40:
                print h * r
        elif h > 40:
                print ((40 * r) + ((h - 40) * (r * 1.5)))
except:
        print "Error, please enter numeric input" 
