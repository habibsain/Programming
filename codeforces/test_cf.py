
import cat_final
def test_dfsbfs():
    x = 4
    y = [1, 3, 2, 4]
    assert cat_final.dfs_equals_bfs(x, y) == 2