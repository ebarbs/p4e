# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at
# the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

#going to use find to locate the : and len to build the index of the part of the string we want
#convert and print

print(float(text[text.find(':')+1:len(text)]))