from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:  # End gene must be in the bank
            return -1

        bank_set = set(bank)  # Convert bank to a set for O(1) access
        queue = deque([(startGene, 0)])  # Queue for BFS (gene, mutation count)
        while queue:
            gene, mutation_count = queue.popleft()
            if gene == endGene:
                return mutation_count

            # Check all possible one-character mutations
            for i in range(len(gene)):
                for char in 'ACGT':
                    mutated_gene = gene[:i] + char + gene[i+1:]
                    if mutated_gene in bank_set and mutated_gene != gene:
                        queue.append((mutated_gene, mutation_count + 1))
                        bank_set.remove(mutated_gene)  # Mark as visited

        return -1  # No mutation path found
