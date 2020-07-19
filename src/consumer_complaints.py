import sys
from datetime import datetime
input_args = sys.argv[1:]
print ("Files",input_args)
inputfile = input_args[0]
print (inputfile)
outputfile = input_args[1]

listoflines = []
with open(inputfile,'r') as in_f:
	line_col = in_f.readline()
	line_fs = in_f.readlines()
	for line_f in line_fs:
		listoflines.append(line_f)

fin_list = []
for line in listoflines:
	toggle = 0
	for i in range(len(line)):
		if toggle == 1 and line[i] == '"':
			toggle = 0
			continue
		if line[i] == '"':
			toggle = 1
			continue
		if toggle == 1:
			if line[i] == ",":
				line = line[0:i] + ":" + line[i+1:]
	fin_list.append(line)

years = []
products = []

companys = []
uniq_companys = []
for line in fin_list:
	line = line.split(",")
	l0 = datetime.strptime(line[0], "%Y-%m-%d")
	l0 = l0.year
	if l0 not in years:
		years.append(l0)
	if line[1] not in products:
		products.append(line[1])

print_list = []
for year in years:
	for product in products:
		companys = []
		uniq_companys = []
		for line in fin_list:
			line = line.split(",")
			l0 = datetime.strptime(line[0],"%Y-%m-%d")
			l0 = l0.year
			if year == l0 and product == line[1]:
				l2 = line[7]
				l2 = l2.lower()
				companys.append(l2)
				if l2 not in uniq_companys:
					uniq_companys.append(l2)
			
		len_comp = float(len(companys))
		len_ucomp = float(len(uniq_companys)) 
		try:
			percentage = round(len_ucomp / len_comp * 100)
			print_line = product.replace(":",",").lower() + "," + str(int(year)) + "," + str(int(len_comp)) + "," + str(int(len_ucomp)) + "," + str(int(percentage)) + "\n"
			print_list.append(print_line)
		except:
			continue
print_list.sort()

with open(outputfile,'a') as out_f:
	for line in print_list:
		out_f.write(line)
