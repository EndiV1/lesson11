file_path = "C:/Users/Student/Desktop/lesson11/leximi.txt"
#file = open(file_path, "r")
## line1 = file.readline()
  # print(line1)

#with open(file_path, "w") as file:
# #file.write("hello world")

with open(file_path, "w") as file:
    file.write("hello world")
    file.seek(20)
    print(file)




