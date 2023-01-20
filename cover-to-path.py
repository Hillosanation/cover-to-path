# coding=utf-8
import csv
import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--csv-path", default="cover.csv")
parser.add_argument("--unglued-fumen-script-path", default=r"..\forks\GluingFumens\unglueFumen.js")
args = parser.parse_args(sys.argv[1:])

InputCSV = []
for row in csv.reader(open(args.csv_path, 'r')):
    InputCSV.append(row)
# print(InputCSV)

open("temp_gluedfumens.txt", "w").write("\n".join(InputCSV[0][1:]))

os.system(fr'node {args.unglued_fumen_script_path} --fp ".\temp_gluedfumens.txt" --op ".\temp_ungluedfumens.txt"') #calls unglueFumen

ungluedRow = open("temp_ungluedfumens.txt", "r").read().split("\n")
# print(ungluedRow)

OutputCSV = []
OutputCSV.append(["pattern", "solutionCount", "solutions", "unusedMinos", "fumens"]) #QoL, not read by strict-minimal

for row in InputCSV[1:]: 
    sequence = row[0]
    SuccessFumens = []
    for element, fumen in zip(row[1:], ungluedRow):
        if (element == 'O'):
            SuccessFumens.append(fumen)
            # print(SuccessFumens)
    OutputCSV.append([sequence, len(SuccessFumens), '', '', ";".join(SuccessFumens)])
# print(OutputCSV)

extentionPos = args.csv_path.find(".csv")
OutputFilePath = args.csv_path[:extentionPos] + "_to_path" + args.csv_path[extentionPos:]
print(f"writing to file: {OutputFilePath}")
OutputFileWriter = csv.writer(open(OutputFilePath, 'w', newline=''))
for row in OutputCSV:
    OutputFileWriter.writerow(row)
