#applying the input function
import time
User_input= input("what is your name?\n")
# applying the output function
print (User_input)
# creting the varriable 
num_candidates=3
winning_percent=73.81
candidate=User_input
won_election=True
tally_local_warewolves=10
warewolf_name="Ayush"
is_warewolf=False
print(candidate)
print(winning_percent)
user_howl = float(input("Please input float of 0 or greater. ")) # converts whatever passed to it into an integer.
print(user_howl) #python treats all the user input as a strings untill it is specified
#comparing the statement
if user_howl>0:
    print("you are the good guy...")
    # for the if else condition statement
    temprature=int(input("enter the temprature in integer...\n"))
    if temprature>80:
        print("open AC")
    else:
        print("open the heater")

# for nested if/else statement
grades=int(input("enter the grades in integer:"))
if grades >= 90:
    print("outstanding")
else:
 if grades >=80:
    print("excellent")
 else:
    if grades >=70:
       print("very good")
    else:
       if grades >= 60:
          print("good")
       else:
          if grades >= 50:
             print("satisfactory")
          else:
             print("try again next year")  # end of loop


# excercise solution 
# we can use elif instead of else if i.e
birth_year=float(input("Enter the birth year:"))
if 1946  <=birth_year<=1964:
   print("you are a baby bommer")
else: 
   if 1965<=birth_year<=1980:
      print("you are a member of genX")
   else:
      if 1981<=birth_year<=1996:
         print("you are millienal")
      else:
         if 1997<=birth_year<=2012:
            print("you are generation Z")
         else:
            if 2013<= birth_year :
               print("you are a member of generation alpha")
            else:
               print("error ! please enter four digits year 1946 or later..")

