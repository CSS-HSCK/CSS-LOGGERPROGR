import random
import time
import threading

# Function to simulate extremely high CPU load by creating complex calculations
def cpu_load():
    while True:
        # Deep loop to put more stress on CPU
        for _ in range(100000000):  # Use a huge iteration to consume more CPU
            _ = random.random() ** random.random()

# Function to consume memory rapidly by creating massive strings and lists
def memory_hog():
    data = []
    while True:
        # Create larger chunks of memory consumption
        data.append("slowdown" * 100000)  # Keep appending large strings to memory
        time.sleep(0.05)  # Add delay to avoid instant crash but fill memory fast

# Function to simulate slow keyboard input with extreme delays
def keyboard_delay():
    while True:
        time.sleep(random.uniform(0.5, 2))  # Random delay between 0.5 and 2 seconds
        print("Simulating extreme typing delay...")

# Function to simulate slow mouse movement with random lag
def random_mouse_delay():
    while True:
        time.sleep(random.uniform(0.5, 1.5))  # Random delay between 0.5 and 1.5 seconds
        print("Simulating heavy mouse lag...")

# Function to simulate a heavy screen freeze by running multiple blocking processes
def screen_freeze():
    while True:
        print("System is freezing...")  # Show the freeze message repeatedly
        time.sleep(2)  # Introduce a long sleep to simulate freeze

# Start all slowdown tasks in parallel threads
def start_slowdown():
    cpu_thread = threading.Thread(target=cpu_load, daemon=True)
    memory_thread = threading.Thread(target=memory_hog, daemon=True)
    mouse_thread = threading.Thread(target=random_mouse_delay, daemon=True)
    keyboard_thread = threading.Thread(target=keyboard_delay, daemon=True)
    freeze_thread = threading.Thread(target=screen_freeze, daemon=True)
    
    cpu_thread.start()
    memory_thread.start()
    mouse_thread.start()
    keyboard_thread.start()
    freeze_thread.start()

if __name__ == "__main__":
    print("Starting extreme PC slowdown...")
    start_slowdown()

    # Keep the main thread alive to prevent script from exiting
    while True:
        time.sleep(1)
