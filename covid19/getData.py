import  urllib.request,csv
url = 'https://od.cdc.gov.tw/eic/Day_Confirmation_Age_County_Gender_19CoV.csv'
webpage = urllib.request.urlopen(url)  #開啟網頁
data = csv.reader(webpage.read().decode('utf-8').splitlines()) #讀取資料到data陣列中

with open('covid_file.csv', 'w+') as output_file:
                writer = csv.writer(output_file)
                for i in data:
                    writer.writerow(i)
                output_file.close()
