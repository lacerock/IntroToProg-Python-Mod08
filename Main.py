#)0_0(#
#Title: main.py
#Desc: an application demonstrating py modules
#Change Log
#lredinger,191129,created file
#lredinger,191201, added code to complete Assignment09

# modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as EmpIo
else:
    raise Exception("This file was not intended for import")

# data
file_name = "EmployeeData.txt"
empList = []
fileList = Fp.read_data_from_file(file_name)

# pull data from file into list
for row in fileList:
    empList.append(Emp(row[0], row[1], row[2].strip()))

# main script using modules
while True:
    # menu handling
    EmpIo.print_menu_items()
    usrCh = EmpIo.input_menu_options()

    # show current employees
    if usrCh == "1":
        EmpIo.print_current_list_items(empList)

    # user add employees
    elif usrCh == "2":
        empList.append(EmpIo.input_employee_data())

    # save current data to file
    elif usrCh == "3":
        Fp.save_data_to_file("EmployeeData.txt", empList)

    else:
        print("Exiting Program")
        break
