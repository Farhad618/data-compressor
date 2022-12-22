# code = input("enter the code: ")
# div = int(input("Enter the division: "))
code="1000110 1000001 1010010 1001000 1000001 1000100"
div=7
out_code="0"*div
print("length before: {}".format(len(code)))
code=code.split(" ")

i=1

for x in code:
	k=0
	for o in range(len(out_code)):
		temp=""
		if out_code[o]=="0":
			if x[k]=="1":
				temp+=out_code[0:o]
				temp+=str(i)
				temp+=out_code[o+1:]

				out_code=temp
			k+=1
	if k<div:
		out_code+=x[k:].replace("1", str(i))
	i+=1

		

print(out_code)
print("length before: {}".format(len(out_code)))