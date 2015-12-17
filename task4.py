def computepay(h,r):
    if h <= 40:
        return h * r
    else:
        return ((40 * r) + ((h - 40) * (r * 1.5)))
try:
    hrs = raw_input("Enter Hour:")
    rate = raw_input("Enter Rate:")
    h = float(hrs)
    r = float(rate)
except:
    print "Error enter numeric value for h and r"
    exit()
p = computepay(h,r)
print p

