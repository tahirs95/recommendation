import csv
import itertools
import unittest
import os

# loading csv records in an array
def load_record():
    entries = []
    with open('canadianCheeseDirectory.csv', 'r', encoding="utf-8") as f:
        mycsv = csv.reader(f)
        for i, row in enumerate(itertools.islice(mycsv, 201)):
            if i == 0:                            # removed column names
                continue
            try:                                  # exception handling
                entries.append(row)
            except Exception:
                print("No record found.")
    return entries

# creating new record and storing it in array.
def create_record(entries):
    record = []
    for i in range(0,19):
        array_input = input("Enter the value for column {}:".format(i+1))
        record.append(array_input)

    entries.append(record)
    print("New record inserted is:", record)
    return entries, record


# edit record and store it in csv file
def edit_record(entries):
    row_input = int(input("Enter the value for row to be edited:"))
    col_input = int(input("Enter the value for column to be edited:"))
    value = input("Now please enter value:")

    entries[row_input-1][col_input-1] = value

    print("Row no.{} and col no.{} is edited".format(row_input, col_input))

    with open('canadianCheeseDirectory_edited.csv', 'w', encoding="utf-8") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(entries)
    csvFile.close()

    return entries, row_input, col_input, value

# delete record
def delete_record(entries):
    row_input_delete = int(input("Enter the value for row to be deleted:"))
    del entries[row_input_delete-1]
    writer = csv.writer(open('canadianCheeseDirectory_deleted.csv', 'w', encoding="utf-8"))
    writer.writerows(entries)
    print("Row no.{} is deleted.".format(row_input_delete))
    return entries


# Unit Test Cases
class TestSum(unittest.TestCase):

    def test_load_record(self):
        self.assertEqual(len(load_record()), 200, "Should be 200")

    def test_create_record(self):
        entries = load_record()
        new_entries, new_input = create_record(entries)
        self.assertEqual(new_input, new_entries[200], "Should be inserted at the last")
    
    def test_edit_record(self):
        entries = load_record()
        edited_entries, row, col, value= edit_record(entries)
        self.assertEqual(value, edited_entries[row-1][col-1], "Changes didn't occur in the list.")
    
    def test_delete_record(self):
        entries = load_record()
        deleted_entries = delete_record(entries)
        self.assertEqual(len(deleted_entries), len(entries), "Deletion didn't occur in the list.")
    
    def test_file_exits(self):
        self.assertEqual(os.path.exists("canadianCheeseDirectory.csv"), True, "File doesn't exist.")

if __name__ == '__main__':
    entries = load_record()
    option = int(input("Please select the option:"))
    if option == 1:
        new_entries, record = create_record(entries)
    elif option == 2:
        e, row_input, col_input, value = edit_record(entries)
    elif option == 3:
        print("200 entries are: ", entries)
    elif option == 4:
        e = delete_record(entries)
    else:
        print("Please select a valid option.")
    
    # unittest.main()