def validBraces(string):
    braces_map = {']': '[', '}': '{', ')': '('}
    braces_stack = []                                    
    for character in string:
        # push everything opening braces into stack
        if character == '[' or character == '(' or character == '{':
            braces_stack.append(character)

        # whenever we see any of the closing braces, check whether it match the last opening brace
        if character == ')':
            if braces_map[character] != braces_stack.pop():
                return False
        if character == '}':
            if braces_map[character] != braces_stack[len(braces_stack)-1]:
                return False
        if character == ']':
            if braces_map[character] != braces_stack.pop():
                return False

    # if there is anything left in the stack after we loop through everything that means we are missing one or more closing braces
    if len(braces_stack) >0:
        return False
    else:
        return True
str1 = "Hello! My name (the best name ever) is Cody!" # This is a valid braces configuration
str2 ="({[]})" # This is also a valid braces configuration
str3 ="({])}" # This is NOT  avalid braces configuration

print(validBraces(")))((("))