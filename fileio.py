#this tutorial is about file input and output
with open('texteditor.py') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end = '')