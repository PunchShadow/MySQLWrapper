import mysql.connector
from mysql.connector import Error

class MySQLWrapper:
    def __init__(self, host, port, database, user, password):
        try:
            self.host = host
            self.port = port
            self.database = database
            self.user = user
            self.password = passowrd
            self.connection = mysql.connector.connect(
                host = host,
                port = port,
                database = database,
                user = user,
                password = password
            )
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Database version: ", db_Info)
                self.cursor = self.connection.cursor()
                
        except Error as e:
            print("Database connect fail: ",e)
        
        self.tableNames = [] # Record the name of tables
        self.tableColumn = {} # Record column names by table

    def close(self):
        if (self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
            print("Database is close")


# -------------- << Privacy Functions >> -----------------------------

    def __reconnect(self):
        # Reconnect mysql connector
        self.connection = mysql.connector.connect(
            host = self.host,
            port = self.port,
            database = self.database,
            user = self.user,
            password = self.password
        )
        if self.connection.is_connected():
            db_Info = self.connection.get_server_info()
            print("Database version: ", db_Info)
            self.cursor = self.connection.cursor()

    def __findColumn(self, ColName):
        # Find the corresponding column name with current table
        # Return datatype when found, esle false
        # TODO: MySQL command execution
    def 



# ----------------- << Reset MySQL parameters >> --------------------------

    def setDatabase(self, newDB):
        # Reset the data base and reconnect
        self.database = newDB
        self.__reconnect()

    def setTable(self, newTable):
        # Reset the table usage
        self.table = newTable
        self.__reconnect()


# ----------------- << Database  Functions >> --------------------------------------

    def create_table(self, tableName, colList):
        # tableName: string, Name of the table
        # colList: List, [ ['column name', 'column type'], [] ]
        
        # Record table and column names
        self.tableNames.append(tableName)
        colName = []
        colStr = ''
        for col in colList:
            colName.append(col[0])
            colStr = colStr + ', ' + col[0] + ' ' + col[1]
        colStr = colStr[2:]
        self.tableColumn[tableName] = colName
        
        command = "CREATE TABLE %s (%s);" % (tableName, colStr)
        command_data = (tableName, colStr)

        print(colStr)
        self.cursor.execute(command)
    
    def _search_table(self, tableName):
        for table in self.tableNames:
            if table == tableName:
                return 1
        return 0


    def insert_table(self, row):
        

    def delete_table(self, tableName):
        if _search_table(tableName):
            command = 'DROP TABLE %s;' % tableName
            self.cursor.execute(command)
        else:
            print("There's not %s in %s" % (tableName, self.coonection.database))


# ----------------- << Support Functions >> -------------------

        
