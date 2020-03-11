import csv

def main():
    with open('coinmarket.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter='|')
        with open('data.csv', 'w') as c:
            cwriter = csv.writer(c, delimiter='|')
            i = 0
            l = list()
            for row in data:
                for word in row:
                    if(i==5):
                        i+=1
                    elif(i==6):
                        cwriter.writerow(l)
                        l = list()
                        i=0
                    else:
                        l.append(word)
                        i+=1
main()