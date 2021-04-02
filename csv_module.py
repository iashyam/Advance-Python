import csv
#pritty much all the code has to be momorised

#reding the csv file
with open ('file.csv', 'r') as file_csv:
    reader = csv.reader(file_csv)

    with open('new.csv','w') as file2:
        writer = csv.writer(file2)

        for line in reader:
            writer.writerow(line)