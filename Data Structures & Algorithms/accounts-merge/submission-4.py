class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        
        # setup all pointers from indices
        acct_merge = {}
        for i, acct in enumerate(accounts):
            for email in acct[1:]:
                if email in acct_merge:
                    uf.merge(i, acct_merge[email])
                else:
                    acct_merge[email] = i
        
        # map acct root to emails
        email_to_emails = {}
        for email, i in acct_merge.items():
            root = uf.find(i)
            if root in email_to_emails:
                email_to_emails[uf.find(i)].add(email)
            else:
                email_to_emails[uf.find(i)] = {email}
        
        return [[accounts[i][0]]+sorted(list(emails)) for i, emails in email_to_emails.items()]




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