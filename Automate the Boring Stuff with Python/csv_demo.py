import csv
from pprint import pprint

#open the file
exampleFile = open('customer_data.csv')
#pass the object to the reader method of the csv module to create the reader object.
exampleReader = csv.reader(exampleFile)
#print location of the reader object.
#~ print(exampleReader)

#make a list from the data
exampleData = list(exampleReader)

pprint(exampleData)

#~ print('*' * 100)
#~ #print specific values from the data file. 
#~ print(exampleData[1][0], exampleData[1][1], exampleData[1][2], exampleData[1][3])
#~ print('*' * 100)
#loop through the data file row by row and print the data
#~ for row in exampleReader:
	#~ print('Row #' + str(exampleReader.line_num) +  ' ' + str(row))
	
#~ print('*' * 100)
#insert row into existing data

#~ outputFile = open('customer_data.csv', 'a', newline = '')
#~ outputWriter = csv.writer(outputFile)
#~ outputWriter.writerow(['101','Michael Barnes', 'mbarnes@asumh.edu', '870 508-6131'])
#~ outputFile.close()

print('*' * 100)
csvFile = open('csv_options.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter = '\t', lineterminator = '\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['potatoes','carrots', 'corn'])
csvWriter.writerow(['ham','ham','ham','ham','ham'])
print('File written?')

csvFile.close()


