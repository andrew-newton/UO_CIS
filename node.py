class Node:

    def __int__(self, node_data: int):
        self.node_data = node_data

    def sum_node_data(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


class Leaf(Node):

    def __init__(self, node_data: int):
        self.node_data = node_data

    def sum_node_data(self) -> int:
        return self.node_data

    def __str__(self):
        return f"<{self.node_data}>"


class Internal(Node):

    def __init__(self, node_data: int, left: Node, right: Node):
        self.node_data = node_data
        self.left = left
        self.right = right

    def sum_node_data(self) -> int:
        left_sum = self.left.sum_node_data()
        right_sum = self.right.sum_node_data()

        return self.node_data + left_sum + right_sum

    def __str__(self) -> str:
        left_sum = self.left.__str__()
        right_sum = self.right.__str__()
        return f"<{self.node_data}, {left_sum}, {right_sum}>"

    def sum(self):
        return self.sum_node_data()



def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum())


if __name__ == "__main__":
    main()
