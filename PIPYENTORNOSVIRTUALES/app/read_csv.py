import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])
  
"""
import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path, 'r') as csvfile:      
      total = sum(int(r[1]) for r in csv.reader(csvfile))
      return total

response = read_csv('./data.csv')
print(response)
## este es el csv
Administration,200
Marketing,201
Purchasing,114
Human Resources,203
Shipping,121
IT,103
Public Relations,204
Sales,145
Executive,100
Finance,108

"""
