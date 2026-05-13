class Solution(object):
    def containsDuplicate(self, nums):
        valor_percorrido = set()
        for i in range(len(nums)):
            if nums[i] in valor_percorrido:
                return True
            else: valor_percorrido.add(nums[i])
        return False
    
    # aprendendo a usar set() para verificar duplicatas. 
    # OBS: eu poderia ter usado apenas uma linha com uma verificação 
    # para rodar em menos tempo.