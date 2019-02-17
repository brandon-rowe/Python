# Chapter 8
# Activiy 1
# Question 2
def main():

    sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    def last(n):
        return n[-1]

    def first(n):
        return n[0]

    def sort_list(tuples):
        return sorted(tuples, key=last)

    def sort_list_first(tuples):
        return sorted(tuples, key=first)

    print(sample)
    print(sort_list(sample))
    print(sort_list_first(sample))

main()
