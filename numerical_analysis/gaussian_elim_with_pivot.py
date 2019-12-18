import numpy as np

list1 = np.array([
            [1, 1, 0, 3, 4],
            [2, 1, -1, 1, 1],
            [3, -1, -1, 2, -3],
            [-1, 2, 3, -1, 4]
            ])

list2 = np.array([
                [58.9, 0.03, 59.2],
                [-6.10, 5.31, 47.0],
                ])
def solve_linear(a):
    a = a.astype(float)
    N = len(a)
    
    solution = np.zeros(N)
    
    
    for j in range(N):
        
        # switching process
        has_sol = 0
        for i in range(j, N):
            if a[i][j] == 0:
                continue
            else:
                a[[j, i]] = a[[i, j]]
                has_sol = 1
                break
        if has_sol == 0:
            print('No unique solution!')
            break
        
        # pivoting process
        scale_list = np.zeros(N-j)
        print(a)
        for i in range(j, N):
            max_a = max(abs(a[0:N, i]))
            scale_list[i-j] = a[i, j]/max_a
        ind = np.where(abs(scale_list) == max(abs(scale_list)))[0][0]
        a[[j, ind + j]] = a[[ind + j, j]]
        print(a)
        print("\n")
        
        # eliminating process
        for i in range(j+1, N):
            ratio = a[i][j]/a[j][j]
            a[i] = a[i] - ratio*a[j]
    
    if a[N-1][N-1] == 0:
        print('No unique solution!')
    for i in range(N):
        a[i] = a[i]/(a[i][i])
    
    solution[N-1] = a[N-1][N]

    for i in range(N-2, -1, -1):
        summ = 0
        
        for j in range(i+1, N):
            summ += solution[j]*a[i][j]
        solution[i] = a[i][N] - summ
    return list(solution)

solution = solve_linear(list1)
print(solution)
        
        
        
    


        