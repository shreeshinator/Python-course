import time
print("Timer Example")
duration = int(input("Enter duration in seconds: "))
for i in range(duration, 0, -1):
    print(f"Time remaining: {i} seconds")
    time.sleep(1)
print("Time's up!")