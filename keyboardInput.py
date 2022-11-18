import keyboard

print("Press esc to stop.")
while True:
    print(keyboard.read_key())
    if keyboard.read_key() == "esc": break
    
print("✔ Program finished.")
