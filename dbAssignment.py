
import sqlite3

# Establish a connection with the database file
conn = sqlite3.connect('new.db')
# while we have that connection open
with conn:
    # We are going to get the cusor off the connection
    cur = conn.cursor()
    # Use the cursor to send a command to our database
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_file TEXT)")
    # Commit your changes into the database
    conn.commit()
# Close the connection
conn.close()
    

# Establish a connection with the database file again       
conn = sqlite3.connect('new.db')


fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# This will loop through each object in the fileList and find the files that end with .txt
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # The value for each row will be one file name out of the list (x,)
        # will denote a string for each text file ending with .txt.
            cur.execute("INSERT INTO tbl_fileList (col_file) VALUES (?)", (x,))
            print(x)

conn.close()

            
