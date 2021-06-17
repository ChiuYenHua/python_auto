import csv

f = open("military.csv", encoding = "Big5")
csv_f = csv.reader(f)
for row in csv_f:
    SeqNo,Annual,ItemName,Category,Percentage ,Author,IssueDate,URL = row
    print("SeqNo:{} Annual:{} ItemName:{} Category:{} Percentage:{} Author:{} IssueDate:{} URL:{}".format(SeqNo,Annual,ItemName,Category,Percentage ,Author,IssueDate,URL))
ˇˇ
