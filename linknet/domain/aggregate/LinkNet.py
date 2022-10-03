# python standard library
from collections import defaultdict
# domain
from domain.aggregate.Link import Link
from domain.entity.Hub import Hub
from domain.entity.Point import Point
# infrastructure
from infrastructure.master.Connection import Connection


class LinkNet(Link):

    def __init__(self, point: Point):
        super().__init__(point)
        self.hubs = defaultdict(list)
        self.constructed = [point.str_ld()]


    def __repr__(self):
        return '{}'.format(self.head)


    def connect(self, own_point: Point):
        other_points = Connection.df[Connection.df['source'] == own_point.str_ldf()]
        if other_points is not None:
            for i in range(0, len(other_points)):
                other_point = Point(
                    other_points.iloc[i]['line_cd'],
                    other_points.iloc[i]['direction_cd'],
                    other_points.iloc[i]['fmp'],
                    other_points.iloc[i]['name'],
                    other_points.iloc[i]['division_cd'],
                )
                self.hubs[own_point.str_ld()].append(Hub(own_point, Link(other_point)))






