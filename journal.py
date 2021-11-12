import os.path


#line.replace("Date", "") when printing a string of entry for date we only gonna get the date without the text 'date'.
#entry_text.rstrip() -> it will get rid of the trailing white space.

def rid():
    if os.path.exists("hello.txt"):
        notepad_file = open("hello.txt", "r") 

        entry_list = []
        current_date = ""
        entry_text = ""
        #current_entry = ""
        
        for line in notepad_file:
            if line == "***\n":
                journal_entry = {'date': current_date, 'text': entry_text}
                entry_list.append(journal_entry)
                entry_text = ""
                current_date = ""
            elif "Date: " in line:
                current_date = line.replace("Date: ", "")
                entry_text = ""
            else:
                entry_text += line

        if entry_text != "":
            journal_entry = {'date': current_date, 'text': entry_text}
            entry_list.append(current_entry)
        
        notepad_file.close()

        return entry_list
    else:
        return []
