import openpyxl


# create the object for workbook
wb = openpyxl.Workbook()

# grab the active sheet
sh = wb.active

# set Sheet Name
sh.title = "Dev_Evn"

sh['A1'] = "FName"
sh['B1'] = "LName"

sh['A2'] = "Divya"
sh['B2'] = "Z"

sh['A3'] = "Sarath"
sh['B3'] = "M"

# for save this file
wb.save(r"C:\Users\gopir\PycharmProjects\Python_Oct2020\data\WriteData.xlsx")