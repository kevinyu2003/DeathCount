import keyboard
import os
def increment_death_count(filename):
  """Increments the death count in a specified text file.

  Args:
    filename: The name of the text file containing the death count.

  Returns:
    None
  """

  try:
    with open(filename, 'r+') as f:
      absolute_path = os.path.abspath(filename)
      print(f"File updated. The file path is: {absolute_path}")
      count = int(f.read().strip())
      new_count = count + 1
      f.seek(0)
      f.write(str(new_count))
      f.truncate()
  except FileNotFoundError:
    print(f"File '{filename}' not found. Creating a new file with initial count 1.")
    
    with open(filename, 'w') as f:
      f.write('1')

def on_key_press(event):
  if event.name == 'k':
    increment_death_count('DeathCount.txt')
    print("K")

# Start listening for key presses
keyboard.on_press(on_key_press)
keyboard.wait()