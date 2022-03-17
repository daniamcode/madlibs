# We want to write a paragraph with blank spaces that will be variables

# #3 possible ways
# color = "red"
# print("My favourite color is " + color)
# print("My favourite color is {}".format(color))
# #recommended way to go with string concatenation
# print(f"My favourite color is {color}")

sport = input("Tell me a sport: ")
verb = input("Now a verb: ")
name = input("Write a name: ")
advice = input("What's your favourite advice?: ")

madlib=f"Today I watched a {sport} game on TV and after \
that I went to the street to {verb} and \nI met \
{name} who told me: {advice}"

print(madlib)
