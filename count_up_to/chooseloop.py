
still_playing = True

while still_playing:
    try:
        users_number = int(input("Please type in a number: "))
        if users_number > 3:
            print("too high")
        elif users_number == 3:
            print("you guessed correctly")
            still_playing = False
        else:
            print("too low")
    except ValueError:
        print("Please enter a number in.")
    

