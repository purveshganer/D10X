import openai
from config import gpt35_api_key

openai.api_key = gpt35_api_key


system_prompt = '''
    *You are a SQL query generating AI agent.
    Generate an SQL query to retrieve detailed attendance records for an employee from a database. 
    The user will provide the employee's name and an optional time interval. 
    If the time interval is not given, use the employee's joining date to the current date. 
    The database has two tables:

    Employee:

    employee_id
    employee_name
    employee_age
    employee_gender
    employee_joining_date
    Attendance:

    employee_id
    date
    status_morning (boolean)
    status_afternoon (boolean)
    Ensure the query joins the tables on employee_id and filters by the given employee name and date range. 
    Order the results by date.

    For example-
    FOR prompt - 'I want attendance of Om Shirude from 1st July 2024 to 5th August 2024.'
    In response provide a similar SQL query - '
    SELECT * 
    FROM attendance
    JOIN employee ON attendance.emp_id = employee.id
    WHERE employee_name = 'Om Shirude' 
    AND attendance.date BETWEEN '2024-07-01' AND '2024-08-05';'*

        '''

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages=[{"role":"system","content":system_prompt},
                      {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__" : 
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit","bye","exit"]:
            break
        answer = chat_with_gpt(user_input)
        print('Assistant: ', answer)
