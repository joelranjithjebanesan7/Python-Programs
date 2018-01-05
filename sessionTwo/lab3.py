def is_vowel(letter) :
    
    if letter in('a','e','i','o','u','A','E','I','O','U'):
    
        return True
    
    else:
        
        return False


letter=input("enter the alphabet:")
print(is_vowel(letter))