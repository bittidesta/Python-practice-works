## Find 0.8475 in the string 'text' and convert it to float. 
text = "X-DSPAM-Confidence:    0.8475";
in1 = text.find("0");
inlast = float(text[in1:]);
print inlast;
