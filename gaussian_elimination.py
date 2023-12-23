class matrix:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.data = [[0]*c for _ in range(r)]


    def gaussian_elimination(self):
        eps = 10e-6
        r = self.r
        c = self.c
        data = self.data
        cur = 0
        for j in range(c):
            for i in range(cur, r):
                if abs(data[i][j]) > eps:
                    data[i], data[cur] = data[cur], data[i]
                    pivot = data[cur][j]
                    for k in range(j, c):
                        data[cur][k] /= pivot
                    for l in range(r):
                        if l != cur:
                            for k in range(j, c)[::-1]:
                                data[l][k] -= data[cur][k]*data[l][j]
                    cur += 1
                    break
    
    def rank(self):
        eps = 10e-6
        self.gaussian_elimination()
        for i in range(self.r):
            for j in range(self.c):
                if abs(self.data[i][j]) > eps:
                    break
            else:
                return i
        return self.r
 
    def __getitem__(self, key):
        return self.data[key]
    
    def __str__(self):
        return "\n".join([" ".join(map(str, self.data[i])) for i in range(self.r)])

A = matrix(4, 3)
A.data = [[1, 2, 2], [2, 3, 4], [-1, 1, -2], [3, 0, 6]]
print(A.rank())
print(A)