import time
time_count = int(input("Enter Your Time (in seconds):"))
for x in range(time_count,0,-1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/60/60)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up !")
