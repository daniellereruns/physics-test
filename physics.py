print("--- Physics Test---")

score= 0
gravityscore=0
weightscore=0

w= [19, 49, 98, 147]
problems= {19:10, 49:11, 98:13, 147:16}
probparttwo= {5:8, 9:10, 3:2, 8:3}

one=False
two=False
three=False

def test(x):
    if x== "M":
        global one
        one= True
        print("The formula you will be using today is M= W/G")
        grav= input("Pick A Planet, this will be determining what your gravity given will be! (Earth, Moon, Venus): ")
        if grav== "Earth":
            grav= 9.8
            print("Your given gravity is 9.8 m/s²")
        elif grav== "Moon":
            grav= 1.6
            print("Your given gravity is 1.6 m/s²")
        elif grav== "Venus":
            grav= 8.9
            print("Your given gravity is 8.9 m/s²")
        else:
            print("pick from the selected!")
        global w
        for i in w:
            print(f"you are finding the mass for {i}N and the gravity of {grav}m/s²")
            answer= f"{round(i/grav, 2)}kg"
            print(answer)
            print("mass is in kilograms!")
            user_answer= float(input("What is your answer for this problem? (round to the nearest second decimal point)!: "))
            part_two= input("units?: ")
            final= f"{user_answer}{part_two}"
            if answer==final:
                print("you're correct!")
                global score
                score+=1
                print(f"your final score is {score}")
            else: 
                print("you're incorrect")
                print(f"your final score is {score}")
        print(score)
        
    elif x== "G":
        global two
        two= True
        print("The formula you will be using is G= W/M")
        for weight, mass in problems.items():
                print(f"you are solving for {weight}N and {mass}kg")
                answer= f"{round(weight/mass,2)}m/s^2"
                user_answer= float(input("What is your answer for this problem? (round to the nearest second decimal point)!: "))
                part_two= input("units?: ")
                final= f"{user_answer}{part_two}"
                if answer==final:
                    print("you're correct!")
                    global gravityscore
                    gravityscore+=1
                else:
                    print("you are incorrect!")
        print(gravityscore)
    elif x== "W":
        global three
        three= True
        print("The formula you will be using is W=M*G")
        for mass, gravity in probparttwo.items():
            print(f"You are solving for {mass}kg and {gravity}m/s^2")
            answer= f"{round(mass*gravity,2)}N"
            user_answer= int(input("What is your answer for this problem? (round to the nearest second decimal point)!: "))
            part_two= input("units?: ")
            final= f"{user_answer}{part_two}"
            print(final)
            if answer==final:
                print("you're correct!")
                global weightscore
                weightscore+=1
                
            else:
                print("you are incorrect!")
        print(weightscore)
    else:
        print("not valid input!")
        
type_test= input("\nWould you like to be solving for mass, gravity, or weight today? (M, G, W): ")

type_test= type_test.upper()

test(type_test)
if score>0:
    print(score)
elif gravityscore>0:
    print(gravityscore)
else: 
    print(weightscore)