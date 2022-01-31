
from itertools import zip_longest

def combineList(l1,l2):
   res = [ele for sub in zip_longest(l1, l2) for ele in sub if ele]
   print("Expected Result: ")
   print(res)


print("Case 1: ")
strList1 = input("Please enter 3 digits of alphabet: ")
strList2 = input("Please enter 3 digits of integer: ")
combineList(sorted(strList1), sorted(strList2))
