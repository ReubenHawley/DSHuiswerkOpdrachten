list = [35, 10, 12, 30, 17, 0, 45, 18, 18, 12, 30, 0, 5, 40, 10]
sumOfList = 0
for number in list:
    sumOfList += number
print(sumOfList / len(list))

listOfVisitors = [48, 50, 52, 49, 45, 47, 49, 55, 60, 45, 50, 51, 53, 47, 60, 60, 35, 45, 47, 38, 40, 50, 49, 46, 43,
                  47]

listOfVisitors.sort()
highest = max(listOfVisitors)
lowest = min(listOfVisitors)
distribution = highest-lowest
print(f"Distribution is: {distribution}")


import os
path = os.path.normpath(os.getcwd())
filename= "knmi_data.txt"
full_path = os.path.join(path,filename)
print(full_path)
