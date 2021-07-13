import mysql.connector
class DbHelper:
    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='12345',
                                         database='emplooyeedb')
        db_Info = self.connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        self.cursor = self.connection.cursor()
        
    
        
       

    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''

        self.cursor.execute("select max(salary) from employee")
        max_sal=self.cursor.fetchall()
        return max_sal

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        self.cursor.execute("select min(salary) from employee")
        min_sal=self.cursor.fetchall()
        return min_sal
        

if __name__ == "__main__":

    
    db_helper = DbHelper()
    
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)
