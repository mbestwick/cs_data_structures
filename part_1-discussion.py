"""

Part 1: Discussion Questions

<<< Runtime >>>

1. The workload would be going through each cracker in the box and checking if
it is an elephant. Once you find the first elephant, your work is done. In terms
of runtime, we would assume the worst - that you have to look at every single
cracker in the box, and the very last one is an elephant, so the entire runtime
would be the total number of crackers in the box - i.e. O(n).

2. In order of most efficient to least efficient:
    O(1)
    O(logn)
    O(n)
    O(nlogn)
    O(n^2)
    O(2^n)


<<< Stacks and Queues >>>

1. stack v queue:
    1. stack
    2. queue
    3. stack

2. Queue examples: order of handling print jobs, caching old/unnecessary info
3. Stack examples: 'undo' process in a program, back button in your browser


<<< Linked Lists >>>

1. The nodes are the boxes that say apple, berry, and cherry, and the data at
each node is the string of its name. The head is the apple node. The tail is
the cherry node.

2. A singly-linked list only goes in one direction - i.e. you can only go to the
next node and cannot reverse and go to a previous. A doubly-linked list goes in
both directions, and you can go to the next or previous node at any point.

3. Without a tail, we would need to traverse the entire linked list until we
find the end. With a tail, we could immediately go to the tail and add a node
after it.

<<< Trees >>>

1. food, Italian, Indian, Mexican, lasagna, pizza, tikka masala, saag, burritos

2. food, Mexican, enchiladas, tacos, burritos, Indian, saag, tikka masala,
Italian, pizza, Sicilian, New York-style, Chicago-style

3. Each node in a binary search tree can only have up to 2 children, and the
position of each child (left or right) is dependent on a specific rule that
applies to each node in the tree. Because the rule is the same at each node,
it is very easy to traverse a tree from root to leaf, and only takes one
direct path.

"""
