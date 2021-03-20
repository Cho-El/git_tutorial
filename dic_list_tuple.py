station = ["사당", "신도림", "인천공항"]
list = ['사당', '신도림', "인천공항"]

print(station[1])
print(list[2])
print(list)
del list[1]
print(list)
list2 = list *2
list3 = list , "니은"
print(list2)
print(list3)
print(list3[0][1])
dict = {'a' : '0', 'b' : '123','c' : 3}
print(dict['a'])
print(dict['b']+str(3))
dict['abc'] = 2
print(dict)
genre = [{'id':1, 'name':'Animation'}, {'id': 2, 'name':'Comedy'}]
print(genre)
print(genre[1])
genre_list = []
for g in genre:
    print(g)
    print(g['id'])
    print(g['name'])
    genre_list.append(g['name'])

print(genre_list)

# practice
games = ["lol", "star", "sing", "read"]
foods = ['pizza','corn','clam', 'fish']
favorites = games + foods
print(favorites)

name = "성윤"
first = "조"
num = 1
placeholder = "Hi there " + name + first + "!"
print("Hi there %s %s %d!" % (first, name, num))
print(placeholder)