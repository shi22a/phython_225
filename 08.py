

S = "banana"
n = len(S)

# consonents
stuart = 0

# vowels
kevin = 0

for i in range(n):
    if S[i] in ('a', 'e', 'i', 'o', 'u'):
        kevin += n - i
    else:
        stuart += n - i
print(stuart)



