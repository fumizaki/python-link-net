# python standard library
from typing import Optional
# domain
from domain.entity.Point import Point

class Node:

    """
    同一線上のポイントを接続する
    """

    def __init__(self, point: Point, next_point: Point=None):
        self.point: Point = point
        self.next: Optional[Point] = next_point if self.is_same(next_point) else None


    def __repr__(self):
        return '{} --> {}'.format(self.point, self.next)


    # 同一線上か判定
    def is_same(self, point: Point):
        if point is None:
            return False

        return self.point.line_cd == point.line_cd \
            and self.point.direction_cd == point.direction_cd





