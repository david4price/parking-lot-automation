import time


def startmessage():
    time.sleep(0.1)

    welcome = "\nHello,\nWelcome to our parking lot\n\n"

    for character in welcome:
        print(character, end="", flush=True)
        time.sleep(0.05)


def choice():
    choices = "\nPlease choose ONE of the following\n1) Entering \n2) Exiting \n3) Check entrance time \n4) Forgot " \
              "your keycode\n "

    for character in choices:
        print(character, end="", flush=True)
        time.sleep(0.05)


def choice2():
    choices = "Sorry, we are full at the moment\n\nPlease choose ONE of the following\n1) Exiting \n2) Check entrance " \
              "time \n3) Forgot your keycode\n "

    for character in choices:
        print(character, end="", flush=True)
        time.sleep(0.05)


def admin_choice():
    adminchoice = "\nWelcome to the DARK SIDE\n1) Set parking spots \n2) Set base price \n3) Reset \n4) Print all " \
                  "cars \n5) Return to menu "

    for character in adminchoice:
        print(character, end="", flush=True)
        time.sleep(0.05)
