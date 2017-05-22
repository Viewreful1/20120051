s = raw_input().split()
v = [[]]
num = int(s[0])
start = int(s[2])
for i in range(1,num+1):
    v.append([])

for i in range(int(s[1])):
    t = raw_input().split()
    v[int(t[0])].append(int(t[1]))
    v[int(t[1])].append(int(t[0]))

df = []
bf = []

for i in range(len(v)):
    v[i].sort()

def dfs(a):
    if len(df) == num:
        for j in df: 
            print j,
        return
    tmp = a 
    for i in tmp:
        if i not in df: 
            df.append(i)
            dfs(v[i]) 

def bfs(a):
    if len(bf) == num:
        for j in bf: 
            print j,
        return
    tmp = a 
    tmpv = []
    for i in tmp:
        if i not in bf: 
            bf.append(i)
        for j in v[i]:
            if j not in bf: 
                tmpv.append(j)
    bfs(tmpv)


dfs([start])
print
bfs([start])
