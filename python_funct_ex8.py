def play_again():
    answ = raw_input("Do you want to play again (Y or N)? ")
    if answ == "Y":
        return True
    else:
        return False

play_again()
