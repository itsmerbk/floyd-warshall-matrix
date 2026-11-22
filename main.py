def floyd_warshall(n, edges):
    INF = 10**9; d = [[0 if i==j else INF for j in range(n)] for i in range(n)]
    for u, v, w in edges: d[u][v] = min(d[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]: d[i][j] = d[i][k] + d[k][j]
    return d

if __name__ == "__main__":
    mat = floyd_warshall(3, [(0,1,3),(1,2,4),(0,2,10)])
    assert mat[0][2] == 7
    print("[PASS] 017_floyd_warshall_matrix")
