def solve(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(solve(a, b, c))