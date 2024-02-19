which_problem = int(input("Which question would you like to ask, 1-10? "))

if which_problem == 1:
    num1 = 1
    while num1 <= 1000:
        print (num1)
        num1 = num1+1

elif which_problem == 2:
    num2 = 1
    while num2 <= 1000:
        print(num2)
        num2 = num2 +2


elif which_problem == 3:
    num3 = 0
    while num3 <= 1000:
        print(num3)
        num3 = num3+3


elif which_problem == 4:
    num4 = 0
    while num4 <= 1000:
        if num4 % 3 == 0 or num4 % 5 == 0:
            print(num4)
        num4 += 1


elif which_problem == 5:
    play = True
    while play == True: 
        max = int(input("Give me a number above 200: "))
        num = 1
        while num <= max and max >= 200:
            if num % 11 == 0 or num % 13 == 0:
                print(num)
            if num == max:
                play = False        
            num += 1

        if max < 200:
            print ("Try again")


elif which_problem == 6:
    string = input("Write a string: ")
    n6 = int(len(string))
    num6 = 0
    while num6 <= n6:
        print (string[num6])
        num6 = num6+1


elif which_problem == 7:
    play = True
    while play == True:
        string = input("Write a string with more than 10 characters: ")
        n = int(len(string))
        num = 1
        while num <= n and n >= 10:
            print(string[num])
            num = num + 2
        
        if num > n:
            break

        if n < 10:
            print ("Try again with a longer string.")


elif which_problem == 8:
    import random
    play = 1
    num1=0
    num2=0
    num3=0
    num4=0
    num5=0
    num6=0
    while play <= 1000:
        dice_roll = random.randint(1,6)
        if dice_roll == 1:
            num1 += 1
        elif dice_roll == 2:
            num2 += 1
        elif dice_roll == 3:
            num3 += 1
        elif dice_roll == 4:
            num4 += 1
        elif dice_roll == 5:
            num5 += 1
        elif dice_roll == 6:
            num6 += 1
        play = play +1
    print ("Number of times that the dice roll was a...")
    print ("1: ", num1)
    print ("2: ", num2)
    print ("3: ", num3)
    print ("4: ", num4)
    print ("5: ", num5)
    print ("6: ", num6)


elif which_problem == 9:
    num = int(input("Give me a number and I will tell you if it is a prime number: "))
    div_num = 2
    while div_num < num:
        if num % div_num == 0:
            print(num, "is not a prime number.")
            break
        elif num % div_num != 0:
            div_num += 1
    if div_num == num:
        print(num, "is prime number!")


elif which_problem == 10:
    num = 1
    while num <= 1000:
        div_num = 2
        while div_num <= num-1:
            if num % div_num == 0:
                num = num + 1
                break
            else:
                div_num = div_num + 1
        if num == div_num:
            print(num)
            num = num + 1
        if num == 1:
            print(num)
            num = num + 1

else:
    print("Try again and choose a number 1-10.")