import heapq
from sys import stdin, stdout

input = stdin.readline
print = stdout.write


# union find 알고리즘 : 사이클의 존재 여부 판단
def find(parent , target):
	if parent[target] != target :# 루트 노드가 아닌 경우
		parent[target] = find(parent, parent[target])
	return parent[target] # 루트노드를반환


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y



# def getCycleCount(n ,edges):
#     cycleCount = 0
#     parent = [ i for i in range(0 , n+1)] # 정점들 초기화, 편의상 인덱스 0 은 사용하지 않음
#     for x,y in edges : # edges = (시작정점, 도착정점)
#         if find(parent,x) == find(parent,y): # 바로 직후에 집합화할건데 같은 팀이었던 상황이니까
#             cycleCount += 1
#         union(parent, x,y)
#     print(f"parent:{parent}\n")
#     return cycleCount


def getTreeCount(n ,edges):
    cycleCount = 0
    parent = [ i for i in range(0 , n+1)] # 정점들 초기화, 편의상 인덱스 0 은 사용하지 않음
    for x,y in edges : # edges = (시작정점, 도착정점)
        if find(parent,x) == find(parent,y): # 바로 직후에 집합화할건데 같은 팀이었던 상황이니까
            cycleCount += 1
        union(parent, x,y)
    # print(f"cycleCount : {cycleCount}, ")
    roots=[]
    for root in parent:
        if root not in roots:
            roots.append(root)

#    print(f"roots : {roots} , len(roots)-1:{len(roots)-1} ->")
#    print(f"( len(roots)-1 ) - cycleCount :{len(roots)-1 - cycleCount}\n")
    return len(roots)-1 - cycleCount




def main():
    caseCount = 1
    while(True) :
        # N : 정점갯수
        # M : 간선 갯수
        N,M = map(int,input().split())
        # print(f"N:{N}, M:{M}\n")
        if N==M==0: # 0 , 0 입력시 종료
            break
        edges = []
        for i in range(M):
            edge = list(map(int,input().split()))
            edges.append(edge)
        # print(f"edges:{edges}\n")
        res = getTreeCount(N, edges)
        if (res > 1):
            print(f"Case {caseCount}: A forest of {res} trees.\n")
        elif(res == 1 ):
            print(f"Case {caseCount}: There is one tree.\n")
        else :
            print(f"Case {caseCount}: No trees.\n")
        caseCount+=1




    return

if __name__ == "__main__":
    main()