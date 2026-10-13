class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_mult = 0
        cur_str = ''
        
        for let in s:
            if let.isdigit():
                cur_mult = (cur_mult*10)+int(let)

            elif let == '[':
                # save cur state in stack
                stack.append((cur_mult, cur_str))
                cur_mult = 0
                cur_str = ''
            
            elif let == ']':
                # pop state and add to cur_str
                save_mult, save_str = stack.pop()
                cur_str = save_str + cur_str*int(save_mult)
                
            else:
                cur_str += let
    
        return cur_str