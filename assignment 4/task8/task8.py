
user_input = input("Enter text to write to the file: ")

file1 = open("output.txt", "w") 
write_text = file1.write(user_input + '\n')
print("Data successfully written to output.txt.")
file1.close()

additional_input = input("Enter additional text to append: ")

file1 = open("output.txt", "a") 
appending_text = file1.write(additional_input + '\n')
print("Data successfully appended.")
print("\nFinal content of output.txt:")
file1.close()

file1 =open('output.txt','r')
read_file = file1.read()
print(read_file)
file1.close()

