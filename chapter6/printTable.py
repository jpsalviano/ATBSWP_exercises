# Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listOfLists):
    colWidths = [0] * len(tableData)    # creates a list where the lengths of the longest strings will be stored
    for index, listOfStrings in enumerate(listOfLists): # iterates in each list
        width = 0
        for string in listOfStrings:    # checks the length of each string and store the longest
            if len(string) > width:
                width = len(string)
        colWidths[index] = width        # stores the longest length in the list previously created for that purpose
    line = 0
    while line < len(listOfLists[0]):   # the number of items in a nested list is the number of lines in the table
        col = 0
        while col < len(listOfLists):   # the number of nested lists in the data list is the number of columns in the table
            print(listOfLists[col][line].rjust(colWidths[col]), end=' ') # prints one item for each column
            col += 1
        line += 1
        print('')                       # make sure next iteration will print in a newline

printTable(tableData)
