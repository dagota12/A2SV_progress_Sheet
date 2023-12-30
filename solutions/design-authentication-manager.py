class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokens ={}
        self.life = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = [currentTime,currentTime + self.life]

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and currentTime < self.tokens[tokenId][1]:
            self.tokens[tokenId][1] = currentTime + self.life

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ct = 0
        for token in self.tokens:
            st,end = self.tokens[token]
            if st < currentTime < end:
                ct += 1
        return ct


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)