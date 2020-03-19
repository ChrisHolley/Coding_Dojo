str1 = "Hello! My name (the best name ever) is Cody!" # This is a valid braces configuration
str2 ="({[]})" # This is also a valid braces configuration
str3 ="({])}" # This is NOT  avalid braces configuration

# Given a string, write an algorithm that determines whether or not the configuration
# of the braces in that string are valid
def ValidBraces(string):
    for (i = 0; i < str.length; i++):
        if (str[i]=='(')
            count_left++
        else if (str[i]==")")
            count_right++
    if count_left == count_right
        return true

    # return Boolean of whether or not the string has a valid brace configuration 


ValidBraces("Hello (something{else)}")
