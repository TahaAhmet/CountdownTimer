import time

while True:
    t = input("Enter the time in seconds (Press q to quit): ")

    if t == "q":
        print("Quitted.")
        break
    elif not t.isdigit():
        print("Please enter a valid number or 'q' to quit.")
        continue

    t = int(t)
    print("Countdown Timer is starting!!")

    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        if t >=0:
            print(t)
        t -= 1
    print('Time is over!!')


