def prime_check(integer):
    if integer < 2:  
        return False
    
    for n in range(2, integer):  
        if (integer % n) == 0:  
            return False
    
    return True
           
integer = int(input("Please enter an integer: "))

if prime_check(integer):
    print(integer, "is a prime number.")
else:
    print(integer, "is not a prime number.")
