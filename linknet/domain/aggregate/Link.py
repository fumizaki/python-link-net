# domain
from domain.entity.Point import Point
from domain.entity.Node import Node


class Link:

    def __init__(self, point: Point):
        self.head = Node(point)

    def __repr__(self):
        return '{}'.format(self.head)

    # Linkに追加
    def append(self, new_point: Point):
        new_node = Node(new_point)

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    # 現在地点までの距離を算出
    def get_distance(self):

        distance = 0

        current_node = self.head
        while current_node.next:
            distance += abs(current_node.point.fmp - distance)
            current_node = current_node.next

        return distance