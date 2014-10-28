import MySQLdb

db = MySQLdb.connect("localhost","root","","mysql")
cursor = db.cursor()
sql = """INSTRUCTION"""
cursor.execute(sql)
db.commit()
db.close()
