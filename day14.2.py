text="    python programming      "
text1= "I study in GLA university"
#removing leading and trailing whitespace
trimmed_text=text.strip()
print(trimmed_text)
#convert to lowercase and uppercase
lower_case=text.lower()
upper_case=text.upper()
print("lowecase",lower_case)
print("uppercase",upper_case)
#replace
replaced_text=text.replace("programming","coding")
print(replaced_text)
#find substring
index=text1.find("GLA")
print("Index of'GLA':",index)