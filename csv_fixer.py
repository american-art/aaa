import xlrd
import sys
import os
import json

filename = os.path.abspath(sys.argv[1])
filedir = filename[:filename.rfind(os.path.sep)]
filename = filename[filename.rfind(os.path.sep)+1:]

wb = xlrd.open_workbook(os.path.join(filedir,filename))
sh = wb.sheet_by_index(0)

fout = open(os.path.join(filedir,filename[:filename.index('.')]+'.json'),'w')

header = sh.row_values(0)

for i in range(1, sh.nrows):
	row = sh.row_values(i)
	if len(row) == len(header):            
	    js = {}
	    for j in range(len(header)):
	        js[header[j]] = row[j]
	    #pprint(js)   
	    fout.write(json.dumps(js))
	    fout.write("\n")
	    #print("Length: ", len(row), row) 
	    #print "\n\n\n"
	else:
	    print ("Some error with ",len(row), len(header))
	    for j in range(len(row)):
	        print(j, row[j])

fout.close()