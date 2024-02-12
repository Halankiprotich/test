#Question 2: Fibonacci Sequence 
#Write a program to generate the Fibonacci sequence up to 100. 

def fibonacci_sequence(n):
    sequence=[0, 1]
    while sequence[-1]< n:
        next_number = sequence[-1] + sequence [-2]
        if next_number > n:
          break
        sequence.append(next_number)
    return sequence
fibo_sequence = fibonacci_sequence(100)
print(fibo_sequence)
    
