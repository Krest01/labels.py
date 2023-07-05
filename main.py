# Task 1

def palindrom(s):
    for i in range(0, len(s)):
        if s[i] == s[i + 1]:
            return True
    return False


string = 'mrwalollkaru'
if palindrom(string):
    print('This string contains palindrome')
else:
    print('This string doesnt contain palindrome')

# Task 2

NO_OF_CHARS = 256


def badCharHeuristic(string, size):
    badChar = [-1]*NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def search(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            print(f"Pattern occur at index = {s}")
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])


text = 'kaorukaku'
pattern = 'uk'
search(text, pattern)

# Task 3

number = int(input("Proszę podać liczbę "))
system = int(input('Proszę podać system końcowy '))
alphabet = 'ABCDEFGHIJKLMNOPRSTQUWVXYZ'
dict = {letter:idx for idx, letter in enumerate(alphabet, start=10)}
reszta = []
while number != 0:
    reszta.append(number % system)
    number = number // system
reszta.reverse()
for i in reszta:
    for key in dict:
        value = dict[key]
        if i == dict[key]:
            reszta[i-10] = key
print(reszta)
# Task 4

