import math
from re import X


myList = [0 , -5,9,-6,2]
# y = [abs(x) for x in myList]
# print(y)
# for n in myList:
#     if n < 0:
#         y += [-n]
#     else:
#         y.append(n)



y = [-x if x < 0 else X for x in myList]

print(y)