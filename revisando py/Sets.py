#Sets{}
friends = ['John','Michael','Terry','Eric','Graham']
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends_set.intersection(my_friends_set)) #interseção
print(friends_set.difference(my_friends_set)) #Diferença de freinds_set de my_friends_set
print(friends_set.union(my_friends_set)) #união das sets