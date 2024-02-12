#Question 4: Capitalize Words 
#Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string. 
#Examples:  
 
#"hi"=> returns "Hi" 
#"i love programming"=> returns "I Love Programming" 


def capitalisation_of_words(sentence):
    words = sentence.split()
    capitalized_sentence = ""
    for word in words:
        capitalized_word = word[0].upper() + word[1:]
        capitalized_sentence += capitalized_word + " "
    
    return capitalized_sentence.strip()

input_sentence = "i love programming"
capitalized = capitalisation_of_words(input_sentence)
print(capitalized)
