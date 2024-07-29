# Define variable
text = "Hello World!"

# Print variable
print(text)

# Using a function
def hello_world():
  print(text)
  
hello_world()

# Writing to a .txt file
with open("helloWorld.txt", "w") as file:
  file.write(text)
