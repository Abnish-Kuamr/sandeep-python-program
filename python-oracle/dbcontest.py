#dbcontest.py
import cx_Oracle
kvrcon=cx_Oracle.connect("scott/tiger@localhost/orcl")
print("Python Program obtains connection from Oracle data base - Sucessfully")