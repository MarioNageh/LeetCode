class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming = [0]  * n
        for src,dst in edges:
            incoming[dst] += 1

        champions = []
        for idx, cnt in enumerate(incoming):
            if not cnt:
                champions.append(idx)
        return -1 if len(champions) > 1 else champions[0]
