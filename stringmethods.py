def disemvowel(string_):
    string1=string_
    vo=["a","e","o","i",'u']
    for i in string_:
        if i.lower() in vo:
            string1=string1.replace(i,"")
    return string1
string_=input("Enter a string")
string1=disemvowel(string_)
print(string1)