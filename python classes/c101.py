import time
print(dir(time))
def counter(seconds):
    while seconds>0:
        m=int(seconds/60)
        s=int(seconds%60)
        timer=f'{m}:{s}'
        print(timer)
        time.sleep(1)
        seconds -=1
    print("Times Up")
seconds=input("Enter The Time In Number Of Seconds")
counter(int(seconds))

