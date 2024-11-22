import pandas as pd
import pymysql 
import yagmail
from datetime import datetime, timedelta
import time
#https://github.com/kootenpv/yagmail


# MySQL database configuration
db_host = "localhost"
db_user = "user"
db_password = "password"
db_name = "database_name"

# SQL query to execute
sql_query = "SELECT * FROM my_table;"

# Email configuration
email_subject = "MySQL Report in Excel Format"
email_recipient = "your_email@example.com"

def execute_sql_query(host, user, password, database, query):
    """
    Executes the SQL query on the MySQL database and returns the results.

    Args:
        host (str): The database host.
        user (str): The database username.
        password (str): The database password.
        database (str): The database name.
        query (str): The SQL query to execute.

    Returns:
        tuple: A tuple containing the columns (headers) and the query results.
    """
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return columns, results

def send_email_with_attachment(subject, recipient, attachment_path):
    """
    Sends an email with the Excel file as an attachment.

    Args:
        subject (str): The email subject.
        recipient (str): The recipient's email address.
        attachment_path (str): The absolute path to the Excel file to attach.
    """
    yag = yagmail.SMTP('your_email@gmail.com', 'your_password')
    yag.send(
        to=recipient,
        subject=subject,
        contents="Attached is the MySQL report in Excel format.",
        attachments=attachment_path
    )

def main():
    # Execute the SQL query
    columns, results = execute_sql_query(db_host, db_user, db_password, db_name, sql_query)

    # Create a pandas DataFrame with the query results
    df = pd.DataFrame(results, columns=columns)

    # Save the results in an Excel file
    excel_file_path = "/tmp/mysql_results.xlsx"
    df.to_excel(excel_file_path, index=False)

    # Send the email with the Excel file attached
    send_email_with_attachment(email_subject, email_recipient, excel_file_path)

if __name__ == "__main__":
    # Schedule automatic execution every 24 hours
    while True:
        # Execute the script
        main()

        # Wait 24 hours before the next execution
        next_execution_time = datetime.now() + timedelta(days=1)
        wait_time_seconds = (next_execution_time - datetime.now()).total_seconds()
        time.sleep(wait_time_seconds)
