filename = "sample.txt"

# Create and write to the file
with open(filename, "w") as file:
    file.write("This is a sample file created for the Cognifyz internship.\n")
    file.write("Python file manipulation task is successfully completed.")

# Read the file
with open(filename, "r") as file:
    content = file.read()

print("File content:")
print(content)