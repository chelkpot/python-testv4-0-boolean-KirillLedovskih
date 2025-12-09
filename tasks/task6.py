# tasks/task6.py

def solve():
# Ниже пишите решение задачи

    a, b, c = map(int, input().split())


    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]


    print(z * z == x * x + y * y)
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()