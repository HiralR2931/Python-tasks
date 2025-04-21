#Task 1: Read a File and Handle Errors 


try:
    file = open('sample.txt', 'r')
    reading_file = file.read()   
    print(reading_file)
    file.close()

except FileNotFoundError:
    print("File not found")

