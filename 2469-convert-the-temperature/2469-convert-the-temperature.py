class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        new=[]
        
        ka=celsius+273.15
        new.append(ka)
        fa=celsius*1.80+32.00
        new.append(fa)
            
        return new