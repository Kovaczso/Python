#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter 


import os, shutil
# Python has a built-in os module with methods for interacting with the operating system
# The Shutil module allows you to do high-level operations on a file, such as copy, create, and remote operations

path = r"C:\Users\zkovac01\Desktop\Python File Sorting"
# The "r" prefix designates a "raw" string literal, 
# which means that backslashes (\) are treated as literal characters and not as escape characters.

path = path.replace("\\", "/")
path = path + "/"
# Replaces all "\" with "/" and adds one more to the end


file_names = os.listdir(path)
# Lists everthing in the path


folder_name = ["EXCELs", "TXTs","SQLs","PYTHONs","PDFs","ZIPs","PICs","DOCXs","JUPITERNBs"]


for loop in range(len(folder_name)):
    if not os.path.exists(path + folder_name[loop]):
        print(path + folder_name[loop])
        os.makedirs(path + folder_name[loop])
# This loop checks if folders from the list [folder_name] exist in the directory



for file in file_names:
    if ".csv" in file and not os.path.exists(path + "EXCELs/"+ file):
        print("File: " + file + " Moved into: "+ path + "EXCELs/"+ file)
        shutil.move(path + file, path + "EXCELs/"+ file)
    elif ".xlsx" in file and not os.path.exists(path + "EXCELs/"+ file):
        print("File: " + file + " Moved into: "+ path + "EXCELs/"+ file)
        shutil.move(path + file, path + "EXCELs/"+ file)
    elif ".xlsm" in file and not os.path.exists(path + "EXCELs/"+ file):
        print("File: " + file + " Moved into: "+ path + "EXCELs/"+ file)
        shutil.move(path + file, path + "EXCELs/"+ file)
        
    elif ".log" in file and not os.path.exists(path + "TXTs/"+ file):
        print("File: " + file + " Moved into: "+ path + "TXTs/"+ file)
        shutil.move(path + file, path + "TXTs/"+ file)
    elif ".txt" in file and not os.path.exists(path + "TXTs/"+ file):
        print("File: " + file + " Moved into: "+ path + "TXTs/"+ file)
        shutil.move(path + file, path + "TXTs/"+ file)
    elif ".TXT" in file and not os.path.exists(path + "TXTs/"+ file):
        print("File: " + file + " Moved into: "+ path + "TXTs/"+ file)
        shutil.move(path + file, path + "TXTs/"+ file)
  
    elif ".zip" in file and not os.path.exists(path + "ZIPs/"+ file):
        print("File: " + file + " Moved into: "+ path + "ZIPs/"+ file)
        shutil.move(path + file, path + "ZIPs/"+ file)
        
        
    elif ".sql" in file and not os.path.exists(path + "SQLs/"+ file):
        print("File: " + file + " Moved into: "+ path + "SQLs/"+ file)
        shutil.move(path + file, path + "SQLs/"+ file)
        
    elif ".pdf" in file and not os.path.exists(path + "PDFs/"+ file):
        print("File: " + file + " Moved into: "+ path + "PDFs/"+ file)
        shutil.move(path + file, path + "PDFs/"+ file)
        
    elif ".docx" in file and not os.path.exists(path + "DOCXs/"+ file):
        print("File: " + file + " Moved into: "+ path + "DOCXs/"+ file)
        shutil.move(path + file, path + "DOCXs/"+ file)
        
    elif ".jpg" in file and not os.path.exists(path + "PICs/"+ file):
        print("File: " + file + " Moved into: "+ path + "PICs/"+ file)
        shutil.move(path + file, path + "PICs/"+ file)
    elif ".png" in file and not os.path.exists(path + "PICs/"+ file):
        print("File: " + file + " Moved into: "+ path + "PICs/"+ file)
        shutil.move(path + file, path + "PICs/"+ file)
    
    elif ".py" in file and not os.path.exists(path + "PYTHONs/"+ file):
        print("File: " + file + " Moved into: "+ path + "PYTHONs/"+ file)
        shutil.move(path + file, path + "PYTHONs/"+ file)
    
    elif ".ipynb" in file and not os.path.exists(path + "JUPITERNBs/"+ file):
        print("File: " + file + " Moved into: "+ path + "JUPITERNBs/"+ file)
        shutil.move(path + file, path + "JUPITERNBs/"+ file)


    elif ".json" in file and not os.path.exists(path + "JSONs/"+ file):
        print("File: " + file + " Moved into: "+ path + "JSONs/"+ file)
        shutil.move(path + file, path + "JSONs/"+ file)
        
    elif ".pbix" in file and not os.path.exists(path + "PBIs/"+ file):
        print("File: " + file + " Moved into: "+ path + "PBIs/"+ file)
        shutil.move(path + file, path + "PBIs/"+ file)
        
# This for loop is placing the files into created folders according to their extension specified in the if/elif statements.
# Also it is printing out the file name that is being moved and the directory where it is moved if file is being moved.
