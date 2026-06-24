# ==================================================

# 1. REVERSE WORDS IN A STRING

# ==================================================

n = input()
l = n.split()
new = l[::-1]
print(' '.join(new))

# ==================================================

# 2. BALANCED STRING SPLIT

# ==================================================

s = input()

c = 0
l = 0
r = 0

for ch in s:

```
if ch == 'L':
    l += 1

if ch == 'R':
    r += 1

if l == r:
    c += 1
```

print(c)

# ==================================================

# 3. INTEGER BREAK (MAXIMUM PRODUCT)

# ==================================================

n = int(input())

if n == 2:
print(1)

elif n == 3:
print(2)

else:

```
p = 1

while n > 4:
    p = p * 3
    n = n - 3

p = p * n

print(p)
```

# ==================================================

# 4. DECRYPT STRING FROM ALPHABET TO INTEGER MAPPING

# ==================================================

s = input()

s1 = ""

i = len(s) - 1

while i >= 0:

```
if s[i] == '#':

    s1 = s1 + chr(96 + int(s[i-2:i]))
    i = i - 3

else:

    s1 = s1 + chr(96 + int(s[i]))
    i = i - 1
```

print(s1[::-1])

# ==================================================

# 5. CAN PLACE FLOWERS

# ==================================================

n = int(input())

l = list(map(int, input().split()))

p = int(input())

c = 0

for i in range(len(l)):

```
if i == 0:
    le = 0
else:
    le = l[i-1]

if i == len(l)-1:
    ri = 0
else:
    ri = l[i+1]

cu = l[i]

if le == 0 and ri == 0 and cu == 0:

    l[i] = 1
    c += 1
```

if c >= p:
print("yes")
else:
print("no")

# ==================================================

# 6. CHECK IF ONE STRING IS A SUBSEQUENCE OF THE OTHER

# ==================================================

s1 = input().strip()
s2 = input().strip()

def check(big, small):

```
j = 0

for i in range(len(big)):

    if j < len(small) and big[i] == small[j]:
        j += 1

return j == len(small)
```

if check(s1, s2) or check(s2, s1):
print("yes")
else:
print("no")

# ==================================================

# 7. CONTAINER WITH MOST WATER

# ==================================================

n = int(input())

l = list(map(int, input().split()))

i = 0
j = len(l) - 1

m = 0

while i < j:

```
w = j - i
h = min(l[i], l[j])

area = w * h

if area > m:
    m = area

if l[i] > l[j]:
    j -= 1
else:
    i += 1
```

print(m)

# ==================================================

# 8. REMOVE STARS FROM STRING

# ==================================================

s = input()

l = []

for i in range(len(s)):

```
if s[i] == '*':

    if l:
        l.pop()

else:
    l.append(s[i])
```

print(''.join(l))

# ==================================================

# 9. MINIMUM FLIPS TO MAKE (A OR B) = C

# ==================================================

a, b, c = map(int, input().split())

f = 0

while a > 0 or b > 0 or c > 0:

```
abit = a % 2
bbit = b % 2
cbit = c % 2

if cbit == 0:

    if abit == 1 and bbit == 1:
        f += 2

    elif abit == 1 or bbit == 1:
        f += 1

if cbit == 1:

    if abit == 0 and bbit == 0:
        f += 1

a //= 2
b //= 2
c //= 2
```

print(f)

# ==================================================

# 10. UGLY NUMBER

# ==================================================

n = int(input())

while n % 2 == 0:
n = n // 2

while n % 3 == 0:
n = n // 3

while n % 5 == 0:
n = n // 5

if n == 1:
print("yes")
else:
print("no")
# ==================================================

# 11. SEARCH INSERT POSITION

# ==================================================

n = int(input())

l = list(map(int, input().split()))

t = int(input())

if t not in l:
l.append(t)
l.sort()

for i in range(len(l)):

```
if t == l[i]:
    e = i
```

print(e)

# ==================================================

# 12. COUNT INTEGERS BEFORE

# ==================================================

n = input()

l = list(map(int, input().split()))

m = l[:]

l.sort()

d = {}

for i in range(len(l)):

```
if l[i] not in d:
    d[l[i]] = i
```

for x in m:
print(d[x], end=' ')

# ==================================================

# 13. SHUFFLE STRING

# ==================================================

n = input()

s = list(n)

m = [''] * len(s)

l = list(map(int, input().split()))

for i in range(len(l)):
m[l[i]] = s[i]

print(''.join(m))

# ==================================================

# 14. SORT STRINGS BY LENGTH AND CONCATENATE

# ==================================================

n = int(input())

l = []

for i in range(n):

```
a = input().strip()

l.append(a)
```

l.sort(key=len)

x = ''.join(l)

print(x)

# ==================================================

# 15. WATER BOTTLES

# ==================================================

a, b = map(int, input().split())

m = a

while a >= b:

```
n = a // b

m = m + n

r = a % b

a = n + r
```

print(m)
# ==================================================

# 16. RANK INTEGERS IN ARRAY

# ==================================================

n = int(input())

l = list(map(int, input().split()))

s = l[:]

l.sort()

d = {}

r = 1

for i in range(len(l)):

