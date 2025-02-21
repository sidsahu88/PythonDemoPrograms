with open('hello.py') as file1:
    file_stuff = file1.read()
    print(file_stuff)

print(file1.closed)
print(file_stuff)

Lines = ['Hi, How are you?\n', 'I am good. Thank you.\n', 'How is your work going?\n', 'Its going good.']

with open('demo_file.txt', 'w') as file2:
    for line in Lines:
        file2.write(line)

