import time
import sys

# Define the loading function
def show_loading_screen(duration=5):
    load_str = "Loading..."
    load_animation = "|/-\\"
    length = len(load_str)

    for i in range(duration * 5):
        sys.stdout.write("\r" + load_str + " " + load_animation[i % len(load_animation)])
        sys.stdout.flush()
        time.sleep(0.1)  # Pause to create the animation effect

    # Clear the loading screen after duration ends
    sys.stdout.write("\r" + " " * (length + 5) + "\r")
    sys.stdout.flush()
    print("Your Expense Tracker is now running")
#loading_screen(5)
def exit_screen(duration=5):
    load_str = "Exiting..."
    load_animation = "|/-\\"
    length = len(load_str)

    for i in range(duration * 5):
        sys.stdout.write("\r" + load_str + " " + load_animation[i % len(load_animation)])
        sys.stdout.flush()
        time.sleep(0.1)  # Pause to create the animation effect

    # Clear the Exit screen after duration ends
    sys.stdout.write("\r" + " " * (length + 5) + "\r")
    sys.stdout.flush()
    print("Expense Tracker closed")
