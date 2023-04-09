open_file = ""
code = ""
lines = []
function = []
numbers = {}
letters = {}
error_lines = []
comments = []
running = True

def check_response(response):
    global running, open_file, code
    if response == "load":
        open_file = input("File:\n>>>")
        if ".monke" in open_file:
            try:
                with open(open_file, "r") as file:
                    code = file.read()
                    print("Open File: " + open_file)
                    print("Script: " + code)
            except Exception as e:
                print("File Could Not Open Because " + str(e))
        else:
            print("Not A .monke File")
    elif response == "run":
        if open_file == "":
            print("No Open File")
        else:
            compile()
            b = 0
            print("Errors on lines:")
            while b < len(error_lines):
                print(error_lines[b])
                b = b + 1
    elif response == "quit":
        running = False
    elif response == "help":
        print("help : prints list of commands and what they do")
        print("load : loads a file")
        print("run : compiles and runs the code")
    else:
        print("Not A Command")

def compile():
    global running, lines, function, numbers, letters, error_lines, comments
    lines = code.split("\n")
    i = 0
    while i != len(lines):
        if "monke.hideline" not in lines[i]:
            if " is numbers" in lines[i]:
                function = lines[i].split(" is ")
                numbers[function[0]] = 0
            elif " is letters" in lines[i]:
                function = lines[i].split(" is ")
                letters[function[0]] = ""
            elif " is " in lines[i] and "numbers" not in lines[i] and "letters" not in lines[i]:
                function = lines[i].split(" is ")
                if "console.read" in function[1]:
                    function[1] = input()
                if "+" in function[1]:
                    value = function[1].split(" + ")
                    function[1] = value[0] + value[1]
                if "-" in function[1]:
                    value = function[1].split(" - ")
                    function[1] = value[0] - value[1]
                if "*" in function[1]:
                    value = function[1].split(" * ")
                    function[1] = value[0] * value[1]
                if "/" in function[1]:
                    value = function[1].split(" / ")
                    function[1] = value[0] / value[1]
                if function[0] in numbers:
                    numbers[function[0]] = int(function[1])
                elif function[0] in letters:
                    letters[function[0]] = str(function[1])
                else:
                    error_lines.append(i)
            elif "console.write in " in lines[i]:
                function = lines[i].split(" in ")
                if function[1] in numbers:
                    print(numbers[function[1]])
                elif function[1] in letters:
                    print(letters[function[1]])
                else:
                    print(function[1])
            elif "jump if " in lines[i]:
                function = lines[i].split(" if ")
                function = function[1].split(" ")
                if function[2] == "to":
                    if function[1] in numbers:
                        if numbers[function[1]] == int(function[0]):
                            i = int(function[3]) - 1
                    else:
                        error_lines.append(i)
                else:
                    error_lines.append(i)
            elif "jump if not " in lines[i]:
                function = lines[i].split(" if not ")
                function = function[1].split(" ")
                if function[2] == "to":
                    if function[1] in numbers:
                        if numbers[function[1]] != int(function[0]):
                            i = int(function[3]) - 1
                    else:
                        error_lines.append(i)
                else:
                    error_lines.append(i)
            elif "jump to " in lines[i]:
                function = lines[i].split(" to ")
                i = int(function[1]) - 1
            else:
                error_lines.append(i)
        i = i + 1

print("MonkeLang Compiler Version 1.2 2023\nType 'help' for more information")

while running == True:
    check_response(input(">>>"))