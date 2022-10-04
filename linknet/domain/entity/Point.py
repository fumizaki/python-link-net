# python standard library
from __future__ import annotations

class Point(object):

    """
    line上の点(施設等)を示す
    """

    def __init__(self, line_cd: str, direction_cd: int, fmp: int, name: str, division_cd: int):
        self.line_cd: str = line_cd # 地点の線分を表すコード
        self.direction_cd: int = direction_cd # 地点の方向を表すコード
        self.fmp: int = fmp # For Management Point: 管理用の地点数値情報を示す(line&direction内で一意)
        self.name: str = name # 地点の名称
        self.division_cd: int = division_cd # 地点の区分を示す(10: spoke, 20: hub)


    def __repr__(self) -> str:
        return '{}[{}]-{}({})'.format(self.line_cd, self.direction_cd, self.name, self.fmp)


    def str_ld(self):
        return '{}_{}'.format(self.line_cd, self.direction_cd)


    def str_ldf(self):
        return '{}_{}_{}'.format(self.line_cd, self.direction_cd, self.fmp)


    def is_equal(self, o: Point):
        return (self.line_cd == o.line_cd) \
            and (self.direction_cd == o.direction_cd) \
            and (self.fmp == o.fmp)

