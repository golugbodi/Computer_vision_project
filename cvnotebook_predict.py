import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

#Define label classes
def my_labels():
    labels = {}
    dict_list = list(labels.values())
    classes = dict_list
    with open("labels.txt", "r") as label:
        text = label.read()
        lines = text.split("\n")
        #print (text)
        #print(lines)
        for line in lines[0:]:
            hold = line.split(" ",1)
            #print(hold)
            #print(hold[1])
            #print(hold[1])
            labels[hold[0]]= hold[1]
            #mydict=labels.append(line)
            #print(classes)
            #print(labels)
    dict_list = list(labels.values())
    classes = dict_list
    #print("I am inside the label function")
    return classes


#Get prediction from webcam
def get_prediction ():
    
    while True: 
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        #print(prediction)
        classes = my_labels()
        max_Position = np.argmax(prediction)  
        prediction_label = classes[max_Position]
        #print(prediction_label)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  
    # After the loop release the cap object
    cap.release()
# Destroy all the windows
    cv2.destroyAllWindows()
            #return prediction_label 


#Input webcam image as user choice and play game
import random

options = ["Rock", "Paper", "Scissors"]


def get_computer_choice():
    computer_choice = random.choice(options)
    #print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.")
    #print(f"The computer chose {computer_choice}.")
    return computer_choice

def get_user_choice():
    #user_choice = input("Enter rock, paper or scissors: ").lower()
    user_choice = get_prediction ()
    #if user_choice in options:
    return user_choice
    #else:
        #print("Invalid. Please try again.")

#user_choice = get_user_choice()
#computer_choice = get_computer_choice()
    
def get_winner(computer_choice, user_choice):
    while True:
        if user_choice == computer_choice:
            print(" ")
            print(f"Both players chose {user_choice}.") 
            #return "It's a tie."
            print("It's a tie")
            
        elif computer_choice == "rock" and user_choice == "paper":
            print(" ")
            print("You chose paper, and the computer chose rock.")
            #return "You won! Congratulations!"
            print("You won! Congratulations!")
            
        elif computer_choice == "rock" and user_choice == "scissors":
            print(" ")
            print("You chose scissors, and the computer chose rock.")
            #return "You lost! Sorry!"
            print("You lost! Sorry!")
            
        elif computer_choice == "paper" and user_choice == "scissors":
            print(" ")
            print("You chose scissors, and the computer chose paper.") 
            print("You won! Congratulations!")
            
        elif computer_choice == "paper" and user_choice == "rock":
            print(" ") 
            print("You chose rock, and the computer chose paper.") 
            print("You lost! Sorry!")
                
        elif computer_choice == "scissors" and user_choice == "rock":
            print(" ")
            print("You chose rock, and the computer chose scissors.")
            #return "You win! Congratulations!"
            print("You won! Congratulations!")
            
        elif computer_choice == "scissors" and user_choice == "paper":
            print(" ")
            print("You chose paper, and the computer chose scissors.")
            #return "You lost! Sorry!"
            print("You lost! Sorry!")
            
def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    get_winner(computer_choice, user_choice)

play()
