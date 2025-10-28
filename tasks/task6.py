def solve(a, b, c):
    sides = sorted([a, b, c])
    return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(solve(a, b, c))