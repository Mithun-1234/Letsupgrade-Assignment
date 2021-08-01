#Remove occurence of an element in list  
def remove_value(list_name,val):
  return[value for value in list_name if value != val]
A = [5,1,8,9,5,6,3,5]
A = remove_value(A,5)
print(A)