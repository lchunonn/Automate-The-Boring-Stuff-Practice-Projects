import time, pyperclip

input("Press ENTER to start the stopwatch. Afterwards, press ENTER again to 'click' the stopwatch. Ctrl-C to quit.")
print('Started')
lapNum = 1
startTime = time.time()
lastTime = startTime
output_text = []
try:
    while True:
        input()
        lapTime = round(time.time()-lastTime,2)
        totalTime = round(time.time() - startTime,2)
        text = f'Lap #{str(lapNum).rjust(2)}: {str(lapTime).rjust(5)} ({str(totalTime).rjust(6)})'
        print(text, end='')
        output_text.append(text)
        lapNum +=1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nStopwatch stopped.')
    pyperclip.copy('\n'.join(output_text))