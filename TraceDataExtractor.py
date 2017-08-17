import numpy as np
import csv as csv
import sys


arg=sys.argv
counter=0
with open(arg[1], "r") as trace:
	for line in trace:
		counter=counter+1
		parts = line.split(":")
		op_addr = parts[2].split(" ")
		if (counter==1):
			inicial=int(parts[0])
		if ("Read" in op_addr):
			i = op_addr.index("address")
			print("%d %s %s" %((int(parts[0])-inicial)/500,op_addr[i+1],"READ"))
			#print(int(parts[0])-inicial,op_addr[i+1],"READ",)
		if ("Write" in op_addr):
			i = op_addr.index("address")
			print("%d %s %s" %((int(parts[0])-inicial)/500,op_addr[i+1],"WRITE"))
			#print(int(parts[0])-inicial,op_addr[i+1],"WRITE",)
		if ("IFetch" in op_addr): 
			i = op_addr.index("address")
			print("%d %s %s" %((int(parts[0])-inicial)/500,op_addr[i+1],"READ"))
#			print(parts[0],op_addr[i+1],"IFetch",)

