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
no_of_lines_with_error = 0
no_of_blank_lines = 0

for i in range(1, sh.nrows):
	row = sh.row_values(i)
	if len(row) == len(header):            
	    js = {}
	    for j in range(len(header)):
	    	try:
	    		if int(row[j]) == row[j]:
	    			js[header[j]] = int(row[j])
	    	except:
	        	js[header[j]] = row[j] 
	    fout.write(json.dumps(js))
	    fout.write("\n")
	else:
	    if len(row) == 0:
	    	no_of_blank_lines += 1
	    else:
	    	no_of_lines_with_error += 1

print(no_of_blank_lines)
print(no_of_lines_with_error)

fout.close()