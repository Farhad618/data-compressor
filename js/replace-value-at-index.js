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


console.log(replace_value_at_index("farhad", 5, "k"))

// export default replace_value_at_index;