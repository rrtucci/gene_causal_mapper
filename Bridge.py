class Bridge:
    def __init__(self, t1, pt1, t2, pt2):
        self.t1 = t1
        self.pt1 = pt1
        self.t2 = t2
        self.pt2 = pt2
        
    def ___str___(self):
        return f"{self.t1}--{self.t2}, {self.pt1}--{self.pt2}"
    
    @staticmethod
    def bridges_str(bridges):
        str1 = ""
        for bridge in bridges:
            str1 += str(bridge) + ", "
        return str1[:-2]
