# #logic building means experiments---
# # key board row
# class keyboard:
#     def key_row(self,words):
#         row1 = set("qwertyuiop")
#         row2 = set('asdfghjkl')
#         row3 = set("zxcvbnm")
#         res = []
#         for word in words:
#             lower_word = word.lower()
#             if lower_word[0] in row1:
#                 row = row1
#             elif lower_word[0] in row2:
#                 row = row2
#             elif lower_word[0] in row3:
#                 row = row3
            
#             all_in_word = True
#             for char in lower_word:
#                 if char not in row:
#                     all_in_word = False
#                     break
#             if all_in_word:
#                 res.append(word)    
#         return res
# # print(keyboard().key_row(['alaska','dad','peace']))
# a1 = keyboard()
# print(a1.key_row(['alaska','dad','peace']))


# checking palindrome or not
# def palindrome(num): #123
#     y = 0
#     temp = num 
#     while(0<num):
#         y = num % 10 + y*10  # rem=3 & y * 10 = 0 => y = 3 then 3*10+2=32=>32*10+1=320+1=321
#         num = num // 10   # flore division =>12 => 1 
#     print(f"reversed num is:{y}")
#     if y == temp:
#         print(f"first num:{temp} and second num:{y} are same- its palindrome")
#     else:
#         print(f"both num are: {temp}&{y} different so, its not a palindrome")

# palindrome(int(input("Enter a num to check palindrome or not: ")))

# valid paranthesis
# way 1
# def paranthesis(p):
#     pairs = {"]":"[","}":"{",")":"("}
#     sets = []
    
#     for char in p:
#         if char in pairs.values():
#             sets.append(char)
#         elif char in pairs:
#             if not sets or sets.pop() != pairs[char]:
#                 return False
#         else:
#             return False
#     return not sets
# print(paranthesis(input("Enter parathesis:")))
# way 1
# def paranthesis(p):
#     pairs = {"]": "[", "}": "{", ")": "("}
#     stack = []  # using 'stack' name for clarity
    
#     print(f"\nInput: {p}\n{'-'*30}")
    
#     for char in p:
#         print(f"Reading: {char}")
        
#         # Case 1: It's an opening bracket
#         if char in pairs.values():
#             stack.append(char)
#             print(f"  It's an opening bracket. Stack now: {stack}")
        
#         # Case 2: It's a closing bracket
#         elif char in pairs:
#             if not stack:
#                 print("  ❌ Stack empty but found closing bracket — invalid!")
#                 return False
#             last_open = stack.pop()
#             print(f"  It's a closing bracket. Popped: {last_open}")
#             print(f"  Expected opening: {pairs[char]}")
            
#             if last_open != pairs[char]:
#                 print("  ❌ Mismatch — invalid pair!")
#                 return False
#             else:
#                 print("  ✅ Matched correctly.")
        
#         # Case 3: Invalid character
#         else:
#             print(f"  ⚠️ Invalid character detected: {char}")
#             return False
    
#     # End of input
#     print(f"\nFinished reading. Stack: {stack}")
#     if not stack:
#         print("✅ All parentheses balanced correctly!")
#         return True
#     else:
#         print("❌ Some brackets not closed properly.")
#         return False

# # Try it:
# print(paranthesis(input("Enter parentheses: ")))

def paranthesis(p):
    # ANSI color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"

    pairs = {"]": "[", "}": "{", ")": "("}
    stack = []
    
    print(f"\n{CYAN}Input: {p}{RESET}")
    print("-" * 40)
    
    step = 1
    for char in p:
        print(f"{YELLOW}Step {step}:{RESET} Reading → '{char}'")
        
        # Case 1: Opening bracket
        if char in pairs.values():
            stack.append(char)
            print(f"  {GREEN}Opening bracket found. Stack → {stack}{RESET}")
        
        # Case 2: Closing bracket
        elif char in pairs:
            if not stack:
                print(f"  {RED}❌ Error: Closing '{char}' found but stack is empty!{RESET}")
                return False
            last_open = stack.pop()
            expected = pairs[char]
            
            print(f"  Found closing '{char}', popped '{last_open}' from stack.")
            if last_open != expected:
                print(f"  {RED}❌ Mismatch! Expected '{expected}', got '{last_open}'{RESET}")
                return False
            else:
                print(f"  {GREEN}✅ Matched correctly!{RESET}")
        
        # Case 3: Invalid character
        else:
            print(f"  {RED}⚠️ Invalid character '{char}' — ignoring or invalid input.{RESET}")
            return False
        
        step += 1
    
    print(f"\n{CYAN}Final Stack State → {stack}{RESET}")
    print("-" * 40)
    
    if not stack:
        print(f"{GREEN}✅ SUCCESS: All brackets balanced correctly!{RESET}\n")
        return True
    else:
        print(f"{RED}❌ FAILURE: Some brackets not closed: {stack}{RESET}\n")
        return False

# Test it interactively:
print(paranthesis(input("Enter parentheses: ")))







































