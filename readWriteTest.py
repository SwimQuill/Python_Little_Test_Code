dataFile = open("testfile.txt", "w")

dataFile.write("Hello, World!")
dataFile.write(" And here is some more text.")

dataFile = open("testfile.txt", "r")

print dataFile.read()

dataFile.close()

x = raw_input("Do you wish to delete the contents of dataFile? >>> ")
y = raw_input("Do you wish to overwrite the contents of dataFile? >>> ")


def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()

if x in ['yes', 'Yes', 'Y', 'y']:
    dataFile = open("testfile.txt", "w")
    deleteContent(dataFile)
else:
    print ("You didn't delete the file!")

# To Do List:
# 1. Make a backup file that can't be accessed in any way to preserve data.
# 2. Make a method that will overwrite the data of the main file with new data.
