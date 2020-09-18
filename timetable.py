import pdb
#timetables - 1 to 20 time table and choose from 1 up to second input value
done = False
number1 = 0
number2 = 0
bothnumbers = False
while done is False :
    while bothnumbers is False :
        user_input = input("Enter your timetable value between 1 and 20:")
        try: 
            number1 = int(user_input)
            print("yes")
            if number1 < 1 or number1 > 20:
                print("not in range")
            elif number1 > 0 and number1 < 21:
                print("yes in range")
        except (TypeError, ValueError):
            print("not an integer")
        
         


        

       
        
        #endif