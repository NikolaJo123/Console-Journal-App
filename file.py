import sys
import os.path

def first_test():
    fake_text = '\nHello people!'
    my_file = open("hello.txt", "w")
    my_file.write(fake_text)
    my_file.close()
    #print(my_file)

def user_change():
    print("Type 'r' to write a text in a file or 'exit' to leave the editing.\n")
    while True:
        line = input(">")
        if line == "r":
            while True:
                date = input("Enter the date: ")
                time = input ("Enter the time: ")
                try:
                    name = input("Enter your name: ")
                except:
                    name = int
                if name == int:
                    print("Thats not a real name!")
                else:
                    break
                
            while True:
                try:
                    age = int(input("Enter your age: "))
                except:
                    age = -1
                if age < 0:
                    print("Entered a text, must enter a number!\n")
                else:
                    break
        
            stars = "\n***\n"

            if os.path.exists("test.txt"):
                notepad_file = open("test.txt", "w") #this short option (w) will rewrite the file or put text if there is none.
                notepad_file.write(f"Info entered on {date}, {time}: \n       name:{name} \n       age:{age}")
                notepad_file.write(stars)
                notepad_file.close()
        elif line == "exit":
            break
        else:
            print("Wrong command!")
            
    print("Editing closed!")



def user_append():
    print("Type 'r' to add more text in a file or 'exit' to leave the editing.\n")
    while True:
        line = input(">")
        if line == "r":
            while True:
                #try:
                date = input("Enter the date: ")
                    #date = ""
                if date == "":
                    print("You must enter a valid date for your journal entry.")
                else:
                    break
                
            while True:
                time = input ("Enter the time: ")
                try:
                    name = input("Enter your name: ")
                except:
                    name = int
                if name == int:
                    print("Thats not a real name!")
                else:
                    break
                
            while True:
                try:
                    age = int(input("Enter your age: "))
                except:
                    age = -1
                if age < 0:
                    print("Entered a text, must enter a number!\n")
                else:
                    break
            stars = "\n***\n"
            #print("")
            #print("\n\n")
            notepad_file = open("hello.txt", "a") # the short option (a) appends the text in the file.
            notepad_file.write(f"\n\nInfo entered on {date}, {time}: \n       name:{name} \n       age:{age}")
            notepad_file.write(stars)
            notepad_file.close()
        elif line == "exit":
            break
        else:
            print("Wrong command!")
            
    print("Editing closed!")


def time():
    print(system.time)


def read_file1():
    if os.path.exists("hello.txt"):
        notepad_file = open("hello.txt", "r") # this "r" flag or option is for reading the file.
        #sh = notepad_file.read() # -> this is another approach
        #print(sh) #                for printing the text from a certain file

        entry_list = []
        reverse = []
        current_entry = ""
        
        for line in notepad_file:
            if line == "***\n":
                #entry_list.append(current_entry)
                #current_entry = ""
                break
            else:
                current_entry += line
                #print(line, end="")
        #if current_entry != "":
        entry_list.append(current_entry)
        
        notepad_file.close()

        #entry_list.reverse()
        #reverse = entry_list[::-1]
            
        '''for reverse in entry_list:
            while entry_list != []:
                reverse = entry_list[-1]
                entry_list.pop(-1)
                print(reverse)'''
        
        for entry in entry_list:
            print(entry)
    else:
        print("File does not exist!")

def get_journal_entries_list():
    if os.path.exists("hello2.txt"):
        notepad_file = open("hello2.txt", "r") 

        entry_list = []
        reverse = []
        current_entry = ""
        
        for line in notepad_file:
            if line == "***\n":
                entry_list.append(current_entry)
                current_entry = ""
            else:
                current_entry += line

        if current_entry != "":
            entry_list.append(current_entry)
        
        notepad_file.close()
        
        return entry_list
    else:
        return []
        #print("File does not exist!")


def delete_entry():
    #Delete part. But previously we need to read the file.
    journal_entries = get_journal_entries_list()

    #del(journal_entries[0])
    print("Which journal entry date do you want to delete?")
    journal_date = input("Date: ")

    deletion(journal_entries, journal_date)


def deletion(entries_list, date_input):
    new_list = []
    final_list = []
    
    for index, inpt in enumerate(entries_list):
        if date_input in inpt:
            del(entries_list[index])
            break #-> In case we have more journal entries with the same date, with this approach we will only delete the first one.
            #return #-> If we use return instead of break we jump from the function off, but with break we execute the rest of the code.
        else:
            new_list = entries_list

    notepad_file = open("hello.txt", "w")
    for item in new_list:
        final_list = item + "***\n"
        #print(final_list)
        notepad_file.write(final_list)
    notepad_file.close()
    print("Done")
    


def read_file():
    if os.path.exists("hello.txt"):
        notepad_file = open("hello.txt", "r") 

        entry_list = []
        reverse = []
        current_entry = ""
        
        for line in notepad_file:
            if line == "***\n":
                entry_list.append(current_entry)
                current_entry = ""
            else:
                current_entry += line

        if current_entry != "":
            entry_list.append(current_entry)
        
        notepad_file.close()

        for entry in entry_list:
            print(entry)
    else:
        print("File does not exist!")


def edit_entry():
    count = 0
    lista = []
    #num = []
    journal_entries = get_journal_entries_list()
    for item in journal_entries:
        count = count + 1
        lista = count
        #print(lista)
    
    print(f"There are {count} entries!\n")
    print(journal_entries)
    print("\nWhich one would you like to edit?")

    #num = {count}
    '''while True:
        guess = input(">")
        if guess != 6:
            print("Wrong")
        else:
            print("It works!")'''
    #print(num)'''

    while True:
        entry = input(f"Enter a number from 1 to {count} or type 'exit' to leave the editing: ")
        if entry == 'exit':
            break
        else:
            wrong()


'''if sys.argv[1] == "add": #This approach will work if we execute the program from command promt or different command shell other than python shell.
    user_append()
if sys.argv[1] == 'read':
    read_file()'''

def test():
    lst1 = [1,2,3,4,5]
    lst2 = []

    #while lst1 != []:
    for lst2 in lst1:
        while lst1 != []:
            lst2 = lst1[-1]
            lst1.pop(-1)
            print(lst2)


def wrong():
    print("\nWrong command!")


def call_arg(optt):
    if optt == 'add':
        user_append()
    elif optt == 'read':
        read_file()
    elif optt == 'change':
        user_change()
    elif optt == 'test':
        test()
    elif optt == 'delete':
        delete_entry()
    elif optt == 'edit':
        edit_entry()
    else:
        wrong()




def equal():
    lista = [3,5,5,8,12,15]
    count = []
    broj = 0
    br = 0
    summ = 0

    for item in lista:
        broj = broj + 1
        count = broj
    for br in range(count):
        print(f"[ {br} ]")
    for br in lista:
        summ += br
    print(summ)
    '''while True:
        guess = input(">")
        if guess == "b":
            break
        elif guess != range(count):
            print("It works!")
        else:
            print("wrong!")'''

def s():
    print("Enter the following commands: 'add', 'read', 'change', 'delete', 'edit' or 'exit'")
    while True:
        comm = input("\nEnter your command: ")
        if comm == "exit":
            break
        else:
            call_arg(comm)

    print("Program closed!")



print("Print 's()' to start")






















