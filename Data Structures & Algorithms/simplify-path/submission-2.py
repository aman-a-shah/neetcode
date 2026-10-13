class Solution:
    def simplifyPath(self, path: str) -> str:
        direc = []

        i = 0
        cur_acc = ''

        while i < len(path):
            if path[i] == '/':

                # slash indicates end so update
                if cur_acc != '':
                    if cur_acc == '..':
                        if len(direc)>0:
                            direc.pop()
                    elif cur_acc == '.':
                        pass
                    elif cur_acc != '':
                        direc.append(cur_acc)

                cur_acc = ''
                i += 1

                continue
            
            cur_acc += path[i]
            i+=1

            
        if cur_acc != '':
            if cur_acc == '..':
                if len(direc)>0:
                    direc.pop()
            elif cur_acc == '.':
                pass
            elif cur_acc != '':
                direc.append(cur_acc)

        return '/' + '/'.join(direc)