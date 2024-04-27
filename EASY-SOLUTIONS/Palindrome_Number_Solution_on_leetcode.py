class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        straight_list=[]
        reverse_list=[]
        for a in range(0,len(str(x))):
            b=str(x)[a]
            straight_list.append(b)
        reverse_list=straight_list
        reverse_list=reverse_list[::-1]
        counter=0
        for a in range(0,len(straight_list)):
            if(straight_list[a]==reverse_list[a]):
                counter+=1
        if(counter==len(reverse_list)):
            return True    

        else:
            return False 










        