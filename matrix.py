class matrix:
    def __init__(self, r, c, ID=0):
        self.r = r
        self.c = c
        self.data = [[0]*c for _ in range(r)]
        if ID:
            if r != c:
                raise Exception("Error! r: "+str(r)+" != c: "+str(c))
            for i in range(r):
                self.data[i][i] = ID

    def __add__(self, other):
        r1 = self.r
        c1 = self.c
        r2 = other.r
        c2 = other.c

        if r1 != r2:
            raise Exception("Error! r1: "+str(r1)+" != r2: "+str(r2))
        if c1 != c2:
            raise Exception("Error! c1: "+str(c1)+" != c2: "+str(c2))
        
        for i in range(r1):
            for j in range(r2):
                self[i][j] += other[i][j]
                self[i][j] %= mod

        return self
    
    def __radd__(self, other):
        return self+other

    def __mul__(self, other):
        r1 = self.r
        c1 = self.c

        if type(other) == int:
            ret = self
            for i in range(r1):
                for j in range(c1):
                    ret.data[i][j] *= other
                    ret.data[i][j] %= mod

        else:
            r2 = other.r
            c2 = other.c
            if c1 != r2:
                raise Exception("Error! c1: "+str(c1)+" != r2: "+str(r2))
            ret = matrix(r1, c2)
            for i in range(r1):
                for k in range(c1):
                    for j in range(c2):
                        ret.data[i][j] += self.data[i][k] * other.data[k][j]
                        ret.data[i][j] %= mod

        return ret

    def __rmul__(self, other):
        return self*other
    
    def __pow__(self, n):
        r = self.r
        c = self.c
        x = self
        if r != c:
            raise Exception("Error! r: "+str(r)+" != c: "+str(c))
        ret = matrix(r, c, 1)
        while n:
            if n & 1:
                ret *= x
            x *= x
            n >>= 1
        return ret
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __str__(self):
        return "\n".join([" ".join(map(str, self.data[i])) for i in range(self.r)])