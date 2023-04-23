


#---------
#--- Tuple Methods-----
#----------


# Tuple With One Element


myTuple1 = ("Salar" ,)
myTuple2 = "Salar" ,

print(myTuple1) # Salar
print(myTuple2) # Salar

print(type(myTuple1)) # <class 'str'> # <class 'tuple'>
print(type(myTuple2)) # <class 'str'> # <class 'tuple'>

print(len(myTuple1)) # 1
print(len(myTuple2)) # 1


# Tuple Concatenation

a = (1,2,3,4)
b = (5,6,7)
c = a+b
d = a + ("A" , 9 , True) + b
print(c) # (1, 2, 3, 4, 5, 6, 7)
print(d) # (1, 2, 3, 4, 'A', 9, True, 5, 6, 7)


# Tuple , List , String Repeat (*)

myString = "Salar"
myList = [1,2]
myTuple = ("A" , "B")

print(myString * 6) # SalarSalarSalarSalarSalarSalar
print(myList * 6) # [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
print(myTuple * 6) # ('A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B')


# Methdos =>  Count()

a = (1,2,3,6,8,1,6,1)
print(a.count(1)) # 3


# Methods => Index()

b = (1,4,7,2,9,6)
# print( "The Position of The Index Is : " + b.index(9)) # 4 # Error can only concatenate str (not "int") to str
print( "The Position of The Index Is :{:d} ".format(b.index(9))) # The Position of The Index Is :4
print(f"The Position of The Index Is :{b.index(9)} ") # The Position of The Index Is :4


# Tuple Destruct

a = ("A" , "B" , 4 , "C")
# x, y, z = "A" , "B" ,"C"
# x , y , z = a
x , y , _ , z = a 
# print(x) # A
# print(y) # B 
# print(z) # C

# print(x) # A
# print(y) # B
# print(z) # C


print(x) # A
print(y) # B
print(z) # C