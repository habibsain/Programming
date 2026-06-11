
def take_input():
    x = int(input())
    y = input().strip()
    y = list(map(int, y.split(" ")))
    return x, y

def dfs_equals_bfs(num, arr):
    pass


if __name__ == "__main__":
    x, y = take_input()
    print(x)
    print(y)