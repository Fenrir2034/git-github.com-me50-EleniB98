def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ''.join(char for char in text if char not in vowels)
    return result

if __name__ == "__main__":
    user_input = input("Enter a string of text: ")
    result_text = remove_vowels(user_input)
    print(result_text)
