class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Will store (previous_string, repeat_count)
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current state onto the stack
                stack.append((current_string, current_num))
                # Reset for the new nested level
                current_string = ""
                current_num = 0
            elif char == ']':
                # Pop the previous state
                prev_string, repeat_count = stack.pop()
                # Decode the current level
                current_string = prev_string + current_string * repeat_count
            else:  # letter
                current_string += char
        
        return current_string