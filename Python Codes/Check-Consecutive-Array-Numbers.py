# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class SortArray:
    @classmethod
    def check_consecutive(self,input1, input2):
        input2.sort()
        for i in range(1,input1):
            if input2[i] != input2[i-1]+1:
                return 0
        return 1
    

obj = SortArray()
result = obj.check_consecutive(input1=5, input2=[2,1,3,6,4])
print(result)
