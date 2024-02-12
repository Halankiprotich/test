#Question 3: Power of Two 
#Write a program that takes an integer as input and returns true if the input is a power of two. 
 
#Examples:  
#8=> returns true 
#6=> returns false 


def is_power_of_two(number):
    if number <= 0:
        return False
    while number > 1:
        if number %2 !=0:
            return False
        number=number/2
    return True
print(is_power_of_two(16))
print(is_power_of_two(9))

        
