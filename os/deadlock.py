    n = 5 
    m = 3 
    alloc = [[0, 1, 0 ],[ 2, 0, 0 ],
            [3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]]
    
  
    max = [[7, 5, 3 ],[3, 2, 2 ],
            [ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]]
    
    avail = [3, 3, 2] 
    
    f = [0]*n
    ans = [0]*n
    ind = 0
    need = [[ 0 for i in range(m)]for i in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max[i][j] - alloc[i][j]
    
    while True:
        found = False
        for i in range(n):
            if f[i] == 0:
                flag = True
                for j in range(m):
                    if need[i][j] > avail[j]:
                        flag = False
                        break
                if flag:
                    ans[ind] = i
                    ind += 1
                    for y in range(m):
                        avail[y] += alloc[i][y]
                    f[i] = 1
                    found = True
                    break
        if not found:
            break
    
    print("it is safe sequence")
