'''
110
How to check if a binary tree is balanced?
'''

#a tree is balanced if the absolute value of the left and right subtree
#height is <=1

#method for solving:
#recursively determine the height for the left and the right subtree
#if unbalanced at any point (absolute value of difference > 1)
#return False


def isBalanced(root):
    def helper(root):
        #base case
        if root is None:
            return 0, True
        
        #recursive

        #heights
        left_height, left_balanced = helper(root.left)
        right_height, right_balanced = helper(root.right)

        if not left_balanced or not right_balanced:
            return 0, False
        if abs(left_height - right_height) > 1:
            return 0, False
        return 1 + max(left_height, right_height), True

    height, balanced = helper(root)

    return balanced