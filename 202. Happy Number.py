'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
#学会几种方法，一种是用递归调用，如果递归调用需要存储数据，则可以在主程序里面调用其他的函数，添加参数
#第二种就是用快慢指针的方法，但是这种方法是用C++ 写的 因为需要用到do while 在Python里面用 
while True: 
  if condition:
    break 
#代替
#还有一种sum()方法可以计算列表 set等的和
class Solution(object):
    def isHappy1(self, n):
        return self.calculate(n,l)

    def calculate(self,n,l):
        l = []
        sum1 = sum(int(k)**2 for k in str(n))
        if sum1 == 1:
            return True
        elif sum1 in l:
            return False
        else:
            l.append(sum1)
            return self.calculate(sum1,l)
do--while方法

Freezen
Freezen
 521
Last Edit: 2 days ago

I see the majority of those posts use hashset to record values. Actually, we can simply adapt the Floyd Cycle detection algorithm. I believe that many people have seen this in the Linked List Cycle detection problem. The following is my code:

int digitSquareSum(int n) {
    int sum = 0, tmp;
    while (n) {
        tmp = n % 10;
        sum += tmp * tmp;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow, fast;
    slow = fast = n;
    do {
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
    } while(slow != fast);
    if (slow == 1) return 1;
    else return 0;
}
  
}
