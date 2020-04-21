import os
import sys
begin=open("template/begin.html","r").readlines()
end=open("template/end.html","r").readlines()
srcs=["index"]

for i in srcs:
	if os.path.isfile("{}/.html".format(i)):
		os.unlink("{}/.html".format(i))
	content=open("src/{}.html".format(i),"r").readlines()
	output=open("{}.html".format(i),"w")
	for j in begin:
		output.write(j)
	for j in content:
		output.write(j)
	for j in end:
		output.write(j)
	output.close()

