# Writing a function to open a file

def open_file(x):
    try:
        fp = open(x, "r")
        print(fp.read())
    except:
        print("something went wrong")
    finally:
        print("close the file")
        fp.close()

open_file(r"C:\Users\homiv\PySaprkProject\FirstPythonProject\data\Netflix_Dataset_Rating.csv")