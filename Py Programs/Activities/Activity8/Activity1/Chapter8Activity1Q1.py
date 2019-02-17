# Chapter 8
# Activiy 1
# Question 1
def main():
    count = 0
    sample = ['abc','xyz','aba','1221']
    new = []
    for str in sample:
        n = len(str)
        if n > 2:
            if str[0] == str[n-1]:
                count += 1
                new.append(str)
    print(new)
    print(count)
main()
