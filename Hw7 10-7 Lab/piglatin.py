import re 


piglatin = re.compile("([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([AEIOUaeiou])(\w*)")

pattern = "([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([AEIOUaeiou])(\w*)"

inpt = "Happy"

# if re.match(pattern, inpt):
#     print(piglatin.sub(r"\2\3\1ay", inpt))
    # print("It matches!")


constantvowel = "([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([AEIOUaeiou])(\w*)"
constantconstant = "([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])([BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz])(\w*)"
vowel = "([AEIOUaeiou])(\w*)"

cc_regex = re.compile(constantconstant, re.VERBOSE)
cv_regex = re.compile(constantvowel, re.VERBOSE)
v_regex = re.compile(vowel, re.VERBOSE)

inpt = "awesome"
if re.match(constantconstant, inpt):
    print(cc_regex.sub(r"\3\1\2ay", inpt))
elif re.match(constantvowel, inpt):
    print(cv_regex.sub(r"\2\3\1ay", inpt))
elif re.match(vowel, inpt):
    print(v_regex.sub(inpt + "way",inpt))
