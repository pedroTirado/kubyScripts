import csv

with open('/Users/dro/Documents/kubyLOs.csv',newline='') as csvinput:
    with open('/Users/dro/Documents/kubyLOs_edited.csv','w',newline='') as csvoutput:
        reader = csv.reader(csvinput, delimiter=',')
        writer = csv.writer(csvoutput, delimiter=',')

        all = []
        row = next(reader)

        for row in reader:
            if "identify" in row.__str__().lower():
                row.append("Remember")
            elif "describe" in row.__str__().lower() or "understand" in row.__str__().lower():
                row.append("Understand")

            all.append(row)
        writer.writerows(all)