```
if l[i] not in d:
    d[l[i]] = r
    r += 1
```

for x in s:
print(d[x], end=" ")

# ==================================================

# 17. MAXIMUM SINGLE SWAP

# ==================================================

n = input().strip()

l = list(n)

for i in range(len(l)-1):

```
m = max(l[i+1:])

if m > l[i]:

    for j in range(len(l)-1, i, -1):

        if l[j] == m:
            break

    l[i], l[j] = l[j], l[i]

    break
```

print(''.join(l))

# ==================================================

# 18. SMALLEST NUMBER WHOSE BINARY HAS ONLY 1s

# ==================================================

n = int(input())

i = 0

while True:

```
e = (2 ** i) - 1

i += 1

if e >= n:
    ans = e
    break
```

print(ans)

# ==================================================

# 19. ONE STRING SWAP

# ==================================================

s1 = input().strip()

s2 = input().strip()

d = []

if s1 == s2:

```
print("true")
```

else:

```
for i in range(len(s1)):

    if s1[i] != s2[i]:
        d.append(i)

if len(d) != 2:

    print("false")

elif s1[d[0]] == s2[d[1]] and s1[d[1]] == s2[d[0]]:

    print("true")

else:

    print("false")
```

# ==================================================

# 20. RANSOM NOTE

# ==================================================

s1 = input().strip()

s2 = input().strip()

d = {}

for c in s2:
d[c] = d.get(c, 0) + 1

a = True

for c in s1:

```
if c not in d or d[c] == 0:
    a = False
    break

d[c] = d[c] - 1
```

if a:
print("true")
else:
print("false")
# ==================================================

# 21. PREFIX STRING OF WORDS

# ==================================================

s1 = input().strip()

l = []

s = ""

a = False

n = int(input())

for i in range(n):
l.append(input())

for j in range(len(l)):

```
s = s + l[j].strip()

if s == s1:
    a = True
    break
```

if a:
print("true")
else:
print("false")

# ==================================================

# 22. SORT NAMES BASED ON HEIGHTS

# ==================================================

n = int(input())

l = []

s = []

ans = []

for i in range(n):
l.append(list(input().split()))

for j in range(len(l)):

```
e = l[j]

s.append(int(e[-1]))
```

s.sort(reverse=True)

for h in s:

```
for e in l:

    if h == int(e[-1]):
        ans.append(e[0])
```

for m in range(len(ans)):
print(ans[m])

# ==================================================

# 23. MINIMUM SWAPS TO MAKE ALL 1's CONTIGUOUS

# ==================================================

n = input()

l = list(n)

s1 = []

s2 = []

s3 = []

for i in range(len(l)):

```
if l[i] == '1':
    s1.append(i)
```

for j in range(len(s1)):

```
e = s1[j] - j

s2.append(e)
```

m = len(s2) // 2

for k in range(len(s2)):

```
d = abs(s2[k] - s2[m])

s3.append(d)
```

print(sum(s3))

# ==================================================

# 24. POWER OF STRING

# ==================================================

n = input().strip()

m = 1

c = 1

for i in range(len(n)-1):

```
if n[i] == n[i+1]:

    c += 1

    m = max(m, c)

else:

    c = 1

    m = max(m, c)
```

print(m)

# ==================================================

# 25. FAULTY KEYBOARD

# ==================================================

s1 = input().strip()

s2 = ""

for c in s1:

```
if c != 'i':

    s2 = s2 + c

else:

    s2 = s2[::-1]
```

print(s2)
# ==================================================

# 26. PERCENTAGE OF CHARACTER

# ==================================================

s1 = input().strip()

s2 = input().strip()

l = len(s1)

co = 0

for c in s1:

```
if c == s2:
    co += 1
```

ans = (co / l) * 100

print(int(ans))

# ==================================================

# 27. MAXIMUM SCORE AFTER SPLITTING A BINARY STRING

# ==================================================

n = input().strip()

m = 0

l = 0

r = 0

for i in range(len(n)):

```
if n[i] == '1':
    r += 1
```

for j in range(len(n)-1):

```
if n[j] == '0':
    l += 1

else:
    r -= 1

if m < l + r:
    m = l + r
```

print(m)

# ==================================================

# 28. PATH CROSSING

# ==================================================

n = input().strip()

x = 0

y = 0

l = []

l.append((x, y))

ans = False

for c in n:

```
if c == 'N':
    y += 1

if c == 'S':
    y -= 1

if c == 'E':
    x += 1

if c == 'W':
    x -= 1

p = (x, y)

if p in l:
    ans = True
    break

else:
    l.append(p)
```

if ans:
print("true")
else:
print("false")

# ==================================================

# 29. LENGTH TWO SUB-ARRAYS EQUAL SUM

# ==================================================

n = int(input())

l = list(map(int, input().split()))

ans = set()

c = False

for i in range(len(l)-1):

```
s = l[i] + l[i+1]

if s in ans:
    c = True

else:
    ans.add(s)
```

if c:
print("true")
else:
print("false")

# ==================================================

# 30. FIND ELEMENT USING GIVEN INDEX AFTER SORTING

# ==================================================

l = list(map(int, input().split()))

k = int(input())

l.sort()

print(l[k-1])
