class Solution:
    def romanToInt(self, s: str) -> int:
	    symbols= {
	    "I":1,
	    "V":5,
	    "IV":4,
	    "X":10,
	    "IX":9,
	    "L":50,
	    "XL":40,
	    "C":100,
	    "XC":90,
	    "D":500,
	    "CD":400,
	    "M":1000,
	    "CM":900
	    }
	
	    exept1=["IV","IX","XL","XC","CD","CM"]
	    roman= s
	    num = 0
	    i=0
	    r=0
	    while i < len(roman):
	        r=i+1
	        if r<len(roman):
	            ex=roman[i]+roman[r]
	            #print(ex in exept1)
	            if ex in exept1:
	                num+= symbols[ex]
	                i+=2
	                continue
	        ch = roman[i]
	        num+= symbols[ch]
	        i+=1
	    return (num)
	        