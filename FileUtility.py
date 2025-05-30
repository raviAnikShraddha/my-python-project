try:
    file1 = open("myFile.txt", "r")
    myContent = file1.readlines()
    file1.close()
    for line in myContent:
        print(line.replace("\n", ""))
except FileNotFoundError as error:
    print("Error: File not found")

try:
    file2 = open("output.txt", "a")
    myContent = str(input("Enter that text to write to you file: "))
    file2.write(myContent)
    print("Data successfully written to output.txt")
    file2.write(str(input("Enter additionally text to append to you file: ")))
    print("Data successfully appended to output.txt")
    file2.write(str(input("Final content to output file: ")))
    file2.close()
except FileNotFoundError as error:
    print("Error: File not found")

try:
    file1 = open("output.txt", "r")
    myContent = file1.readlines()
    file1.close()
    for line in myContent:
        print(line.replace("\n", ""))
except FileNotFoundError as error:
    print("Error: File not found")

