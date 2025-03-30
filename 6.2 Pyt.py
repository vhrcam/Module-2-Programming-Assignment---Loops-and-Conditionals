guess_me = 7
number = 1

while number <= guess_me:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    number += 1
else:
    print("oops")
