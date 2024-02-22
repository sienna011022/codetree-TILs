n ,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

rogic = [0,1,2,3]
def count(x,y,direction):

    if direction == 0:
        return graph[x][y] + graph[x+1][y] + graph[x+1][y+1]
    elif direction == 1:
        return graph[x][y] + graph[x][y+1]+ graph[x+1][y]
    elif direction == 2:
        return graph[x][y] + graph[x][y+1] + graph[x+1][y+1]
    elif direction == 3:
        return graph[x][y+1] + graph[x+1][y] + graph[x+1][y+1]

ans = 0
for i in range(n):
    for j in range(m):
        for direction in range(4):
            if i < n-1 and j < m-1:
                ans = max(ans,count(i,j,direction))

for i in range(n):
    for j in range(m):
        if j < m-2 :
        
            ans = max(ans,graph[i][j] + graph[i][j+1] + graph[i][j+2])

for j in range(m):
    for i in range(n):
        if i < n-2 : 
             
            ans = max(ans,graph[i][j] + graph[i+1][j] + graph[i+2][j])



print(ans)