def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1


while True:
    try:
        number = int(input("Enter a number bigger than 1: "))
        if number <=1:
            print("Enter a number bigger than 1")
            continue
    except ValueError:
        print("Please enter integers only")
        continue
    else:
        steps = 1
        while True:
            number = collatz(number)
            steps += 1
            if number == 1:
                print(f"Collatz sequence completed in {steps} steps")
                break
        while True:
            another_round = input("Another number? y/n: ")
            if another_round == 'n' or another_round == 'y':
                break
            else:
                print("Enter y/n only")
        if another_round == 'n':
            break
