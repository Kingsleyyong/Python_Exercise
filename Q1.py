def calculateCharges(hours, minutes):
   price = 0
   
   if (hours == 24):
      price = 20.00

   elif(hours != 0 and minutes == 0):
      price = hours

   elif (hours != 0 and minutes > 0 ):
      price = hours + 1.00

   return price

for i in range(3):
   print("Case {}: ".format(i+1))
   duration = input("Input: ")
   hourMinute  = [int(s) for s in duration.split() if s.isdigit()]
   print("Expected Result: RM %.2f" % (calculateCharges(hourMinute[0], hourMinute[1])))


