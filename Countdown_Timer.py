import time

def countdown_timer(t):
    while t:
        mins , secs = divmod(t , 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Timer completed !")

print("************************Countdown Timer*******************************")
ch = int(input("Enter Time 1.Seconds 2.Mins 3.Hours :"))
if ch == 1:
    t = int(input("Enter the time in seconds :"))
    countdown_timer(t)
elif ch == 2:
    t = int(input("Enter the time in mins :"))
    countdown_timer(t*60)
else:
    t = int(input("Enter the time in hours :"))
    countdown_timer(t*60*60)

