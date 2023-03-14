import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='your_username', password='your_password',
                              host='your_host', database='your_database')
cursor = cnx.cursor()

# Create the table
table = """CREATE TABLE matieres (
            id_etu INT NOT NULL,
            matiere1 DOUBLE DEFAULT NULL,
            matiere2 DOUBLE DEFAULT NULL,
            matiere3 DOUBLE DEFAULT NULL,
            matiere4 DOUBLE DEFAULT NULL,
            PRIMARY KEY (id_etu))
            ENGINE=InnoDB DEFAULT CHARSET=latin1;"""
cursor.execute(table)

# Insert the data
data = """INSERT INTO matieres (id_etu, matiere1, matiere2, matiere3, matiere4) 
          VALUES (2122753, 15, 14, 11, 17),
                 (20014866, 18, 18, 17, 19),
                 (21201772, 15, 15, 14, 14),
                 (21202056, 15, 14, 13, 12),
                 (21202188, 16, 15, 14, 12),
                 (21202469, 17, 18, 14, 11),
                 (21202654, 15, 14, 13, 12),
                 (21202671, 18, 15, 14, 12),
                 (21203819, 10, 12, 11, 10),
                 (21204871, 15, 14, 13, 12),
                 (21204894, 15, 14, 16, 18),
                 (21205262, 15, 14, 13, 12),
                 (21205661, 15, 15, 14, 14),
                 (21207700, 17, 18, 14, 13),
                 (21211145, 15, 16, 14, 20),
                 (21212434, 12, 15, 13, 16),
                 (21214787, 18, 17, 15, 14),
                 (21215366, 15, 17, 12, 11),
                 (21215601, 11, 12, 12, 12),
                 (21217487, 17, 18, 15, 14),
                 (21217925, 15, 15, 14, 14),
                 (21225617, 16, 18, 11, 14),
                 (21225765, 15, 15, 14, 12),
                 (200141129, 11, 18, 18, 17);"""
cursor.execute(data)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()
