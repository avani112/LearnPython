class Solution:
    
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1

        if s[0] == "0":
            return 0
        
        for i in range(2,len(s)+1):
            if(int(s[i-1]) >= 1):
                dp[i] += dp[i-1]
            if( 10<= int(s[i-2] + s[i-1]) <=26):
                dp[i] += dp[i-2]
                
        return dp[-1]
