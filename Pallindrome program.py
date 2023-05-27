def is_palindrome(word):
    # Convert the word to lowercase and remove any spaces
    word = word.lower().replace(" ", "")

    # Check if the reversed word is the same as the original word
    if word == word[::-1]:
        return True
    else:
        return False

# Test the function
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")