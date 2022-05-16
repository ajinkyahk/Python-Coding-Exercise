import re
text = "I am [name]"
name = "Ajinkya"
pattern = r"(\[\w*\])"
print(re.sub(pattern, name, text))