s = input("Enter text: ")
se = s.count(".") + s.count("?")
w = s.count(' ') + 1
c = len(s)
l = c - se
print("sentence: " , se)
print("words: " , w)
print("characters: " , c)
print("letters: " , l)

x = input(" Enter your character: ")
print(ord(x))

n = input("Enter your number: ")
n = n.isnumeric()
print(n)