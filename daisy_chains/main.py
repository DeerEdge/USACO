import sys
import math

input = sys.stdin.readline

N = int(input())
flowers = list(int(size) for size in input().split())

avg_flowers = N

for i in range(N):
    for j in range(i+1, N):
        avg = sum(flowers[i:j+1])/len(flowers[i:j+1])
        if (avg in flowers[i:j+1]):
            avg_flowers += 1

sys.stdout.write(str(avg_flowers))
