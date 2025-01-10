import os

# Text Formatting to make a nice looking interface
class TxFormat:
    none: str = '\033[0m'
    bold: str = '\033[1m'
    red: str = '\033[91m'
    yellow: str = '\033[93m'
    green: str = '\033[92m'
    blue: str = '\033[94m'
    purple: str = '\033[95m'

# Function to print the program header
def consoleHeader(txt: str) -> None:
    print(f"\n{TxFormat.bold}{TxFormat.purple}{txt.center(os.get_terminal_size().columns, '-')}{TxFormat.none}\n")

# Function to clear the console
def consoleClear() -> None:
    os.system('cls')
    
# Function that deals with showing the question to the user and taking and processing the user input
def askQuestion(question: str) -> float:
    while True:
        try:
            answer: int = int(input(f"{TxFormat.bold}{question}{TxFormat.none} Answer on a scale from 0 (Never / Not at all) to 4 (Always / A lot) :  "))
            if answer == 0:
                return 0.0
            elif answer >= 1 and answer <= 4:
                return float((answer/4)/1)
            else:
                print(f"{TxFormat.red}Please enter a number from 0 to 4! {answer} is not a valid answer!{TxFormat.none}")
        except ValueError:
             print(f"{TxFormat.red}Please enter a number from 0 to 4! {answer} is not a valid answer!{TxFormat.none}") 

# Function that will take the result of 2 opposing questions and the MBTI types that match the result of those questions, and returns the letter that matches the user
def decideLetter(result_question_1: float, result_question_2: float, question_1_high_letter: str, question_2_high_letter: str) -> str:
    if result_question_1 - result_question_2 > 0:
        return question_1_high_letter
    else:
        return question_2_high_letter

# Print Header
consoleClear()
consoleHeader("  MBTI Test by Iggy  ")

# Ask the questions and save the results
ei_question_1: float = askQuestion("How often do you prefer quiet time alone over being around others?") # Higher score = I
print()
sn_question_1: float = askQuestion("How often do you focus on details and facts when making decisions or solving problems?") # Higher score = S
print()
ft_question_1: float = askQuestion("How often do you prioritize logic and objective analysis when making decisions?") # Higher score = T
print()
pj_question_1: float = askQuestion("How important is having a detailed plan or schedule before starting something?") # Higher score = J
print()

ei_question_2: float = askQuestion("How energized do you feel after spending time in a group of people?") # Higher score = E
print()
sn_question_2: float = askQuestion("How much do you focus on possibilities, abstract ideas, and imagining what could be?") # Higher score = N
print()
ft_question_2: float = askQuestion("How often do you prioritize the impact of your decisions on people's feelings and relationships?") # Higher score = F
print()
pj_question_2: float = askQuestion("How much do you like to keep your options open and make decisions spontaneously") # Higher score = P
print()

# Get the MBIT type and print it
mbti_type: str = f"{decideLetter(ei_question_1, ei_question_2, 'I', 'E')}{decideLetter(sn_question_1, sn_question_2, 'S', 'N')}{decideLetter(ft_question_1, ft_question_2, 'T', 'F')}{decideLetter(pj_question_1, pj_question_2, 'J', 'P')}"
print(f"Your MBTI type is: {TxFormat.bold}{mbti_type}{TxFormat.none}")

