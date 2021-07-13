def new_game():
    guesses = [] ##list of guess respond by the player
    correct_guesses = 0 #sum correct answer
    question_num = 0 #loop question

    for key in question: #loop questions
        print("----------------------------")
        print(key)
        for i in options[question_num]: #nested loop for the question options
            print(i)
        guess = input("Enter (A,B,C, or D): ")
        guess = guess.upper()
        guesses.append(guess) # append the choices in th list of guess

        correct_guesses += check_answer(question.get(key),guess) #verify the answers and return 0 or 1
        question_num += 1

    display_score(correct_guesses, guesses)

#########################3
def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0
########################
def display_score(correct_guesses, guesses):
    print("-----------------")
    print("RESULTS")
    print("-----------------")
    print("Answers: ",end=" ")
    for i in question: #display the answers
        print(question.get(i),end=" ")
    print()
    for i in guesses: #display the choices by the player
        print(i,end=" ")
    print()

    score = int((correct_guesses/len(question))*100)
    print("Your score is: "+str(score)+"%")

################3
def play_again():

   response = input("Do you want to play again? (yes/no) ")
   response = response.upper()

   if response == "YES":
       return True
   else:
       return False

question = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group: ": "C",
    "Is the Earth round?: ": "A",
}#dictionary of questions
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]] #list of lists the answers

new_game()

while play_again():
    new_game()
print("Byee!")