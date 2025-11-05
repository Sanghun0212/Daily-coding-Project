## Daily code 3( timer & stopwatch )

import time

print("=== countdown timer ===")

count = int(input("Enter number of seconds: "))

while count >0:
    print(count)
    time.sleep(1)  ## time.sleep(1) --> time - modulke that handles things related to time
                   ## sleep() is a function inside the module
                   ## time,sleep(1) means pause the program  for 1 second before countinuing
    count -= 1

print("Time's up!")

## Trial 1
import time

print(" This is stopwatch! ")

count = int(input("Please write the time for counting: "))

while count > 0 :
    print(count)
    time.sleep(1)
    count -= 1

print("Finish!")


## Trying to create timer (what time cost) 
# Case 1 if users set limit time

import time

print(" This is timer! ")
count = 0
limit = int(input("Please put limit number: "))

while True:
    print(f"{count}s")
    count += 1
    time.sleep(1)

    if count == limit:
        print(f"{limit}s")
        print("Timer reaches the limit!")
        break

# Case 2 advanced version

import time

print(" This is timer! ")
count = 0
limit = int(input("Please put limit number: "))

start = int(input("countdown seconds before start: "))
while start >= 0:
    print(f"The timer will start in {start}s...")
    start -= 1
    time.sleep(1)

while count <= limit:
    print(f"{count}s")
    count += 1
    time.sleep(1)


print("Timer reaches the limit!")
        

# Case 3 more realistic timer

import time

print(" This is a stopwatch! ")

input("Press Enter to start ... ")
print("start!")
start = time.time()

input("Press Enter to stop ... ")
end = time.time()
print("finish!")

elapsed = end - start    ## we can calculate how many seconds spent on this stopwatch by taking minus on time when I pushed enter on "end" with time when "start"
minute = int(elapsed // 60)
seconds = int(elapsed % 60)
# print(f" Elapsed time: {elapsed} s")

if elapsed <= 60:
    print(f" Elapsed time: {elapsed:.2} s")    ## I use elapsed:.2 to show 1 decimal point
else:
    print(f" Elapsed time: {minute}min {seconds:.2}s")


# Case 4 add pause and resume concept

import time

print("===Stop Watch===")

print("Commands: start | pause | resume | stop")

elapsed = 0
running = False

while True:
    action = input("Enter command: ").lower()

    if action == "start" and not running:
        start_time = time.time()
        running = True
        print("Stop Watch Started!")

    elif action == "pause" and running:
        elapsed += time.time() - start_time 
        running = False
        if elapsed <= 60:
            print(f"Paused at {elapsed:.3f}s")
        else:
            minute = int(elapsed // 60)   # need to use int()
            seconds =  int(elapsed % 60)    
            print(f"Paused at {minute}min {seconds:.3f}s ")
    
    elif action == "resume" and not running:
        start_time = time.time()
        running = True
        print("Resumed!")

    elif action == "stop":
        elapsed += time.time() - start_time
        running = False
        if elapsed <= 60:
            print(f"Stopped at {elapsed:.3f}s")
        else:
            minute = int(elapsed // 60)
            seconds = int(elapsed % 60)
            print(f"Stopped at {minute}min {seconds:.3f}s ")
        break
    
    else:
        print("Invalid command")