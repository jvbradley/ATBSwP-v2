#! python3
# https://automatetheboringstuff.com/2e/chapter6/
'''
Table Printer
Write a function named printTable() that takes a list of lists of strings and
displays it in a well-organized table with each column right-justified. Assume
that all the inner lists will contain the same number of strings. For example,
the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose
'''

def printTable(tableData):
    columnWidths = [0] * len(tableData)
    columnDataRotated = {}
    outputTable = []

    # This section of code iterates through the variable
    # provided and feeds it into a rotated table.
    # Variable 'l' accesses each list in tableData
    for l in range(len(tableData)):
        # Variable 'd' accesses the data of list 'l'
        for d in range(len(tableData[l])):
            # This sets the lengths of each column.
            if columnWidths[l] < len(tableData[l][d]):
                columnWidths[l] = len(tableData[l][d])

        for d in range(len(tableData[l])):
            keyName = 'c' + str(l)
            keyName += 'd' + str(d)
            columnDataRotated[keyName] = tableData[l][d].rjust(columnWidths[l])

    y = 0
    while y < int(len(columnDataRotated) / len(tableData)):
        x = 0
        columnData = []
        while x < len(tableData):
            keyName = 'c' + str(x)
            keyName += 'd' + str(y)
            columnData.append(columnDataRotated[keyName])
            x += 1
        outputTable.insert(y, columnData)
        y += 1

    #Variable 'o' access each list in outputTable
    for o in range(len(outputTable)):
        print(' '.join(outputTable[o]))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
