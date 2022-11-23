import random, time, datetime

numberofQuestions = 10
score = 0
for i in range(numberofQuestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
    answer_count = 0
    print(f'Question #{i+1}: {num1} * {num2} = ')
    while True:
        if answer_count>=3:
            print("No more attempts")
            break
        start_time = datetime.datetime.now()
        answer = input()
        end_time = datetime.datetime.now()
        time_difference = (end_time - start_time).seconds
        if time_difference > 8:
            print("Time out.")
            break
        if not answer.isdigit():
            print("Enter integers only")
            answer_count +=1
            continue
        if int(answer) <=0:
            print("Positive integers only")
            answer_count += 1
            continue
        if int(answer) == num1*num2:
            print("Correct!")
            score += 1
            time.sleep(1)
            break
        else:
            print("Wrong. Please try again!")
            answer_count += 1
            continue
print(f"Score: {score}/{numberofQuestions}")
