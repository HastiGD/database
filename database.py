"""
CS 5001 SP 2019
Hasti Gheibi Dehnashi
HW5

consulted stackoverflow to learn how to raise a SyntaxError
https://stackoverflow.com/questions/33717804/python-raise-syntaxerror-with-lineno

"""



      
def main():
    filename = input("Enter the name of your file\n")
    
    #return filename and pass to process(file)
    process_file(filename)
    
    
def process_file(filename):
    #read header record
    file = open(filename, "r")
    
    #process header record
    firstLine = file.readline().strip().split()
    
    #process remaining lines
    database = []
    current_line = []
    converted_line = []
    

    for line in file:
        current_line = line.strip().split()
        if len(current_line) != len(firstLine):
            raise SyntaxError("wrong number of records in line #")
        num_fields = len(current_line)
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
                converted_line.append(currency_field)
        database.append(converted_line)
        for item in converted_line:
            print(type(item))
        converted_line = []
    print(database)


            
    #print(database)
        #for field in current_line:
            #print(field, end='\n')
            
        #for i in range(len(line)):
            #
        #database.append(current_line)
    #print(database)
        
        

    #

main()

"""
if firstLine[i] == "S":
                string_field = line[i]
                string_field = string_field.upper()
                current_line.append(string_field)
            if firstLine[i] == "#":
                num_field = line[i]
                num_field = num_field*2
                current_line.append(num_field)
            if firstLine[i] == "$":
                currency_field = line[i]
                currency_field = "$" + currency_field 
                current_line.append(currency_field)
        
        database.append(all_lines) 
    for index, value in enumerate(firstLine):
        if value == character:
            print("Index of",character, "is", index)
            indexes_of_character.append(index)
    print(indexes_of_character)
    return indexes_of_character





    for i in range(len(database)):
            
                #database_lists(i)
            #database[0][index] = "HASTI"
        #if value == "$":
            #print("Index of $ is",index)
            #database[0][index] = "BABY"
    #print(database)
        
        #if record == "#":
            #print(firstLine.index(record))
        #if record == "$":
            #print(firstLine.index(record))
    #print(database)
            
#def database_lists(list_num):
    #database[list_num][index] = "HASTI"
        
        #read the line
        #break it up into fields
        #check for correct number of fields as specified by header
        #process if number of fields is correct
        #append to database
        #return database
#def dollar(value_str):
    #convert value to string
main()
"""
