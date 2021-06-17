with open("abc.txt") as file:
    lines = file.readlines()

for i in range(5):
    with open("pig"+str(i)+".txt","w") as file:
        file.write("She is a girl\nHe is a boy")
