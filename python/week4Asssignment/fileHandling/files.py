with open('names.txt', "r") as file:
    contents =file.read()
    with open("newNames.txt", "w") as newFile:
        newFile.write(contents)
        newFile.close()
    file.close()
