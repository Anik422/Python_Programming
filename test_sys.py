import sys
# print(sys.argv)
if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    Password = sys.argv[1]
    print("password", Password)