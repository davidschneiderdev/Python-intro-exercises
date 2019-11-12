count = 0
input_string = input("How high should we count? ")
# try to run a block of code
try:
    MAX = int(input_string)
    while (count < MAX):
        is_odd = count % 2 != 0
        if is_odd:
            print(count)        
        count += 1    
# if there's an error, print a message for the user.
except ValueError:
    print("Please run the program again and type a number!")