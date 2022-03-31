import csv

macInPath = '/Users/dro/Documents/kubyLOs.csv'
macOutPath = '/Users/dro/Documents/kubyLOs_edited.csv'
linuxInPath = '/home/dro/kubyScripts/kubyLOs.csv'#'/data/birc/home/pedrotirado/kubyScripts/kubyLOs.csv'
linuxOutPath = '/home/dro/kubyScripts/kubyLOs_edited.csv'#'/data/birc/home/pedrotirado/kubyScripts/kubyLOs_edited.csv'

with open(linuxInPath,newline='') as csvinput:
    with open(linuxOutPath,'w',newline='') as csvoutput:
        reader = csv.reader(csvinput, delimiter=',')
        writer = csv.writer(csvoutput, delimiter=',')

        all = []
        row = next(reader)

        for row in reader:

            curRow = row.__str__().lower()

            if "compare" in curRow or "contrast" in curRow:
                
                row.append("Analyze")

            elif ("offer" in curRow or "create" in curRow 
                or "provide" in curRow or "categorize" in curRow
                or "draw" in curRow or "formulate" in curRow
                or "propose" in curRow):

                row.append("Create")

            elif "evaluate" in curRow:

                row.append("Evaluate")

            elif ("apply" in curRow or "application" in curRow 
                or "predict" in curRow or "show why" in curRow):

                row.append("Apply")
                
            elif ("identify" in curRow or "outline" in curRow 
                or "articulate" in curRow):

                row.append("Remember")

            else: #elif "describe" in curRow or "understand" in curRow or "explain" in curRow:

                row.append("Understand")

            all.append(row)

        writer.writerows(all)
