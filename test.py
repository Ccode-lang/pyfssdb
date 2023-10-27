import fssdb

db = fssdb.db("127.0.0.1")

print(db.ping())
print(db.create_dict("test"))
print(db.write_point("test", "test", "Hello, World!"))
print(db.read_point("test", "test"))
print(db.delete_point("test", "test"))
print(db.delete_dict("test"))
print(db.powerdown())