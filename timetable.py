import pdb
#timetables - 1 to 20 time table and choose from 1 up to second input value
done = False
number1 = 0
number2 = 0
firstnumber = False
secondnumber = False
bothnumbers = False
while done is False :
    #this loop ends the program
    while bothnumbers is False:
        #this loop stays false until both inputs are validated and verified
        while firstnumber is False:
            #this loop stays false until the first input has been validated and verified
            user_input = input("Enter your timetable value between 1 and 20:")
            try: 
                number1 = int(user_input)
                #try loop checks whether input can be converted into integer or not
                if number1 < 1 or number1 > 20:
                    print("not in range")
                elif number1 > 0 and number1 < 21:
                    print("yes in range")
                    print("Are you sure you want to input", str(number1)+"?", "(Y/N):")
                    userchoice = input()
                    if userchoice == "Y":
                        firstnumber = True
                    elif userchoice == "N":
                        raise ValueError
                        #this sends the person to re-enter the first number
                    else:
                        raise TypeError
                        # this input also makes the person re-enter the number
                    #endif
            except (TypeError, ValueError):
                print("Please input an integer again.")
            
            #endtry
        #endwhile
        while secondnumber is False:
            #this loop stays false until the second input is validated and verified
            user_input = input("Enter the number of times your first number multiplies by between 1 and 20:")
            try:
                number2 = int(user_input)
                #try loop checks whether input can be converted into integer or not
                if number2 < 1 or number2 > 20:
                    print("not in range")
                elif number2 > 0 and number2 < 21:
                    print("yes in range")
                    print("Are you sure you want to input", str(number2)+"?", "(Y/N):")
                    userchoice = input()
                    if userchoice == "Y":
                        secondnumber = True
                    elif userchoice == "N":
                        raise ValueError
                        #this sends the person to re-enter the second number
                    else:
                        raise TypeError
                        # this input also makes the person re-enter the number
                    #endif
            except (TypeError, ValueError):
                        print("Please input an integer again.")
            #endtry
        #endwhile
        bothnumbers = True
        #once both nummbers are correct, the while loop ends
    #endwhile
    #this for loop prints all the numbers specified before the end of the program.
    for count in range(1,number2+1):
        print(number1 * count)
    next
    done = True    
#endwhile    
        
