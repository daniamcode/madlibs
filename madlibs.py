print("My first program in Python")
color = 'red'
number = 3
print("Color is " + str(color) + " and number is " + str(number))
my_phrase = "This is a phrase to change into numbers in certain circumstances"

def translate(phrase):
    try:
        translation = ""
        for letter in phrase:
            if letter in "abc":
                translation = translation + str(8)
            else:
                translation = translation + letter
        return translation
    except Exception as error:
        print(error)

print(translate(my_phrase))