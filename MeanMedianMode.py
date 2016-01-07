#Find the Mean Meadian and Mode of inputed numbers

def  main():
  #Get the numbers
  user_input = raw_input("Find the Mean, Median, and Mode of: ")
  numbers = user_input.split(" ")
  
  #sort numbers
  numbers.sort()
  
  averages(numbers)

#finds the mean median and mode using helper functions
def  averages(numbers):
  length = len(numbers)
  num_sum = 0.
  for num in numbers:
    num_sum = num_sum + int(num)
    
  avg = num_sum / length
  
  mode_list = count(numbers)
  mode_sorted = sorted(mode_list.items(), key = get_count, reverse = True)
  mode = mode_sorted[
  
  median = 0.
  if length % 2 == 0:
    median = (int(numbers[length / 2]) + int(numbers[(length / 2) - 1])) / 2
  else:
    median = int(numbers[(length - 1) / 2])
    
  print("Your mean is: " + str(avg) + ", your median is: " + str(median) + ", and your mode is: " + str(mode[0].))  
  	  
#gets how many times the number appears
def  count(numbers):
  count = {}
  for num in numbers:
    if not num in count:
      count[num] = 1
    else:
      count[num] = count[num] + 1

  return count
  
#gets the count from the dict count
def  get_count(count):
  return count[1]
  
      
if __name__ == '__main__':
  main()
