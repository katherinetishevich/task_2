from main import line_2

line_slice = line_2[::-1]
print(len(line_slice))
print(line_slice)

firstname = "Kate"
lastname = "Tishevich"
age = "22"
result = ('Привет,меня зовут' +  firstname  +  lastname  + ',мне' +  age + 'года')
print(result)

print('{} {}'.format('Hello','World'))
print(f"{'Hello'}{','}{'world'}")

a = [1,2,3]
a.insert(0, 5)
print(a)
b = [4,2,3]
b.append(5)
print(b)
a.extend(b)
print(a)

tuple = ('1','2')

print(list)

list = ['1','2']

print(tuple)

dict = { tuple : list }

print(dict)

dict_2 = { list : tuple }

print(dict_2)
