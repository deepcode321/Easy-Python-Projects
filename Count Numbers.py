

print("Counting Game")
print("You get 1 pt by guessing right before the timer runs out.")
print("You lose your chance")
print("Are you ready")

import time
count=0
score=0

time_limit = 10
start_time = time.time()

while(count<10 and time.time()-start_time<time_limit):
    count+=1
    
    answer = input()
    
    if int(answer) ==count:
        score+=1
        print("Correct! Your score is now", score)
    else:
        print("Wrong guess")
        
if (score==10):
    print("You counted it all right")
else:
    print("Better luck next time. you couldn't count it within 10 sec")






