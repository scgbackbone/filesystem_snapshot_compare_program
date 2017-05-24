#=======================================#
#SNAPSHOTS.PY
#
#DIRECTORY/FILE SYSTEM SNAPSHOT PROGRAM #
#
#=======================================#

import snapshot_helper
import os
import time
import sys
from difflib import unified_diff

def menu():
    os.system("clear")
    print ('''
    DIRECTORY/FILE COMPARISON TOOL
    ====================================
    Please type a number and press enter:
    1. Create a snapshot
    2. List snapshot files
    3. Compare snapshots
    4. Help
    5. Exit
    ''')
    choice = input()
    return str(choice)

choice = "1"
while choice != "5":
    choice = menu()
    print(choice)
    if choice == "1":
        os.system("clear")
        print("\tCREATE SNAPSHOT")
        print("====================================")
        directory = input("Enter the directory name to create snapshot of: ")
        filename = input("Enter the name of the snapshot file to create: ")
        snapshot_helper.createSnapshot(directory, filename)

    elif choice == "2":
        os.system("clear")
        print("\tLIST SNAPSHOT FILES")
        print("====================================")
        print("Enter the file extension for your snapshot files")
        print("(for example, ‘snp’ if your files end in ‘.snp’):")
        extension = input("\t")
        snapshot_helper.listSnapshots(extension)

    elif choice == "3":
        os.system("clear")
        print("\tCOMPARE SNAPTSHOTS")
        print("====================================")
        snap1 = input("Enter the filename of snapshot 1: ")
        snap2 = input("Enter the filename of snapshot 2: ")
        snapshot_helper.compareSnapshots(snap1, snap2)

    elif choice == "4":
        snapshot_helper.showHelp()
    else:
        if choice != "5":
            snapshot_helper.invalidChoice()
os.system("clear")
