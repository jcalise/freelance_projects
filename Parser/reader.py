import ast
from datetime import datetime, timedelta, date
import csv


with open("jsondata.txt", "r") as ins:
    data = []
    for line in ins:
        this_line = ast.literal_eval(line)
        receipt_date = datetime.strptime(this_line["receipt_submission_datetime"]["s"].split(".")[0], "%Y-%m-%dT%H:%M:%S") - timedelta(hours=7)
        if receipt_date.isocalendar()[1] - 28 == 0:
            continue
        else:
            receipt_ID = this_line["receipt_submission_id"]["s"]
            receipt_status = this_line["receipt_status"]["s"]
            week_number = receipt_date.isocalendar()[1] - 28
            receipt_date = datetime.strftime(receipt_date, "%Y-%m-%d")
            receipt_data = {"receipt_ID": receipt_ID, "receipt_status": receipt_status, "receipt_date": receipt_date, "week_number": week_number}
            data.append(receipt_data)

file_name = "campaign_data_" + str(date.today()) + ".csv"

with open(file_name, mode='w') as csv_file:
    fieldnames = ['receipt_ID', 'receipt_status', 'receipt_date', 'week_number']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        writer.writerow(item)
