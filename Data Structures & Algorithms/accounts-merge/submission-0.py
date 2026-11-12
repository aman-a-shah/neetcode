class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        email_owner = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_owner:
                    uf.merge(i, email_owner[email])
                else:
                    email_owner[email] = i

        groups = defaultdict(set)
        for email, i in email_owner.items():
            groups[uf.find(i)].add(email)

        return [[accounts[root][0]] + sorted(emails)
                for root, emails in groups.items()]


class UnionFind:
        def __init__(self, n):
            self.parent = [i for i in range(n)]
        
        def find(self, x):
            if self.parent[x] == x:
                return x
            
            return self.find(self.parent[x])
        
        def merge(self, x, y):
            px, py = self.find(x), self.find(y)
            self.parent[px] = py