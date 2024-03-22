fin = open("diamond.in", "r")
fout = open("diamond.out", "w")

N, K = map(int, fin.readline().split())
sizes = [int(size.replace("\n", "")) for size in fin.readlines()]
sizes = list(set(sorted(sizes)))
max_D = N
N = len(sizes)
print(sizes)
for i in range(N):
    for j in range(i + 1, N):
        print(N-1-i, N-1-j, "-", sizes[N-1-i], sizes[N-1-j], "-", max_D, sizes[N-1-i]-sizes[N-1-j])
        if abs(sizes[N-1-i]-sizes[N-1-j]) > K:
            max_D -= 1  
print(max_D)

fout.write(str(max_D))
