s="Sorting1234"

print("".join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))))