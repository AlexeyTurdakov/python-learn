print('------------lesson2------Списки--------')

name = 'irbis'

names = ['1', 1, name]

print(f'{names[2].title()} {names[-3]}')

names[1] = 2

names.append(10)
names.append('100')
names.insert(1, '1000')
del names[0]
pop_method = names.pop(2)
names.remove(2)
names.remove('100')
print(names)
print(pop_method)

gosts = ['egy', 'rog']

#deleteGosts = gosts.pop(0)
#print(gosts, deleteGosts)

gosts.sort()
gosts.sort(reverse=True)

print(gosts)

#Временная сортировка списка функцией sorted()



