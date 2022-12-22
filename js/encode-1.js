function replace_value_at_index(str, index, value) {
	temp=""
	/*for (var i = 0; i < str.length; i++) {
		if (i==index) {
			temp+=value
		} else {
			temp+=str[i]
		}
	}*/
	temp+=str.slice(0,index)
	temp+=value
	temp+=str.slice(index+1)
	return temp
}


let code="1000110 1000001 1010010 1001000 1000001 1000100"
let div=7

code = code.split(" ")
// console.log(code)
let out_code="".padStart(div, "0")
let i=1

for (let x of code){
	// console.log("x: "+ x)
	let k=0
	for (var o = 0; o < out_code.length; o++) {
		temp=""
		if (out_code[o]=="0") {
			if (x[k]=="1") {				
				out_code=replace_value_at_index(out_code, o, i)
				// console.log("out_code: "+out_code)
			} 
			k++
		}
	}
	if (k<div) {
		out_code+=x.slice(k).replaceAll("1", i)
	}
	i++
}

console.log(out_code)
