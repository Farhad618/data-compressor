code = input("enter the code: ")
div = int(input("Enter the division: "))
# code="1111 0000"
# div=4
out_code="0"*div
print("length before: {}".format(len(code)))
code=code.split(" ")

i=1

for x in code:
	k=0
	for y in range(len(out_code)):
		# print(x[y])
		if out_code[y]=="0" and k<4:
			temp=""
			for j in range(y):
				temp+=out_code[j]

			temp+="0" if x[k]=="0" else str(i)
			for j in range(y+1,len(out_code)):
				temp+=out_code[j]
			# print("temp:"+temp)
			out_code=temp
			k+=1
	for l in x[k:]:
		out_code+="0" if l=="0" else str(i)
	i+=1

print(out_code)
print("length before: {}".format(len(out_code)))