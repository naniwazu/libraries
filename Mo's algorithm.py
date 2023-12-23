class Mo():
    """
    Mo's algorithmを実行する。区間は半開区間[l, r)として扱う。
    """
    def __init__(self, N):
        self.N = N
        self.Q = 0
        self.queries = []
        self.cur_l = 0
        self.cur_r = 0
    
    def add_query(self, l, r):
        self.queries.append((l, r, self.Q))
        self.Q += 1
    
    def sort_queries(self):
        INF = 10**9
        bsize = self.N // min(self.N, int(self.Q**0.5))
        self.queries.sort(key = lambda x:x[0]//bsize*INF+((x[0]//bsize)%2*2-1)*x[1])
    
    def add(self, idx):
        pass # ここに処理を書く

    def erase(self, idx):
        pass # ここに処理を書く

    def build(self):
        self.sort_queries()
        self.ans = [None]*self.Q
        cur_l = self.cur_l
        cur_r = self.cur_r
        self.sort_queries()
        for l, r, i in self.queries:
            while cur_l > l:
                self.add(cur_l-1)
                cur_l -= 1
            while cur_r < r:
                self.add(cur_r)
                cur_r += 1
            while cur_l < l:
                self.erase(cur_l)
                cur_l += 1
            while cur_r > r:
                self.erase(cur_r-1)
                cur_r -= 1
            # self.ans[i] = 