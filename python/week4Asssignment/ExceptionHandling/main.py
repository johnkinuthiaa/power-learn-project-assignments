# thought i can create a cli portfolio
file_names =["aboutMe.txt","cars.txt","schools.txt","languages.txt","projects.txt"]

# just a script to create the files ...

# for file_name in file_names:
#     with open(file_name,"w") as file:
#         file.write("hi")
print("<<<Welcome to my cli portfolio>>>")
print("remember to enter 'quit' to exit the program")

is_over =False

while not is_over:
    print("Here are the available files: ")
    for file_name in file_names:
        print(file_name.strip())
    page_name =input("Enter the name of the file to read the contents: ")
    page_name = page_name.strip().lower()
    if page_name == "quit":
        print("Exiting the portfolio! Have a nice day ~by kinuthia")
        is_over =True
        break
    try:
        with open(page_name) as file:
            contents =file.read()
            print(f"Here are the contents of the {page_name} file: \n{contents}")
    except:
        print(f"no file with the name {page_name} was found")
    finally:
        print("Thanks for viewing my portfolio!!byee")
