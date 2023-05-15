# Given a list of numbers, find the
    #largest,
    # smallest, and
    # second-largest
#list of numbers
  # Given a list of numbers, find the
    #largest,
    # smallest, and
    # second-largest
    #list of numbers
#James

def numberProperties(list):
    list = [3, 2, 1, 7, 29, 88, 65, 10, 4]
    largest = max(list)
    smallest = min(list)
    print ("The Largest number is: ")
    print (largest)
    print ("The Smallest number is: ")
    print (smallest)
    list.remove(largest)
    secondLargest = max(list)
    print ("The Second Largest number is: ")
    print(secondLargest)
numberProperties(list)