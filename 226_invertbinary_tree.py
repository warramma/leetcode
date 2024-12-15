'''
226
Given the root of a binary tree, invert the tree, and return its root.


'''

def invertTree(root):
    #base case
    if root is None:
        return None
    else:
        #swap at the same time
        root.left, root.right = root.right, root.left

        invertTree(root.left)
        invertTree(root.right)
    return root