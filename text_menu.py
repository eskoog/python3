user_input = input("Please press p to continue.  If you are done, please press q: ")
while user_input == "p" or "q":
    if user_input == "p":
        print("Hello")
        user_input = input("Please press p to continue.  If you are done, please press q: ")
    elif user_input == "q":
        print("Terminating.")
        break
    else:
        print("You did not enter p or q.")
        user_input = input("Please press p to continue.  If you are done, please press q: ")