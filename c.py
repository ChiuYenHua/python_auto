import os

#print(os.path.getsize("bird0.txt"))
timestamp = os.path.getmtime("bird0.txt")
import datetime

date = datetime.datetime.fromtimestamp(timestamp)
#
print(os.getcwd())
#os.mkdir("new_dir")
#os.chdir("/Users/qiuyanhua/Desktop/python_auto")
#print(os.getcwd())

#os.rmdir("new_dir")

#print(os.listdir())
