# -*- coding:UTF-8 -*-
'''

'''

class Solution(object):
    def lastRemain(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        # i = 0
        nums = [x for x in range(n)]
        cnt = n
        i = -1
        step = 0
        while cnt > 0:
            i += 1
            if i >= n:
                i = 0
            if nums[i] == -1:
                continue
            step += 1
            if step == m:
                print(nums[i])
                nums[i] = -1
                step = 0
                cnt -= 1
        return i

    def lastRemainFormula(self, n, m):
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


'''
    public int LastRemaining_Solution(int n, int m) {
        if(n<1||m<1)
            return -1;
        int[] array = new int[n];
        int i = -1,step = 0, count = n;
        while(count>0){   //跳出循环时将最后一个元素也设置为了-1
            i++;          //指向上一个被删除对象的下一个元素。
            if(i>=n)
                i=0;  //模拟环。
            if(array[i] == -1)
                continue; //跳过被删除的对象。
            step++;                     //记录已走过的。
            if(step==m) {               //找到待删除的对象。
                array[i]=-1;
                step = 0;
                count--;
            }
        }
        return i;//返回跳出循环时的i,即最后一个被设置为-1的元素
    }
'''
if __name__ == '__main__':
    print(Solution().lastRemain(5, 3))
    print("^^^^^^^^^^^^^^^^^^^^^^")
    print(Solution().lastRemainFormula(5, 3))

    # print(Solution().dp_probability(3, 18))
