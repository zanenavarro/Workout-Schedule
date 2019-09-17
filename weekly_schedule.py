
tricep_work = {"Lying extensions\n", "Rope Pull Downs\n", "Tricep Dips\n", "Over Head Extensions\n","Bent over DB extensions\n"}
ab_work = {"Skulls\n","W. Pikes\n","W. Sit-ups\n","W. twist\n","Leg raise\n","Reverse Crunch\n","LLHR\n","Hanging Leg Raise\n","Bikes\n","alternating pikes\n"}
chest_work = {"Bench press\n","Incline Bench\n","Flys\n","Cobra Push-Ups\n","Pike Push-Ups\n","S To S Push-ups\n"}
back_work = {"Lat Pull-Downs\n","Bent Over Rows\n","Deadlifts\n","Pull-Ups\n","Single-Arm Dumbbell Row\n","Bar Pulls\n"}
shoulder_work = {"B/O raise\n","B/O Y-raise\n","over-head press\n","upright row\n","side raise\n","O/H front raises\n","scarecrows\n"}
bicep_work = {"Standing Curls\n","Seated Curls\n","Reverse Grip Curls\n","Curls with plate\n"}
leg_work = {"Squats\n","Lunges(forward)\n","Lunges(backward)\n","Box Jumps\n","Depth Drops\n","Lunge Jumps\n"}

a = "".join(tricep_work)
b = "".join(ab_work)
c = "".join(chest_work)
d = "".join(back_work)
e = "".join(shoulder_work)
f = "".join(bicep_work)
g = "".join(leg_work)

def my_function(fname):
    if fname == "monday":        #MONDAY
        print("today is"+'\033[31m' + " CHEST " + '\033[0m'+ "day and" + '\033[31m' + " AB " + '\033[0m'+"day!")
        input_ex = input("To see a list of your workouts type in either AB or CHEST:").lower()
        if "ab" in input_ex:
            print("Here are your ab workouts for today:\n"+'\033[31m' + b + '\033[0m')
        elif "chest" in input_ex:
            print("Here are your chest workouts for today:\n"+'\033[31m' + c + '\033[0m')
    elif fname == "tuesday":    #TUESDAY
        print("today is"+'\033[31m' + " BACK " + '\033[0m'+ "day and "+ '\033[31m' + " AB " + '\033[0m'+"day!")
        input_ex = input("To see a list of your workouts type in either BACK or ABS:").lower()
        if "ab" in input_ex:
            print("Here are your AB workouts for today:\n"+'\033[31m' + b + '\033[0m')
        elif "back" in input_ex:
            print("Here are your BACK workouts for today:\n"+'\033[31m' + d + '\033[0m')

    elif fname == "wednesday":       #WEDNESDAY
        print("today is"+'\033[31m' + " REST " + '\033[0m'+ "day\n")
        print("take a load off but make sure to eat healthy!!!")

    elif fname == "thursday":        #THURSDAY
        print("today is"+'\033[31m' + " SHOULDER " + '\033[0m'+ "day and "+ '\033[31m' + " AB " + '\033[0m'+"day!")
        input_ex = input("To see a list of your workouts type in either SHOULDERS or ABS:").lower()
        if "ab" in input_ex:
            print("Here are your AB workouts for today:\n"+'\033[31m' + b + '\033[0m')
        elif "shoulder" in input_ex:
            print("Here are your SHOULDER workouts for today:\n"+'\033[31m' + e + '\033[0m')
    elif fname == "friday":        #FRIDAY
        print("today is"+'\033[31m' + " TRICEP " + '\033[0m'+ "day and "+ '\033[31m' + " BICEP " + '\033[0m'+"day!")
        input_ex = input("To see a list of your workouts type in either BICEP or TRICEP:").lower()
        if "tricep" in input_ex:
            print("Here are your TRICEP workouts for today:\n"+'\033[31m' + a + '\033[0m')
        elif "bicep" in input_ex:
            print("Here are your BICEP workouts for today:\n"+'\033[31m' + f + '\033[0m')
    elif fname == "saturday":        #SATURDAY
            print("today is"+'\033[31m' + " REST " + '\033[0m'+ "day. CONGRATS, you made it through the week feel free to take a load off!!")

    elif fname == "sunday":         #SUNDAY
            print("today is"+'\033[31m' + " LEG " + '\033[0m'+ "day and "+ '\033[31m' + " AB " + '\033[0m'+"day!")
            input_ex = input("To see a list of your workouts type in either BACK or ABS:").lower()
            if "ab" in input_ex:
                print("Here are your AB workouts for today:\n"+'\033[31m' + b + '\033[0m')
            elif "leg" in input_ex:
                print("Here are your LEG workouts for today:\n"+'\033[31m' + g + '\033[0m')
    else:
        main()

def alternate_workout(alt_w):
    if alt_w =="none":
        print("Have a GREAT workout")
    elif "bench press" in alt_w:
        print("It usually is sadly, you can always try"+'\033[31m' + " DUMBBELL CHEST PRESSES" + '\033[0m')
    elif "squat rack" in alt_w:
        print("Sadly someone who is very loud is hogging the rack, you should try"+'\033[31m' + " SQUAT JUMPS." + '\033[0m')
    else:
        main()



def main():
    weekday = input("what day of the week is it:").lower()
    my_function(weekday)
    alternate_work = input("Enter which piece of equipment is occupied, if none enter NONE:").lower()
    alternate_workout(alternate_work)
    user_input = input("To see your other workout details, type: CONTINUE").lower()
    if user_input == "continue":
         my_function(weekday)
    else:
        print("Hope you have a good workout")

main()
