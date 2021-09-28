class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        out = []
        for e in emails:
            local, domain = e.split('@')
            if '.' in local:
                local = local.replace(".", "")
            if '+' in local:
                idx = local.index('+')
                local = local[:idx]
            out.append('@'.join([local,domain]))
        return len(set(out))
                
