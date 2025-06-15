# python 

print("hello world")

x="Aun"
y='Aun'
print ("hello from " + x)
print ("hello from " + y)
print("hello from {}".format(x))

a=50
print("hello from " + str(a))

import random


num=random.randint(1,100)
print(num)

num2=random.randrange(1,100,2)
print(num2)



txt="My name is Aun"

if "Aun" in txt:
    print("yes, 'Aun' is present in the text")




for i in range(len(txt)):
    print(txt[i], end=" ")

print("\n")

## negative slicing 

print (txt[-5:-1])
print("\n")
print (txt[-10:])
print (txt[:-5])

print (txt[-5:-1:1])

# SPLIT


print (txt.split(" "))


#formatstrings


print(f"hello from {x} and {y} and {10%2:d} and {10/3:.2f} and {10/3:.3f} and {10/3:.4f}")

print(txt.center(50, '*'))


x=10
y=10

if x is y:
  print(x//y)