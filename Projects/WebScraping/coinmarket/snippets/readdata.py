import pandas as pd

def main():
    data = pd.read_csv("data.csv", delimiter="|")
    print(data)
main()