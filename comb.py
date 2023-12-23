class factorial(): #クラス版
    __slots__ = ['mod', '_fac', '_finv', '_inv', 'N']

    def __init__(self, mod, MAX=1):
        self.mod = mod
        self._fac = [1, 1]
        self._finv = [1, 1]
        self._inv = [None, 1]
        self.N = 1
        self.extend(MAX)
    
    def extend(self, MAX):
        self._fac.extend([0]*(MAX-self.N))
        self._finv.extend([0]*(MAX-self.N))
        self._inv.extend([0]*(MAX-self.N))
        for i in range(self.N+1, MAX+1):
            self._fac[i] = self._fac[i - 1] * i % self.mod
            self._inv[i] = self.mod - self._inv[self.mod%i] * (self.mod // i) % self.mod
            self._finv[i] = self._finv[i - 1] * self._inv[i] % self.mod
        self.N = MAX
    
    def comb(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        if self.N < n:
            self.extend(n)
        mod = self.mod
        return self._fac[n]*(self._finv[n-r]*self._finv[r] % mod) % mod

    def perm(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        if self.N < n:
            self.extend(n)
        return self._fac[n]*self._finv[n-r] % self.mod

    def fac(self, n):
        if self.N < n:
            self.extend(n)
        return _fac[n]

    def finv(self, n):
        if self.N < n:
            self.extend(n)
        return _finv[n]

    def inv(self, n):
        if self.N < n:
            self.extend(n)
        return _inv[n]

#非クラス版
_fac = [1, 1]
_finv = [1, 1]
_inv = [None, 1]

def extend(MAX):
    global _fac, _finv, _inv, mod
    N = len(_fac)-1
    _fac.extend([0]*(MAX-N))
    _finv.extend([0]*(MAX-N))
    _inv.extend([0]*(MAX-N))
    for i in range(N+1, MAX+1):
        _fac[i] = _fac[i - 1] * i % mod
        _inv[i] = mod - _inv[mod%i] * (mod // i) % mod
        _finv[i] = _finv[i - 1] * _inv[i] % mod
    N = MAX

def comb(n, r):
    global _fac, _finv, mod
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    if len(_fac) < n+1:
        extend(n)
    return _fac[n]*(_finv[n-r]*_finv[r] % mod) % mod

def perm(n, r):
    global _fac, _finv, mod
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    if len(_fac) < n+1:
        extend(n)
    return _fac[n]*_finv[n-r] % mod

def fac(n):
    global _fac
    if len(_fac) < n+1:
        extend(n)
    return _fac[n]

def finv(n):
    global _finv
    if len(_finv) < n+1:
        extend(n)
    return _finv[n]

def inv(n):
    global _inv
    if len(_inv) < n+1:
        extend(n)
    return _inv[n]