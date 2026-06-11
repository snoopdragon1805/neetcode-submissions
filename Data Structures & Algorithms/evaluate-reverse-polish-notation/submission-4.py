class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens.pop())
        opr = tokens.pop()
        exp1 = tokens.pop()
        if exp1 in ["+","-","*","/"]:
            tokens.append(exp1)
            exp1 = self.evalRPN(tokens)
        exp2 = tokens.pop()
        if exp2 in ["+","-","*","/"]:
            tokens.append(exp2)
            exp2 = self.evalRPN(tokens)
        if opr == "+":
            return int(exp1)+int(exp2)
        elif opr == "*":
            return int(exp1)*int(exp2)
        elif opr == "-":
            return int(exp2)-int(exp1)
        elif opr == "/":
            return int(int(exp2)/int(exp1))