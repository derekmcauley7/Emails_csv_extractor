__author__ = 'derek'

def main():

    print("Welcome....")
    print("This program extracts the emails from a csv file.")
    num = input("Enter 'y' to convert or any other key to exit: ")
    string = "y"
    if num == string:
        csv_name = input(str("Enter the csv files name: "))

        file = open(csv_name+".csv").read()
        my_list = []
        comma = file.split(",")
        for row in comma:
            if "@" in row:
                row = row.split("\n")
                my_list.append(row)
            else:
                pass
            my_list2 = []
        for row in my_list:
            my_list2.append(row[0])
        emails = open("emails.txt", "w+")
        for row in my_list2:
            emails.write(row + ";")
        input("There should now be a file called email.txt in the folder with the csv")
        print("goodbye!!!")
    else:
        input("Goodbye")

if __name__ == '__main__':
    main()

