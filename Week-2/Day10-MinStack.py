"""
Day 10 - Min Stack
Leetcode Easy Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
  push(x) -- Push element x onto stack.
  pop() -- Removes the element on top of the stack.
  top() -- Get the top element.
  getMin() -- Retrieve the minimum element in the stack.
 
Example:
  MinStack minStack = new MinStack();
  minStack.push(-2);
  minStack.push(0);
  minStack.push(-3);
  minStack.getMin();   --> Returns -3.
  minStack.pop();
  minStack.top();      --> Returns 0.
  minStack.getMin();   --> Returns -2.
  
Hint #1:
  Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)
"""

class MinStack:
    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        if not self.st: self.st.append((x,x))
        else: self.st.append((x, min(x, self.st[-1][1])))

    def pop(self) -> None:
        if self.st: self.st.pop()

    def top(self) -> int:
        if self.st: return self.st[-1][0]
        else: return None

    def getMin(self) -> int:
        if self.st: return self.st[-1][1]
        else: return None
