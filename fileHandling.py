
# open file using open() method

movie = open(r"C:\Users\homiv\PySaprkProject\FirstPythonProject\data\Netflix_Dataset_Movie.csv", "r")
# for i in movie:
#     print(i)
#
#
# movie.close()

# by uisng with function we dont need to close the file

with movie as f:
    print(f.read())


# Writing the file
print("Writing the file from another file")
write_file = open(r"C:\Users\homiv\PySaprkProject\FirstPythonProject\data\movie.csv", "w")


# read file
ratings = open(r"C:\Users\homiv\PySaprkProject\FirstPythonProject\data\Netflix_Dataset_Rating.csv", "r")
with ratings as f:
    # Write the rating in new file
    write_file.write(f.read())

# once we write we have open that file in read mode to read it
wf = open(r"C:\Users\homiv\PySaprkProject\FirstPythonProject\data\movie.csv", "r")
print(wf.read())

write_file.close()
ratings.close()
wf.close()

# Delete the file
# first thing we have to do it is import os
print("deleting the file")
import os

if os.path.exists("C:/Users/homiv/PySaprkProject/FirstPythonProject/data/movie.csv"):
    os.remove("C:/Users/homiv/PySaprkProject/FirstPythonProject/data/movie.csv")
else:
    print("file not found")
