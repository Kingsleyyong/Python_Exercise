def calculateSum (loopCount):
   sum = 0
   for i in range(loopCount):
      if (i%3==0 or i%5==0):
         sum += i

   return sum

print( calculateSum(1000))
