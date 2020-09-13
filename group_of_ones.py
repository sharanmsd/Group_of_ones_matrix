def dfs(l,i,j,r,c):
    if((i<0)or(j<0)or(i>=r)or(j>=c)or(l[i][j]==0)):
        return
    l[i][j]=0
    dfs(l,i-1,j,r,c)
    dfs(l,i+1,j,r,c)
    dfs(l,i,j+1,r,c)
    dfs(l,i,j-1,r,c)

r,c=map(int,input().split())
l=[]
for i in range(r):
    x=list(map(int,input().split()))
    l.append(x)
cnt=0
for i in range(r):
    for j in range(c):
        if(l[i][j]==1):
            # cnt+=1
            dfs(l,i,j,r,c)
            cnt+=1
print(cnt)
