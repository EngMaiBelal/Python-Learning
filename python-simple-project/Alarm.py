import time
from playsound import playsound

def alarm_clock(alarm_time):
    while True:
        current_time = time.strftime('%H:%M')  # Get the current time in HH:MM format
        print(f"Current time: {current_time}", end='\r')  # Overwrite the current time every loop
        time.sleep(60)  # Check the time every minute
        
        if current_time == alarm_time:
            print("\nALARM! Time's up!")
            playsound('alarm_sound.mp3')  # Play your alarm sound
            break

# Set your alarm time in HH:MM format (24-hour clock)
alarm_time = '14:30'  # Example: 2:30 PM
alarm_clock(alarm_time)
