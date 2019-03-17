"""
CS 5001 SP 2019
Hasti Gheibi Dehnashi
HW5

consulted stackoverflow to learn how to raise a SyntaxError
https://stackoverflow.com/questions/33717804/python-raise-syntaxerror-with-lineno

"""



      
def main():
    try:
        
        filename = input("Enter the name of your file\n")   
        records = process_file(filename)
    except FileNotFoundError as error:
        print("no such file found", error)
    except ValueError as error:
        print("incorrect Field Type", error)
    except SyntaxError as error:
        print("wrong number of records in line #", error)
    except EmptyFile 
    else: 
        for record in records:
            for i in record:
                print(i, type(i))    
    
def process_file(filename):
    #read header record
    file = open(filename, "r")
    
    #process header record
    firstLine = file.readline().strip().split()
    
    #begin processing remaining lines
    database = []
    current_line = []
    converted_line = []
    
    #iterates through each line, split and strips it, puts it into a list
    for line in file:
        current_line = line.strip().split()
        if len(current_line) != len(firstLine):
            raise SyntaxError
        num_fields = len(current_line)
        #iterates through each field within the line and processes it according to record
        for i in range(num_fields):
            if firstLine[i] == "S":
                string_field = current_line[i]
                converted_line.append(string_field)
            if firstLine[i] == "#":
                num_field = current_line[i]
                num_field = int(num_field)
                converted_line.append(num_field)
            if firstLine[i] == "$":
                currency_field = current_line[i]
                float_currency_field = dollar(currency_field)
                converted_line.append(float_currency_field)
        #adds converted line to database
        database.append(converted_line)
        converted_line = []
    return database

def dollar(value_str):
    try:
        float_value_str = float(value_str)
    except ValueError:
        if value_str[0] == "$":
            float_value_str = value_str.replace("$","")
            float_value_str = float(float_value_str)
        if value_str[0] != "$":
            raise ValueError

    return float_value_str
  
main()

"""
In case you need to create a custom error, borrowed from:

https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python

class EmptyFile(Exception):
    pass

empty_file = file.read(1)
    if empty_file == "":
        raise EmptyFile("the file is empty")
"""
