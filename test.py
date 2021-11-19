

import csv

# with open("suraj.csv","w") as f:
#     w = csv.writer(f)
#     w.writerow(["1","suraj"])
#     w.writerow(["2","sam"])

with open("suraj.csv",end="") as f:
    file = csv.reader(f)
    for row in file:
        print(row)