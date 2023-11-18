import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
7 3
ABCBABC
ABC
7 3
ABBCABC
ABC
12 2
XYXXYXXYYYXY
XY
7 3
BACCCVB
BAC
"""

def solve(test):
  N,M=map(int,input().split())
  S=[ord(x)-ord('A') for x in input()]
  T=[ord(x)-ord('A') for x in input()]
  dif=[[0 if S[i+j]==T[j] else 1 for j in range(M)].count(1) for i in range(N-M+1)]
  q=[i for i in range(N-M+1) if dif[i]==0]
  while q:
    x=q.pop()
    for i in range(M):
      if S[x+i]!=-1:
        for j in range(M):
          if S[x+i]!=T[j]:
            if 0<=x+i-j<N-M+1:
              dif[x+i-j]-=1
              if dif[x+i-j]==0:
                q.append(x+i-j)
        S[x+i]=-1
  if S.count(-1)==N:
    print('Yes')
  else:
    print('No')

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)