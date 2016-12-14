import csv 

csvfile = open('whatever.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter = ',')

csvwriter.writerow([1, 2, 3, 4, 5])
csvwriter.writerow(['apple', 'banana', 'orange', 'peach', 'kiwi'])
csvwriter.writerow(['Best', '', '', '', 'Worst'])

csvfile.close()