def solve(a, b, c):
    return a == b == c

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(solve(a, b, c))