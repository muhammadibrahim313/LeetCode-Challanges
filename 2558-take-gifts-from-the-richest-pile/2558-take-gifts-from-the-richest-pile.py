class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Perform the operation k times
        for i in range(k):
            pile = max(gifts)            
            gifts.remove(pile)                       
            gifts.append(int(pile ** 0.5))    
        ans = sum(gifts)        
        return ans