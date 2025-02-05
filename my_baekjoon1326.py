from sys import stdin,stdout
from collections import deque

input = stdin.readline
print = stdout.write

N=0



def bfs(a,b,graph):
    global N
    queue = deque()
    visited=[False]*(N+1)
    count=0
    isFound=False

    #스타트 대입
    queue.append(a)
    visited[a]=True

    while queue:
        curNode=queue.popleft()
        count+=1
        
    return -1









    return

def main():
    global N
    N = int(input())
    nodeValues = list(map(int,input().split()))
    nodeValues.insert(0,0)

    # 배수 관계로 간선 형성
    graph=[[]] # 편의상 인덱스 0 은 비움
    for i in range(1,N+1):
        adjointNodes =[]
        curNodeValue=nodeValues[i]
        for k in range(1,N): # 1 ~ N-1
            distance = curNodeValue*k
            if i-distance >=1:
                adjointNodes.append(i - distance)
            if i + distance <=N:
                adjointNodes.append(i + distance)
        graph.append(adjointNodes)
    print(f"graph:{graph}\n")






if __name__ =="__main__":
    main()