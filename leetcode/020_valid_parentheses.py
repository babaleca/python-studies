class Solution(object):
    def isValid(self, s):
        pilha = []
        for i in range (len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{': pilha.append(s[i])
            elif s[i]==')' and len(pilha)!=0 and pilha[-1]=='(': pilha.pop()
            elif s[i]==']' and len(pilha)!=0 and pilha[-1]=='[': pilha.pop()
            elif s[i]=='}' and len(pilha)!=0 and pilha[-1]=='{': pilha.pop()
            else: return False
        if len(pilha)!=0: return False
        else: return True