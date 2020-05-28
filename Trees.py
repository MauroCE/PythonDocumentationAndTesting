class Node:
    """A class implementing a tree."""

    def __init__(self, value):
        """Constructor. Takes the value of the node and initializes the right and the left child to None (i.e. it has no
        children).

        Parameters
        ----------
        value : int
                Value of the node
        """
        self.value = value
        self.right = None
        self.left = None

    def append_left_child(self, child_value):
        """Method used to set a left child for the node.
        If the left child is empty (None) then we instantiate a new Node with the given value.
        If the left child is _not_ empty, then we create a new instance of a node. The left child of this new node
        becomes the left child of this current instance and then we set the left child of this instance equal to the new
        node. Basically, if it has a left child, we squish a new node in between.

        Parameters
        ----------
        child_value: int
                     Value to be given to a new Node instance that is going to become this node's left child.
        """
        if self.left is None:
            self.left = Node(child_value)
        else:
            new = Node(child_value)  # Instantiate new node
            new.left = self.left  # The new node inherits the left child
            self.left = new  # The new node becomes the new left child

    def append_right_child(self, child_value):
        """Same as `append_left_child` but with the right child.

        Parameters
        ----------
        child_value: int
                     Value to be given to a new Node instance that is going to become this node's right child.
        """
        if self.right is None:
            self.right = Node(child_value)
        else:
            new = Node(child_value)
            new.right = self.right
            self.right = new

    def __str__(self):
        """Prints the node in pretty-print style."""
        s = "     |{}|     \n".format(self.value)
        if self.right is not None and self.left is not None:
            s += "     / \     \n"
            s += "   |{}| |{}|    ".format(self.left.value, self.right.value)
        return s


def print_tree():
    """Simple function to print a tree."""
    print(r'     |1|     ')
    print(r'     / \     ')
    print(r'   |3| |8|   ')


if __name__ == "__main__":
    # Print the tree that we want to construct
    print_tree()
    # Construct the tree
    topNode = Node(1)
    leftNode = Node(3)
    rightNode = Node(8)
    topNode.left = leftNode
    topNode.right = rightNode
    # Print the generated tree
    print(topNode)
