# "hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# # " s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]

# def wave(people):
#     # Code here
#     a=people.upper()
#     lst=[]
#     for i in range(len(people)):
#          if people[i] != ' ':
#             b=people.replace(people[i],a[i])
#             lst.append(b)
#     return lst
def wave(people):
    result = []

    for i in range(len(people)):
        if people[i] != ' ':
            result.append(people[:i] + people[i].upper() + people[i+1:])

    return result