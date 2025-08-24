# file reading and writing

file = open("new_file.txt", "w")
file.write("File Handling and Exception Handling.")
 
try:
    file = open("new_file.txt", "r")
    content = file.read()
   
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()