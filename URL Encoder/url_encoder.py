import base64
import ast
import csv
from datetime import date


with open("jsondata.txt", "r") as url_data:
    # Opens text file with vendor URL and JSON data.

    encode_url = url_data.readline().strip()
    # Extracts the vendor URL from the first line of the text file
    url_list = []

    for line in url_data:
        this_line = ast.literal_eval(line)
        #converts line to useable dictionary item 

        encoded_line = base64.urlsafe_b64encode(bytes(this_line['source'], encoding='utf-8'))
        # encodes the "source" key from the dict item

        url_list.append(encode_url + "?ref=" + encoded_line.decode("utf-8"))
        # assembles referral URL and appends to list item

file_name = "encoded_urls_" + str(date.today()) + ".csv"

with open(file_name, mode='w') as csv_file:
    # Creates headers
    fieldnames = ['encoded_url']
    writer = csv.writer(csv_file)

    writer.writerow(fieldnames)
    #write header into CSV 
    
    for item in url_list:
        #writes each line into the CSV, [] ensure that the whole line gets entered into 1 cell
        writer.writerow([item])
