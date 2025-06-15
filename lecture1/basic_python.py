list = list((1,2,3))
print(list)

list.append(4)
print(list)

list.insert(0, 0)
print( list)

list.remove(2)
print(list)

list2=[2,4,5]

list.extend(list2)

print(list)


t1=tuple(((1,2,3),(4,5,6)))
print(t1)

print(t1.count(1))


s1=set((1,2,3,4,5,6))
print(s1)

s1.clear()
print(s1)

s1.update((1,1,2,3,4,5,6))
print(s1)

s1=s1.union(set((7,8,9)))
print(s1)


dic={
    "name": "Aun",
    "age": 25,
    "city": "Karachi"
}
print(dic["age"])

dic={}

dic={"ahmed":"1" , "ali": "2"}
print(dic["ali"])



for i in range(1,10):
    for j in range(1,10):
        print("*",end=" ")
    
    print("\n")


for i in range (2):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}", end=" ")
        print ("\n") 