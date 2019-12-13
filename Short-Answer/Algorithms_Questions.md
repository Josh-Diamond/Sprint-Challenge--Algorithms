# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
• O(n) - while loop only runs n times based on variable

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
• O(n log n) - inner loop is running on less than what the outer loop is so total time will increase at a rate greater than the size of n
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
• O(n) - runs for every bunny passed in

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

Time Complexity - O(log n) Binary search
Pseudo Code:
• divide n-story building in half, and round down to middle ( // )
• check if egg breaks at middle point
• if broken, divide values < middle point ( // ) and repeat
• if egg not broken, divide the values > middle point ( // ) and repeat
• eventually after repeating that logic, you will find the break point level
