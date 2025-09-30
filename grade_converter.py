# FILE NAME - grade_converter.py

# NAME: Michael Glazier
# DATE: 09/30/2025
# BRIEF DESCRIPTION:  return Letter Grade for a numerical grade

########## ENTER YER CODE BELOW THIS LINE ##########

def main():

   print("===== Grade Converter =====")
   numerical_grade = int(input("Enter a numerical grade (1-100): "))

   if numerical_grade > 100:
      print("A+")
   
   elif 90 <= numerical_grade <= 100:
      print("A")

   elif 80 <= numerical_grade < 90:
      print("B")
   
   elif 70 <= numerical_grade < 80:
      print("C")

   elif 65 <= numerical_grade < 70:
      print("D")

   else:
      print("F")

main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

I'd tell them to look out for the start and end of ranges to make sure correct letter is being included when on a boundary

'''