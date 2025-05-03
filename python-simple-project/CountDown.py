import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')  # \r returns the cursor to the start of the line
        time.sleep(1)
        seconds -= 1

    print("00:00")
    print("Time's up!")

# Set the countdown time in seconds
countdown_time = 10  # For example, 10 seconds
countdown_timer(countdown_time)
