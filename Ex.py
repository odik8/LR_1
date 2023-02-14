f1 = 1
z = 2
Et = 5
print(f'''f1 = {f1}, type(f1): {type(f1)}
z = {z}, type(z): {type(z)}
Et = {Et}, type(Et): {type(Et)}
''')
ch = (6 // f1) * z + z * f1 - ((f1 + Et) // 6)
print(f"ch = {ch}")
print(f"type(ch): {type(ch)}")
