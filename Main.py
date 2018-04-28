from random import randrange
from random import sample
from Funcitons import delay_print
#from Questions import Question_Tehran
from Questions import *

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


Question_index = 0
Answer_index = 1
AnswerA_index, AnswerB_index, AnswerC_index, AnswerD_index = 'A','B','C','D'
Correct_Answer_index = 2
Number_of_Cities = 6
Number_of_available_Questions_per_City = 4
Number_of_required_Questions_per_City = 3


City_Number = randrange(Number_of_Cities)
City_Number = 0

Question_Pol = sample(range(0,Number_of_available_Questions_per_City),Number_of_required_Questions_per_City)
print(' ')
print(' ')
print(' ')
print(' ')
for Question_Number in Question_Pol:
    print(' ')
    delay_print(Question_Total[City_Number][Question_Number][Question_index])
    delay_print("A-"+Question_Total[City_Number][Question_Number][Answer_index][AnswerA_index]+
                "\tB-"+Question_Total[City_Number][Question_Number][Answer_index][AnswerB_index]+
                "\tC-"+Question_Total[City_Number][Question_Number][Answer_index][AnswerC_index]+
                "\tD-"+Question_Total[City_Number][Question_Number][Answer_index][AnswerD_index])
    print(' ')
    answer = raw_input("Select Your Choice: ")
    if Question_Total[City_Number][Question_Number][Correct_Answer_index] == Question_Total[City_Number][Question_Number][Answer_index][answer.upper()]:
        print color.GREEN+"your answer is CORRECT:"+ u'\u2713'+color.END
    else:
        print color.RED+"your answer is WRONG  : X"+color.END
print(' ')
print(' ')
print(' ')
print(' ')
print(' ')
