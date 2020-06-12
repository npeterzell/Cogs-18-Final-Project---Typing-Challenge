# Importing modules
import time
import threading

# Function for what the program should do if time runs out on easy difficulty,
# that lets the user type anything into an input box to retry
def time_up_easy():
    print("Time's up! Type anything here to give it another shot.")
    try_again = input("Type here:")
    easy()

# Function for what the program should do if time runs out on medium difficulty,
# that lets the user type anything into an input box to retry
def time_up_medium():
    print("Time's up! Type anything here to give it another shot.")
    try_again = input("Type here:")
    medium()
    
# Function for what the program should do if time runs out on hard difficulty,
# that lets the user type anything into an input box to retry
def time_up_hard():
    print("Time's up! Type anything here to give it another shot.")
    try_again = input("Type here:")
    hard()
    
# Function for what the program should do if time runs out on insane difficulty,
# that lets the user type anything into an input box to retry
def time_up_insane():
    print("Time's up! Type anything here to give it another shot.")
    try_again = input("Type here:")
    insane()
    
# Function that lets the user choose which difficulty they want with an input
# box, that has the user type the difficulty the want into the box
def difficulty_choice():
    user_choose = input("Type here:")
    if user_choose == "easy":
        easy()
    if user_choose == "medium":
        medium()
    if user_choose == "hard":
        hard()
    if user_choose == "insane":
        insane()
        
# Function that gives some introductory text with pauses in between lines,
# then calls the function to choose difficulty
def start():
    print("Welcome to the typing challenge!")
    time.sleep(3)
    print("There are 4 difficulty levels: easy, medium, hard, and insane.")
    time.sleep(3)
    print("You will have 15 seconds to type 10 words.")
    print("Type the difficulty you want to start with:")
    difficulty_choice()

# Function that runs the easy typing challenge
def easy():
    # Printing out a countdown timer with pauses in between counts
    print("All right! Get ready...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    
    # defines what the user should type and prints it out for them to see,
    # then starts a 15 second timer and gives them a box to type in
    correct_type = "dog bog hog log hey fey key lag wag tag"
    print(correct_type)
    typing_timer = threading.Timer(15.0, time_up_easy)
    typing_timer.start()
    user_type = input("Type here:")

    # If the user typed the words right, they get this message. The timer is
    # also stopped and defined as None so it can be started again without a
    # runtime error. The difficulty choice function is called to let the user
    # choose the next challenge.
    if user_type == correct_type:
        print("You did it! Good Job! If you want to try another difficulty, type it here:")
        typing_timer.cancel()
        typing_timer = None
        difficulty_choice()
    
    # If the user made a mistake, they get this message and the timer is cancelled
    # and set to None so it can be started again without a runtime error. They
    # can then type anything to restart that difficulty.
    else:
        
        print("Not quite right! Type anything here to give it another shot.")
        typing_timer.cancel()
        typing_timer = None
        try_again = input("Type here:")
        easy()
        
# Function that runs the medium typing challenge
def medium():
    # Printing out a countdown timer with pauses in between counts
    print("All right! Get ready...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    
    # defines what the user should type and prints it out for them to see,
    # then starts a 15 second timer and gives them a box to type in
    correct_type = "know show throw help whelp yelp kelp wine dine mine"
    print(correct_type)
    typing_timer = threading.Timer(15.0, time_up_medium)
    typing_timer.start()
    user_type = input("Type here:")

    # If the user typed the words right, they get this message. The timer is
    # also stopped and defined as None so it can be started again without a
    # runtime error. The difficulty choice function is called to let the user
    # choose the next challenge.
    if user_type == correct_type:
        print("You did it! Good Job! If you want to try another difficulty, type it here:")
        typing_timer.cancel()
        typing_timer = None
        difficulty_choice()
        
    # If the user made a mistake, they get this message and the timer is cancelled
    # and set to None so it can be started again without a runtime error. They
    # can then type anything to restart that difficulty.
    else:
        
        print("Not quite right! Type anything here to give it another shot.")
        typing_timer.cancel()
        typing_timer = None
        try_again = input("Type here:")
        medium()

# Function that runs the hard typing challenge
def hard():
    # Printing out a countdown timer with pauses in between counts
    print("All right! Get ready...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    
    # defines what the user should type and prints it out for them to see,
    # then starts a 15 second timer and gives them a box to type in
    correct_type = "thrive jive entomb canteen sheen seize threes knees pantry banter"
    print(correct_type)
    typing_timer = threading.Timer(15.0, time_up_hard)
    typing_timer.start()
    user_type = input("Type here:")

    # If the user typed the words right, they get this message. The timer is
    # also stopped and defined as None so it can be started again without a
    # runtime error. The difficulty choice function is called to let the user
    # choose the next challenge.
    if user_type == correct_type:
        print("You did it! Good Job! If you want to try another difficulty, type it here:")
        typing_timer.cancel()
        typing_timer = None
        difficulty_choice()
    # If the user made a mistake, they get this message and the timer is cancelled
    # and set to None so it can be started again without a runtime error. They
    # can then type anything to restart that difficulty.    
    else:
        
        print("Not quite right! Type anything here to give it another shot.")
        typing_timer.cancel()
        typing_timer = None
        try_again = input("Type here:")
        hard()

# Function that runs the insane typing challenge
def insane():
    # Printing out a countdown timer with pauses in between counts
    print("All right! Get ready...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO!")
    
    # defines what the user should type and prints it out for them to see,
    # then starts a 15 second timer and gives them a box to type in
    correct_type = "unnatural celestial unwanted seizure caesar believer galactic pontoon\ntectonic interrelated"
    print(correct_type)
    typing_timer = threading.Timer(15.0, time_up_insane)
    typing_timer.start()
    user_type = input("Type here:")

    # If the user typed the words right, they get this message. The timer is
    # also stopped and defined as None so it can be started again without a
    # runtime error. The difficulty choice function is called to let the user
    # choose the next challenge.
    if user_type == correct_type:
        print("You did it! Good Job! If you want to try another difficulty, type it here:")
        typing_timer.cancel()
        typing_timer = None
        difficulty_choice()
        
    # If the user made a mistake, they get this message and the timer is cancelled
    # and set to None so it can be started again without a runtime error. They
    # can then type anything to restart that difficulty.
    else:
        
        print("Not quite right! Type anything here to give it another shot.")
        typing_timer.cancel()
        typing_timer = None
        try_again = input("Type here:")
        insane()