import os

def cnm(p1):
    for files in os.walk(p1):
        for filename in files:
            print(1)

cnm(r"C:/Users/hp/AppData/Local/Programs/Python/Python36")
