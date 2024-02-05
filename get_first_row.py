import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   f=open('data.csv')
   a=csv.reader(f)
   l=[]
   for i in a:
        l.append(i[0])
   return l[0]
print(get_first_row('data.csv'))

# Read the csv file