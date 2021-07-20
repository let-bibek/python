'''def Chk():
     a= int(input("Enter a number:\n"))
     b=int(input("Enter the another number:\n"))
     if a>b:
         return(a)
     else:
          return(b)
c=Chk()
print("The greatest number is:",c)    '''

#check the palindrome:  

s=input("Enter your name:\n")
s=s.lower()
def is_palindrome(str):


    c=str[-1::-1]
    if s==c:
                return True
    else:
            return False

print(is_palindrome(s))

#Fibonacci series 
 def Fibonacci(n):




