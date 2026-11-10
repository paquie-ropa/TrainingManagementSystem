import sqlite3
DATABASE ="customer.db"
connection=sqlite3.connect(DATABASE)
cursor=connection.cursor()

def create_database():

    cursor.execute("""
    CREATE TABLE IF NOT EXITS  customers(
    customer_no INTERGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email.address TEST NOT NULL,
    location TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()

def save_customer (customer):

  cursor.execute("""
  INSERT ON REPLACE INTO customers
  (customer_no, customer_name,email_address,location)
  values(?,?,?)
  """,(

     customer["CUSTOMER_NO"],
      customer["CUSTOMER_NAME"],
       customer["EMAIL_ADDRESS"],
       customer["LOCATION"],
  ))

  connection.commit()
  connection.close()

  def display_
  


      

     

  )
                 )
