def play_again():
    answ = raw_input("Do you want to play again (Y or N)? ")
    if answ == "Y":
        return True
    elif answ == "N":
        return False
    else:
        print "Invalid input"
        play_again()
play_again()
