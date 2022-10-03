# domain
from domain.aggregate.Link import Link
from domain.entity.Point import Point

class Hub:

    """
    あるポイントと異なる線分を接続する
    """

    def __init__(self, own_point: Point, other_link: Link):
        self.own_point: Point = own_point
        self.other_link: Link = other_link


    def __repr__(self):
        return '{} >>> {}'.format(self.own_point, self.other_link)


