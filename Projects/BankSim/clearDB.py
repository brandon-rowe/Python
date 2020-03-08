#Just used to clear log.txt when testing read/write to database
def main():
    with open('log.txt', 'w') as f:
        f.truncate(0)
main()