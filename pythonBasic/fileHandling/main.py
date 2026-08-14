# file handling

import datetime
import csv
import json

exampleFilePath="pythonBasic\\fileHandling\\example.txt"
csvFilePath="pythonBasic\\fileHandling\\students.csv"
jsonFilePath="pythonBasic\\fileHandling\\data.json"

# reset all files so we can start from a clean point
with open(exampleFilePath, "w") as file:
    file.write("Initial sentence: Hello, this is my first file")

with open(csvFilePath, "w", newline='') as file:
      writer=csv.writer(file)
      writer.writerow(["name", "age", "score"])
      writer.writerows([["Alice", 21, 30], ["Bob", 20, 129]])

with open(jsonFilePath, "w") as jsonFile:
    json.dump({'name': 'Alice', 'age': 30, 'skills': ['python', 'ai']},jsonFile, indent=4)

# open=method to open a file
# r=read mode
# w=write mode; if the file doesn't exist, it create the file; when write() is called, it replace everything in the file
# a=append mode; when write() is called, it appends new content at the end of the file
file=open(exampleFilePath, "r")
content=file.read()
print(content)
file.close() # always close to free the access to the file

file2=open(exampleFilePath, "w")
file2.write(f"Hello, this is my first file {datetime.datetime.now()}")
file2.close()

file3=open(exampleFilePath, "r")
content3=file3.read()
print(content3)
file3.close()

file4=open(exampleFilePath, "a")
file4.write("\n This line is appended later")
file4.close()
file4=open(exampleFilePath, "r")
content4=file4.read()
print(content4)
file4.close()

# `with` operator let the file to close automatically instead of call the close method every time 
with open(exampleFilePath, "r") as file:
    print(file.read())

# csv=comma separated values

with open(csvFilePath,"r") as myCsv:
    reader=csv.reader(myCsv)
    for row in reader:
        print(row)

with open(csvFilePath,"w", newline='') as myCsv:
    writer=csv.writer(myCsv)
    writer.writerow(["name", "age", "score"])
    writer.writerow(["Martha", 45, 27])

# json=set of pairs key/value


with open(jsonFilePath, "r") as jsonFile:
    data=json.load(jsonFile)
    print(data)

newData={"name":"Bob", "age":45, "skills":[]}

with open(jsonFilePath, "w") as jsonFile:
    json.dump(newData,jsonFile, indent=4)

with open(jsonFilePath, "r") as jsonFile:
    data=json.load(jsonFile)
    print(data)



