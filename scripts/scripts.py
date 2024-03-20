import requests
import psycopg2


def get_medicine_details():
    '''
    This function takes in <input> as input and returns a dictionary of the medicine details to be ordered.
    '''

    # Replace with your own database credentials
    connection = psycopg2.connect(
        user="your_username",
        password="your_password",
        host="127.0.0.1",
        port="5432",
        database="your_database"
    )

    data = {}

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query
    cursor.execute("SELECT medicine_name, quantity, information FROM medicines")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print each row
    for i, row in enumerate(rows, start=1):
        data[f"medicine_name_{i}"] = row[0]
        data[f"quantity_{i}"] = row[1]

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return data

def place_order(data):
    '''
    This function takes in the medicine dictionary as input and places order in PharmEasy.
    '''

    api_endpoint = "https://pharmeasy.com/api/orders"
    headers = {"Authorization": "TEMP_API_KEY"}
    response = requests.post(api_endpoint, headers=headers, data=data)
    
    if response.status_code ==  200:
        print("Order placed successfully")
        
    else:
        print("Failed to place order")
    