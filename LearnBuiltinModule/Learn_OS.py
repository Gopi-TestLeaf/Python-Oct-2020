import os

# print(os.getcwd())
#
# os.chdir("C:\devtools-selenium")
#
# print(os.getcwd())
#
# print(os.listdir())

for path, dir, file in os.walk("C:\devtools-selenium\DevTools-Selenium\src"):
    print(file)