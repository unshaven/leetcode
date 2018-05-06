/*
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
*/
input：0,1,2,3,4,5,6....
output:0,1,2,3,4,5,6,7,8,9,1,2,3,4...
class Solution1 {
public:
    int addDigits(int num) {
        if(num<10)
          return num;
        else if(num%9==0)
          return 9;
        else
          return num%9;
    }
};
class Solution2 {
public:
    int addDigits(int num) {
        return 1+((num-1)%9);
    }
};
