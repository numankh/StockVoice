import pymysql
import config

conn = pymysql.connect(dbhost, user=dbuser,port=dbport,
                           passwd=dbpassword, db=dbname)

cursor = conn.cursor()


create_master_table="""
CREATE TABLE master (
userId INT PRIMARY KEY,
appId VARCHAR(255),
deviceId VARCHAR(255))
"""

create_company_table="""
CREATE TABLE company (
userId INT,
name VARCHAR(255),
FOREIGN KEY (userId) REFERENCES master(userId))
"""

create_domain_table="""
CREATE TABLE domain (
userId INT,
name VARCHAR(255),
FOREIGN KEY (userId) REFERENCES master(userId))
"""

# cursor.execute(create_master_table)
# cursor.execute(create_company_table)
# cursor.execute(create_domain_table)


conn.commit()
conn.close()
