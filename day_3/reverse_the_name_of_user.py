'''name=input("Enter your name:\n")
print(f"You ane in reverse order is: {name [-1::-1]}")
name= "Bibek shrestha"
print(name.count("s"))'''
name,charr= input("Enter your name and a character separated by ,:\n").split(",")
print (f"The length of your name is:\n{len(name)}")
newj= charr.upper()
new= name +charr
new2= new.upper()
n= new2.count(newj)
print(f"The no of {charr} is {n} ")