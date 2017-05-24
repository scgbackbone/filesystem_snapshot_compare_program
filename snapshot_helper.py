import os
from difflib import unified_diff
import sys
import pickle
import colorama
from colorama import init, Fore, Back, Style


def createSnapshot(directory, filename):
    cumulative_directories = []
    cumulative_files = []

    for root, dirs, files in os.walk(directory):
        cumulative_directories += dirs
        cumulative_files += files

    try:
        with open(filename, "wb") as output:
            pickle.dump(cumulative_directories, output, -1)
            pickle.dump(cumulative_files, output, -1)
        print("\nSnapshot created successfully")
        print("name:\t" + filename)
    except Exception as e:
        print(e)

    input("\nPress [Enter] to continue...")
    return

def listSnapshots(extension):
    print("Specify full path to directory that you wish to check")
    print("or enter 0 to scan current working direcotry")
    directory = input()
    snaplist = []
    if directory == "0":
        filelist = os.listdir(os.curdir)
    else:
        try:
            filelist = os.listdir(directory)
        except Exception as e:
            input("\nPress [Enter] to continue...")
            return

    for item in filelist:
        if item.find(extension) != -1:
            snaplist.append(item)

    print("\tSnapshot list")
    print("====================================")
    printList(snaplist)

def compareSnapshots(snapfile1, snapfile2):
    colorama.init()
    os.system("clear")

    try:
        pkl_file = open(snapfile1, "rb")
        dirs1 = pickle.load(pkl_file)
        files1 = pickle.load(pkl_file)
        pkl_file.close()

        pk2_file = open(snapfile2, "rb")
        dirs2 = pickle.load(pk2_file)
        files2 = pickle.load(pk2_file)
        pk2_file.close()

    except Exception as e:
        print(e)
        input("Press [Enter] to continue...")
        return

    result_dirs = list(unified_diff(dirs1, dirs2))
    result_files = list(unified_diff(files1, files2))

    added_dirs = []
    added_files = []
    removed_dirs = []
    removed_files = []

    for result in result_files:
        if result.find("\n") == -1:
            if result.startswith("+"):
                added_files.append(result.strip("+"))
            elif result.startswith("-"):
                removed_files.append(result.strip("-"))

    for result in result_dirs:
        if result.find("\n") == -1:
            if result.startswith("+"):
                added_dirs.append(result.strip("+"))
            elif result.startswith("-"):
                removed_dirs.append(result.strip("-"))

    print(Fore.GREEN + "\n\n\t***ADDED DIRECTORIES***:\n")
    printList(added_dirs, default=False)
    print(Style.RESET_ALL)

    print(Fore.RED + "\n\n\t***REMOVED DIRECTORIES***:\n")
    printList(removed_dirs, default=False)
    print(Style.RESET_ALL)

    print(Fore.GREEN + "\n\n\t***ADDED FILES***:\n")
    printList(added_files, default=False)
    print(Style.RESET_ALL)

    print(Fore.RED + "\n\n\t***REMOVED FILES***:\n")
    printList(removed_files, default=False)
    print(Style.RESET_ALL)

    input("Press [Enter] to continue...")

def showHelp():
    colorama.init()
    os.system("clear")
    print(
    '''
    DIRECTORY/FILE SNAPSHOT TOOL
    ====================================
    Welcome to the directory/file snapshot tool. This tool
    allows you to create snapshots of a directory/file tree,
    list the snapshots you have created in the current directory,
    and compare two snapshots, listing any directories and files
    added or deleted between the first snapshot and the second.
    To run the program follow the following procedure:
    '''
    )
    print("\t"+ Back.BLUE + "1. Create a snapshot"+ Style.RESET_ALL)
    print("\t"+ Back.CYAN + "2. List snapshot files"+ Style.RESET_ALL)
    print("\t"+ Back.YELLOW + "3. Compare snapshots"+ Style.RESET_ALL)
    print("\t"+ Back.GREEN + "4. Help (this screen)"+ Style.RESET_ALL)
    print("\t"+ Back.RED + "5. Exit" + Style.RESET_ALL)
    print()
    input("Press [Enter] to continue...")

def invalidChoice():
    os.system("clear")
    print(Fore.RED + "====================================")
    sys.stderr.write("INVALID CHOICE, PLEASE TRY AGAIN\n")
    print("====================================" + Style.RESET_ALL)
    print()
    input("Press [Enter] to continue...")
    return

def printList(listt, default=True):
    fulllist = ""
    indexnum = 1

    if len(listt) > 20:
        for item in listt:
            print("\t\t" + item)
            if (indexnum) % 3 == 0:
                print("\n")
            indexnum += 1
    else:
        for item in listt:
            print("\t" + item)
    if default:
        input("\nPress [Enter] to continue...")
        return
    else:
        return
