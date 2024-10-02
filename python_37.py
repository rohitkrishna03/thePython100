    # # write a python program to translate a message into secret code language.
    # use the rules below to translate normal english into secret code language

    # coding
    # if the word contains atleast 3 characters, remove the first letter and append it at the end.
    # now append three random characters at the starting and the end
    # else: simply reverse the string

    # decoding:
    # if the word containes less than 3 characters, reverse it 
    # else:
    # remove 3 random characters from start and end. now remove the latest letter and appendit to the beginning.

st = input("enter message")
words = st.split(" ")
coding = True
if(coding):
    nwords =[]
    for word in words:
     if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
     stnew = r1+word[1:] + word[0] +r2
    nwords.append(stnew)
else:
    nwords.append(word[::-1])
    print(" ".join(nwords))

else:
     nwords =[]
    for word in words:
    if(len(word)>=3):
        stnew = word[3:-3]
        stnew = stnew[-1] + stnew[:-1]
        nwords.append(stnew)
    else:
        nwords.append(words[::-1])
    print(" ".join(nwords))

