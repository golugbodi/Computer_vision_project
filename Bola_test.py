import random
import cv2
from keras.models import load_model
import numpy as np

class CV:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        

    def get_computer_choice(self):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        return computer_choice


    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            print(prediction)
            max_position = np.argmax(prediction[0])  
            print(max_position)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break  
        return max_position
        # After the loop release the cap object
       # cap.release()
    # Destroy all the windows
       #cv2.destroyAllWindows()
                #return prediction_label 

    def get_user_choice(self):
        max_position = self.get_prediction()
        if max_position == 0:
            user_choice = 'rock'
        elif max_position == 1:
            user_choice = 'paper'
        elif max_position == 2:
            user_choice = 'scissors'
        else:
            user_choice = 'nothing'
        return user_choice

   

    def get_winner(self, computer_choice, user_choice):
            if user_choice == computer_choice:
                print(" ")
                print(f"Both players chose {user_choice}.") 
                #return "It's a tie."
                print("It's a tie")
                
            elif (computer_choice == "rock" and user_choice == "paper") or \
                (computer_choice == "paper" and user_choice == "scissors") or \
                (computer_choice == "scissors" and user_choice == "rock"):
                self.user_score += 1
                print(" ")
                print(f"You chose {user_choice} , and the computer {computer_choice}.")
                #return "You won! Congratulations!"
                print("You won! Congratulations!")
                
            else: 
                print()
                self.computer_score += 1
                print("You chose paper, and the computer chose rock.")
                print("You lost! Sorry!")

    def play(self):
        while self.user_score < 3 and self.computer_score < 3:
            computer_choice = self.get_computer_choice() 
            user_choice = self.get_user_choice() 
            self.get_winner(computer_choice, user_choice)
        if self.user_score == 3:
            print("You won!")
        else:
            print("You lost!")            



cv_game = CV() # creating an instance of the class 
#print(cv_game.computer_score)
cv_game.play()
#print(cv_game.get_computer_choice())
#cv_game.get_prediction()
