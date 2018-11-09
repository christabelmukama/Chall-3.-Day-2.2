#function fizzbuzz and the lists i will use
list_one = [10,11,15]
list_two = [1,3,5]
def fizzbuzz(first_list,second_list):
  merged_length = len(list_one) + len(list_two)
  print('merged_length')
  if merged_length % 3 ==0:
    print('fizz')
  elif merged_length % 5 ==0:
    print('buzz')
  elif merged_length % 5 == 0 and merged_length % 3 == 0:
    print('fizzbuzz')
  else:
    print('merged_length')

fizzbuzz(list_one,list_two)