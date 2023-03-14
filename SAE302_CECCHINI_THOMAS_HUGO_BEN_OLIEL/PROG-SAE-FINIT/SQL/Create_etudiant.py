import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpassword"
)

# Create a cursor
cursor = cnx.cursor()

# Create the database
cursor.execute("CREATE DATABASE c21220018")

# Use the newly created database
cursor.execute("USE c21220018")

# Create the "etudiants" table
table = """
CREATE TABLE etudiants (
    id int(11) NOT NULL AUTO_INCREMENT,
    nom varchar(255) DEFAULT NULL,
    prenom varchar(255) DEFAULT NULL,
    annee int(11) DEFAULT NULL,
    password varchar(200) DEFAULT NULL,
    statut varchar(255) DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
"""
cursor.execute(table)

# Insert sample data
data = """
INSERT INTO etudiants (nom, prenom, annee, password, statut) VALUES
('Collot', 'Enzo', 2023, '$2y$10$unnQ6QJXvfRUzIncl/qVZu9u.NrqHGL3sFMbdskCSLxSuLzDFOrOG', '2A'),
('Meylan', 'Kenan', 2023, '$2y$10$Xai23Voxbnmk1w680UFVce49LwQHLDJVkDTViTPXx7eWHSHHOB.du', '2A'),
('Ben Oliel', 'Hugo', 2023, '$2y$10$I41OetTloPjfbwzc4pEEYOZ3Y9TRv9xSkBQdtOJP00fEIOxYyWTBS', '2A'),
('Fournier', 'Jeremy', 2023, '$2y$10$qNXbrZnBLvEstFhXYhtsUeoZ.By6WPfxHHwGic8kaJMXxBYW67spW', '2A');
"""
cursor.execute(data)

# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()
