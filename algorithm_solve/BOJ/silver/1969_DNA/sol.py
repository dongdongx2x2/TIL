import sys
sys.stdin = open('1969_input.txt')

input = sys.stdin.readline

def find_optimal_dna(dna_list):
    n = len(dna_list)
    m = len(dna_list[0])
    optimal_dna = ""
    total_distance = 0

    for i in range(m):
        nucleotides = [dna[i] for dna in dna_list]
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for nucleotide in nucleotides:
            counts[nucleotide] += 1

        max_count = max(counts.values())
        optimal_nucleotide = min([nuc for nuc, count in counts.items() if count == max_count])

        optimal_dna += optimal_nucleotide
        total_distance += n - max_count

    return optimal_dna, total_distance


n, m = map(int, input().split())
dna_list = [input().strip() for _ in range(n)]
o, total = find_optimal_dna(dna_list)

print(o)
print(total)