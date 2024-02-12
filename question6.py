#Question 6: Count Vowels 
#Write a program that counts the number of vowels in a sentence. 
 
#eg " Hello World " => returns 2 


def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count

input_sentence = "Hello world"
vowel_count = count_vowels(input_sentence)
print(vowel_count)
