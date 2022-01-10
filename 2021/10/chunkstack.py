beginChars = "([{<"
endChars   = ")]}>"
closing = {
    "(":")",
    "[":"]",
    "{":"}",
    "<":">"
}
points = {
    ")":3,
    "]":57,
    "}":1197,
    ">":25137
}
completePoints = {
    ")":1,
    "]":2,
    "}":3,
    ">":4
}

class ChunkStack:
    chars:list[str] = None
    val = 0
    def __init__(self, seed:str) -> None:
        val = 0
        self.chars = []
        for c in seed:
            if c in beginChars:
                self.chars.append(c)
            else:
                if c == closing[self.chars[-1]]:
                    self.chars.pop()
                else:
                    #print("found wrong closing char!")
                    self.val = points[c]
                    return
        if len(self.chars)==0:
            val = -1
    
    def complete(self) -> int:
        points = 0
        while len(self.chars)>0:
            #print("iter")
            points *= 5
            #print(completePoints[closing[self.chars[-1]]])
            points += completePoints[closing[self.chars[-1]]]
            self.chars.pop()
        return points