class Assign4_Q1:
    def subSets(self, sub):
        return self.reSub([], sorted(sub))

    def reSub(self, current, sub):
        if sub:
            return self.reSub(current, sub[1:]) + self.reSub(current + [sub[0]], sub[1:])
        return [current]

print(Assign4_Q1().subSets([4,5,6]))


#original pythonanywhere
class Assign4_Q1:
    def sub_sets(self, sset):
        return self.subsetsRecur([], sorted(sset))

    def subsetsRecur(self, current, sset):
        if sset:
            return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
        return [current]

print(Assign4_Q1().sub_sets([4,5,6]))