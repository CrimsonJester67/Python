#Read each row from a CSV file and print the list of string 
import csv 
csvfile=open('example.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow(['name','age','occupation'])
writer.writerow(['sanju','30','cricketer'])
writer.writerow(['ronaldo','37','footballer']) 
csvfile.close()
csvfile=open('example.csv','r')
reader=csv.reader(csvfile) 
for row in reader:
    print(row)
csvfile.close()
