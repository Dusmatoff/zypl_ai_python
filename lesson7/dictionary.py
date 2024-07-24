thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
}

print(thisdict)
print(thisdict['brand'])
print(len(thisdict))

newdict = thisdict.copy()
newdict['newkey'] = 1234
print(thisdict)
print(newdict)
print(len(newdict))
newdict.clear()
print(newdict)
print(thisdict)

print("=======")
e = {a : a ** 2 for a in range(11)}
print("adad **2 => ", e)
du = {a : a * 2 for a in range(11)}
print("2 => ", du)
se = {a : a * 3 for a in range(11)}
print("3 => ", se)
