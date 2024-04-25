import subprocess


dbname = "finalProject"

host = "localhost"

def run_sql_command(sql_command):
    """Execute an SQL command using the subprocess module and handle errors."""
    psql_cmd = f'psql -d {dbname} -h {host} -c "{sql_command}"'
    try:
        result = subprocess.run(psql_cmd, check=True, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the SQL command.")
        print(e.stderr)
        return False


def insert_data():
    """Inserts data into a specified table, handling inputs more robustly."""
    while True:
        table = input("Enter the table name: ")
        columns = input("Enter the columns (comma-separated): ")
        values = input("Enter the values (comma-separated, use single quotes for strings): ")
        sql_command = f"INSERT INTO {table} ({columns}) VALUES ({values});"
        
        if run_sql_command(sql_command):
            print("Data inserted successfully.")
            break
        else:
            print("Please try again or type 'exit' to return to the main menu.")
            retry = input("Do you want to retry? (yes/no): ").lower()
            if retry != 'yes':
                break

def delete_data():
    table = input("Enter the table name: ")
    condition = input("Enter the condition for deletion (e.g., 'id = 4'): ")
    sql_command = f"DELETE FROM {table} WHERE {condition};"
    run_sql_command(sql_command)

def update_data():
    table = input("Enter the table name: ")
    set_clause = input("Enter the SET clause (e.g., 'column1 = value1, column2 = value2'): ")
    condition = input("Enter the condition for the update (e.g., 'id = 4'): ")
    sql_command = f"UPDATE {table} SET {set_clause} WHERE {condition};"
    run_sql_command(sql_command)

def search_data():
    table = input("Enter the table name: ")
    condition = input("Enter the condition for search (e.g., 'id = 4'): ")
    sql_command = f"SELECT * FROM {table} WHERE {condition};"
    run_sql_command(sql_command)

def aggregate_functions():
    """Perform aggregate functions like COUNT, MAX, MIN, SUM, AVG."""
    table = input("Enter the table name: ")
    column = input("Enter the column name for aggregation: ")
    aggregate = input("Enter the aggregate function (COUNT, MAX, MIN, SUM, AVG): ")
    sql_command = f"SELECT {aggregate}({column}) FROM {table};"
    run_sql_command(sql_command)

def sorting():
    """Sort data in ascending or descending order."""
    table = input("Enter the table name: ")
    column = input("Enter the column name to sort on: ")
    sort_order = input("Enter the sort order (ASC or DESC): ")
    sql_command = f"SELECT * FROM {table} ORDER BY {column} {sort_order};"
    run_sql_command(sql_command)

def joins():
    """Join tables."""
    table1 = input("Enter the first table name: ")
    table2 = input("Enter the second table name: ")
    condition = input("Enter the join condition (e.g., table1.id = table2.table1_id): ")
    sql_command = f"SELECT * FROM {table1} JOIN {table2} ON {condition};"
    run_sql_command(sql_command)

def grouping():
    """Group results and perform aggregate functions."""
    table = input("Enter the table name: ")
    grouping_column = input("Enter the column name to group by: ")
    aggregate = input("Enter the aggregate function (e.g., COUNT(*)): ")
    sql_command = f"SELECT {grouping_column}, {aggregate} FROM {table} GROUP BY {grouping_column};"
    run_sql_command(sql_command)

def subqueries():
    """Execute a subquery within another query."""
    table = input("Enter the table name for the outer query: ")
    outer_condition = input("Enter the condition for the outer query (e.g., 'id IN'): ")
    subquery_table = input("Enter the table name for the subquery: ")
    subquery_condition = input("Enter the condition for the subquery: ")
    sql_command = f"SELECT * FROM {table} WHERE {outer_condition} AND id IN (SELECT id FROM {subquery_table} WHERE {subquery_condition});"
    run_sql_command(sql_command)

def transactions():
    """Execute a set of transactions."""
    print("Starting a transaction block. Please enter your SQL commands one by one.")
    print("Type 'COMMIT;' to commit the transaction or 'ROLLBACK;' to rollback.")
    transaction_commands = []
    while True:
        command = input("Enter SQL command (or 'DONE' to execute the transaction block): ")
        if command.upper() == 'DONE':
            break
        transaction_commands.append(command)
    # Wrap the entered commands in a transaction block
    transaction_block = '\n'.join(transaction_commands)
    sql_command = f"BEGIN;\n{transaction_block}"
    run_sql_command(sql_command)

#def error_handling():
#   
#
#    try:
#        # Simulate an error
#        run_sql_command("SELECT * FROM non_existent_table;")
#    except Exception as e:
#        print("An error was handled: ", e)


def main_menu():
    operations = {
        '1': insert_data,
        '2': delete_data,
        '3': update_data,
        '4': search_data,
        '5': aggregate_functions,
        '6': sorting,
        '7': joins,
        '8': grouping,
        '9': subqueries,
        '10': transactions,
       # '11': error_handling,
    }
    while True:
        print("\nJames awesome Database Management CLI")
        print("Error handling is built into each function.")

        for key in sorted(operations.keys()):
            print(f"{key}. {operations[key].__name__.replace('_', ' ').capitalize()}")
        print("12. Exit")
        choice = input("Enter your choice: ")
        if choice == '12':
            break
        if choice in operations:
            operations[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
