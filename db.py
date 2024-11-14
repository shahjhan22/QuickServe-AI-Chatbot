import pymysql

# Global connection object
cnx = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="pandeyji_eatery"
)


def insert_order_tracking(order_id, status):
    # Open a cursor using pymysql
    cursor = cnx.cursor()

    # Define the insert query
    insert_query = "INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)"

    # Execute the query with provided parameters
    cursor.execute(insert_query, (order_id, status))

    # Commit the transaction to save changes
    cnx.commit()

    # Close the cursor
    cursor.close()



def get_total_order_price(order_id):
    # Opening a cursor to interact with the database
    with cnx.cursor() as cursor:
        # Executing the SQL query to call the stored function
        query = f"SELECT get_total_order_price({order_id})"
        cursor.execute(query)

        # Fetching the result of the query
        result = cursor.fetchone()[0]

    return result




def insert_order_item(food_item, quantity, order_id):
    try:
        # Opening a cursor to interact with the database
        with cnx.cursor() as cursor:
            # Calling the stored procedure
            cursor.callproc('insert_order_item', (food_item, quantity, order_id))

            # Committing the changes to save the transaction
            cnx.commit()

        print("Order item inserted successfully!")
        return 1  # Indicating success

    except pymysql.MySQLError as err:
        print(f"Error inserting order item: {err}")

        # Rollback changes if any error occurs during the transaction
        cnx.rollback()
        return -1  # Indicating an error

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

        # Rollback changes in case of a general exception
        cnx.rollback()
        return -1  # Indicating an error



def get_next_order_id():
    # Open a cursor to perform database operations
    with cnx.cursor() as cursor:
        # Executing the SQL query to get the maximum order_id
        query = "SELECT MAX(order_id) FROM orders"
        cursor.execute(query)

        # Fetching the result
        result = cursor.fetchone()[0]

    # Returning the next available order_id
    if result is None:
        return 1
    else:
        return result + 1


def get_order_status(order_id: int):
    # Create a cursor object
    cursor = cnx.cursor()

    # SQL query to fetch the order status
    query = "SELECT status FROM order_tracking WHERE order_id = %s"
    cursor.execute(query, (order_id,))  # Passing the order_id as a parameter

    # Fetch the result
    result = cursor.fetchone()

    # Closing the cursor
    cursor.close()

    # Returning the order status
    if result:
        return result[0]
    else:
        return None
