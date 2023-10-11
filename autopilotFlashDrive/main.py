import os, sys, datetime
import csv

#& List of stuff to save to new CSV
hwidList = []

#& Loop through all CSV(s)
files = os.listdir("./in")
for file in files:

    #~ make sure it isn't the git keep file
    if file != ".gitkeep":

        print('./in/' + str(file))
        with open('./in/' + str(file), newline='', encoding="utf-16-le") as csvfile:

            rowcount = 0
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            
            for row in reader:

                #? if its the 2nd row then add it to the list 
                if rowcount == 1:

                    hwidList.append(row)

                #? if it's the header row, save the header for later
                else:

                    startingRow = row
                    rowcount += 1

#& export to new file
filename = ('./out/' + str(datetime.datetime.now())[:-7].replace(" ", "_").replace(":","-") + '.csv')
with open(filename, 'w', newline='') as csvfile:
    
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)                    
    writer.writerow(startingRow)

    #~ write the entire list of new rows
    for hwid in hwidList:

        writer.writerow(hwid)