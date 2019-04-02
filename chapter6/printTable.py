# Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listOfLists):
    colWidths = [0] * len(tableData)
    for listOfStrings in listOfLists:
        width = 0
        i = 0
        for string in listOfStrings:
            if len(string) > width:
                width = len(string)
        colWidths[i] = width
        i += 1
    col = 0
    line = 0
    while col < len(listOfLists):
        while line < len(listOfLists[col]):
            print(listOfLists[col][line].rjust(colWidths[col]))
            line += 1
        col += 1

printTable(tableData)
    
    # iterate in each list to evaluate the longest string
    # set coldWidhts[i] = longest string length
    # 2 while loops
    # print tableData[i][0].rjust(colWidhts[i]) -> tableData[i+1][0].rjust(colWidhts[i+1])
    # print tableData[i][1].rjust(colWidhts[i]) -> tableData[i+1][1].rjust(colWidths[i+1])
