from datetime import datetime
from prettytable import PrettyTable
import csv
class SaveTable:
    def __init__(self):
        self.table = PrettyTable()
        self.table.field_names = ["Lane ID", "Customer ID", "Number of Items", "Estimated Time", "Start Time"]

    def save_table_to_file(self,table, filename):
        with open(filename, 'w') as file:
            file.write(table.get_csv_string())

    def append_to_table(self,filename,l_id,date,customers):
        # Read the existing CSV file

        existing_data = []
        
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                existing_data = [row for row in reader]

        except FileNotFoundError:
            pass


        for i,row in enumerate(existing_data):
            if i==0:
                pass
            else:
                self.table.add_row(row)
        # Add new values to the table
        for i in customers:
            id, no_items,e_time,entry = i
            entry = entry.strftime("%Y-%m-%d %H:%M:%S")
            # entry = (date-entry).total_seconds()
            self.table.add_row([l_id,f"C{id}", no_items, f"{e_time}secs", entry])

        # Save the updated table back to the file
        self.save_table_to_file(self.table, filename)