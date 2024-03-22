fin = open("diamond.in", "r")
# fout = open("diamond.out", "w")

N, K = map(int, fin.readline().split())
sizes = [int(size.replace("\n", "")) for size in fin.readlines()]
max_D = N

for i in range(N - 1):
    if abs(sizes[i] - sizes[i + 1]) > K:
        max_D -= 1  
print(sizes)
print(max_D)
# fout.write(str(max_D))

#greedy search needed
