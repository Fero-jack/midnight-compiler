import time

def countdown(minutes):
seconds = minutes * 60

try:
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\rTime remaining: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print("\nTime is up! Take a break.")
except KeyboardInterrupt:
    print("\nTimer stopped.")

def main():
print(“🌙 MIDNIGHT COMPILER — STUDY TIMER”)
print(”–––––––––––––––––”)

try:
    minutes = int(input("How many minutes do you want to study? "))
    if minutes <= 0:
        print("Please enter a number greater than zero.")
        return
    print("Focus mode activated. You can do this!")
    countdown(minutes)
except ValueError:
    print("Please enter a valid whole number.")

if name == “main”:
main()