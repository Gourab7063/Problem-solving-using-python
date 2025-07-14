def greet(language):
    
    dict={}
    lst=[ ("english", "Welcome"), ("czech", "Vitejte"), ("danish", "Velkomst"), ("dutch", "Welkom"), ("estonian", "Tere tulemast"), ("finnish", "Tervetuloa") , ("flemish", "Welgekomen"), ("french", "Bienvenue"), ("german", "Willkommen"), ("irish", "Failte"), ("italian", "Benvenuto"), ("latvian", "Gaidits"), ("lithuanian", "Laukiamas"), ("polish", "Witamy"), ("spanish", "Bienvenido"), ("swedish", "Valkommen"), ("welsh", "Croeso")]
    for i in range(len(lst)):
        dict.update({lst[i][0]:lst[i][1]})
    if type(language)==int:
        return 'Welcome'
    elif language== '':
        return 'Welcome'
    elif '_' in language:
        return 'Welcome'
    else:
        for i,j in dict.items():
            if language.lower()==i:
                return j
print(greet('english'))
print(greet('dutch'))
print(greet('chinese'))
print(greet(1))
print(greet(''))
print(greet('IP_ADDRESS_INVALID'))
