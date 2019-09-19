import csv
filepath="cities.csv"
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    outstring = ""
    count = 0
    while True:
        try:
            line = next(csvreader)
            outstring += "<tr>"
            for element in line:
                if count>0:
                    outstring += "<td>"+element+"</td>"
                else:
                    outstring += "<th>"+element+"</th>"
            outstring += "</tr>\n"
            count += 1
        except:
            break
#outstring = f"{count}"
#print(outstring)
f = open("cities-html.txt", "w")
f.write(outstring)
f.close()