import ast
from datetime import datetime, timedelta, date
import csv


with open("jsondata.txt", "r") as ins:
    # Opens data file, which is poorly formatted version of JSON data
    data = []
    for line in ins:
        this_line = ast.literal_eval(line)
        '''Individual lines are Dict items, this converts the string format of 
        the text file to a useable Dict'''

        receipt_date = datetime.strptime(this_line["receipt_submission_datetime"]["s"]
                                         .split(".")[0], "%Y-%m-%dT%H:%M:%S") - timedelta(hours=7)
        '''UTC date in the file has some unnecssary data and is in the wrong timezome, 
        this shifts the time, removes unnecessary data and converts to datetime'''

        if receipt_date.isocalendar()[1] - 28 == 0:
            # Were looking at data for a specific set of weeks, if the data is before that it's ignored
            continue
        else:
            receipt_ID = this_line["receipt_submission_id"]["s"]
            receipt_status = this_line["receipt_status"]["s"]
            week_number = receipt_date.isocalendar()[1] - 28
            receipt_date = datetime.strftime(receipt_date, "%Y-%m-%d")
            receipt_data = {
                "receipt_ID": receipt_ID, 
                "receipt_status": receipt_status, 
                "receipt_date": receipt_date, 
                "week_number": week_number
            }
            data.append(receipt_data)

file_name = "campaign_data_" + str(date.today()) + ".csv"

with open(file_name, mode='w') as csv_file:
    # Creates headers
    fieldnames = ['receipt_ID', 'receipt_status', 'receipt_date', 'week_number']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        writer.writerow(item)
