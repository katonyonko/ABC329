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
6 5
1 1 1 2 2 3
1 2
6 4
5 1
3 6
4 6
5 3
2 4 2 4 2
3 1
2 5
3 2
"""

def solve(test):
  N,Q=map(int,input().split())
  C=list(map(int,input().split()))
  d=[i for i in range(N)]
  ans=[set([C[i]]) for i in range(N)]
  for i in range(Q):
    a,b=map(int,input().split())
    a-=1; b-=1
    if len(ans[d[a]])>0:
      if len(ans[d[a]])>len(ans[d[b]]):
        for c in ans[d[b]]:
          ans[d[a]].add(c)
        ans[d[b]]=set()
        d[b],d[a]=d[a],d[b]
      else:
        for c in ans[d[a]]:
          ans[d[b]].add(c)
        ans[d[a]]=set()
    print(len(ans[d[b]]))

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