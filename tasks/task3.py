def solve(word1, word2):
    return word1 == "awesome" or word2 == "awesome"

if __name__ == "__main__":
    w1 = input().strip()
    w2 = input().strip()
    print(solve(w1, w2))