'''
235. Lowest Common Ancestor of a Binary Search Tree
Solved
Medium
Topics
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''

def lca(root, p, q):
    smaller, larger = None, None
    if p.val < q.val:
        smaller = p
        larger = q
    elif p.val > q.val:
        smaller = q
        larger = p
    else:
        smaller = p
        larger = p
    
    def bst(root, smaller, larger):
        if root.val >= smaller.val and root.val <= larger.val:
            return root
        if root.val > larger.val:
            return bst(root.left, smaller, larger)
        if root.val < smaller.val:
            return bst(root.right, smaller, larger)
    
    return bst(root, smaller, larger)

#time - o(h), space - O(h)


       