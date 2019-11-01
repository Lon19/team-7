import csv
with open('wpforms-Autistica-8211-Adjustments-10-29-2019.csv','rt')as f:
  data = csv.reader(f)
  count = 0
  for row in data:
        if count == 0:
              titles = row
        #print(row)
        count += 1
print(titles)
