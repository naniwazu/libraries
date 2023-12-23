# https://qiita.com/keymoon/items/11fac5627672a6d6a9f6 より

MASK30 = (1 << 30) - 1
MASK31 = (1 << 31) - 1
MOD = (1 << 61) - 1
MASK61 = MOD
POSITIVIZER = MOD * 4
base = 37

def Mul(a, b): #a * b % (2**61-1)を高速で計算
    au = a >> 31
    ad = a & MASK31
    bu = b >> 31
    bd = b & MASK31
    mid = ad * bu + au * bd
    midu = mid >> 30
    midd = mid & MASK30
    return au * bu * 2 + midu + (midd << 31) + ad * bd # 計算結果はMOD*4未満

def CalcMod(x):
    xu = x >> 61
    xd = x & MASK61
    res = xu + xd
    if res >= MOD:
        res -= MOD
    return res

def RollingHash(s):
    l = len(s)
    hash = [0]*(l+1)
    for i in range(l):
        hash[i+1] = CalcMod(Mul(hash[i],  base) + ord(s[i]))
    return hash

# あらかじめ必要な長さの最大値分のPowMemoを計算しておく
def setup_PowMemo(l):
    global PowMemo
    PowMemo = [1]*(l+1)
    for i in range(l):
        PowMemo[i+1] = CalcMod(Mul(PowMemo[i], base))

def get(hash, l, r):
    return CalcMod(hash[r] + POSITIVIZER - Mul(hash[l], PowMemo(r - l)))