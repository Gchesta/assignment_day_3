
def find_max_min(list_of_nums):
  """ This function is meant to return an Array (List) of the maximum and minmum of the inpt array 
  list_of_nums"""
  
  if max(list_of_nums) == min(list_of_nums): #for a list with identical numbers
    return [len(list_of_nums)]
  
  else:
    return [min(list_of_nums), max(list_of_nums)]