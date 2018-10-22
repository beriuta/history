from collections import  Counter
word = 'this is for the test of Counter class'.split()
cnt = Counter()
for i in word:
    cnt[i] += 1
print(cnt)