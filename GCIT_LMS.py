import mysql.connector

cnx = mysql.connector.connect(user='root', password='jacmsq5903',
                              host='localhost',
                              database='library')

def preparedStatement(statement):
    cursor = cnx.cursor()
    sql = (statement)
    cursor.execute(sql)
    resultSet = cursor.fetchall()
    i=1
    for row in resultSet:
        print(str(i) + ') ' + row[0])
        i += 1
    cursor.close

def getQueryColumn(storedProcedure, columnNumber): 
    cursor = cnx.cursor()
    cursor.callproc(storedProcedure)
    for result in cursor.stored_results():
        resultAsList = []
        for columnIndex in result.fetchall():
            resultAsList.append(columnIndex[columnNumber])
        return resultAsList
    cursor.close

def listCombiner(list1, list2):
    combinedList = []
    for itemA, itemB in zip(list1, list2):
        combinedList.append(itemA + ', '+ itemB)
    return combinedList

def displayResultSet(resultSet, quitMenu=False):
    i=1
    for result in resultSet:
        print(str(i) + ') ' + result)
        i += 1
    if quitMenu == True:
        print(str(i) + ') Quit to menu?')    

def libMenuSelector(screenCode):
    case={
        'main': main,
        'lib1': lib1,
        'lib2': lib2,
        #'lib3': lib3,
        'borr1': borr1,
        #'borr2': borr2,
        'admin': admin
        }
    case.get(screenCode, main)()

def main():
    def selectionHandler(user):
        return {
            '1':'lib1',
            '2':'admin',
            '3':'borr1'
        }.get(user, 'main')

    print("Welcome to the GCIT Library Management System. Which category of a user are you?\n")
    print("1) Librarian \n2) Administrator \n3) Borrower \n")
    userSelection = input()
    libMenuSelector(selectionHandler(userSelection))

def lib1():
    def selectionHandler(selection):
        return {
            '1':'lib2',
            '2':'main'
        }.get(selection, 'lib1')

    print("1) Enter Branch you manage \n2) Quit to previous \n")
    userSelection = input()
    libMenuSelector(selectionHandler(userSelection))

def lib2():
    branchNameList = getQueryColumn('getBranchNames', 0)
    displayResultSet(listCombiner(branchNameList, getQueryColumn('getBranchAddress', 0)), True)

#def lib3():
def borr1():
    print('Welcome Borrower')
#def borr2():
def admin():  
    print('Welcome Admin')  

libMenuSelector(0)
#preparedStatement('Select branchname from tbl_library_branch')
#print('---------SINGLE DATA COLUMN TEST-------------')
#displayResultSet(getQueryColumn('getBranches', 0), True)

##### FIX NESTED FUNCTION CALLS -> state maybe##########
cnx.close()