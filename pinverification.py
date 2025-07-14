def validate_pin(pin):
    # return true or false
    #num=["1","2","3","4","5","6","7","8","9","0"]
    num="1234567890"
    c=0
    if len(pin)==4 or len(pin)==6:
        for i in pin:
            if i in num:
                c+=1
        if c==4 or c==6:
            return True
        else:
            return False
    else:
        return False
pin=input("Enter a pin")
print(validate_pin(pin))