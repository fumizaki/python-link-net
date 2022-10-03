# python external library
import pandas as pd
# infrastructure
from infrastructure.master.Facility import Facility
from infrastructure.master.Range import Range
# domain
from domain.aggregate.LinkNet import LinkNet
from domain.entity.Point import Point


class LinkNetUseCase:

    def __init__(self) -> None:
        self.linknet: LinkNet = None
        self.start_point: Point = None


    def construct(self, line_cd: str, direction_cd: int, fmp: int):

        if not (Facility.validate_ldf(line_cd, direction_cd, fmp)):
            return 'ERROR: {}[{}]の{}は定義されていません。'.format(line_cd, direction_cd, fmp)


        # 始点の作成
        self.start_point = Point(
                line_cd,
                direction_cd,
                fmp,
                Facility.get_name(line_cd, direction_cd, fmp),
                Facility.get_division_cd(line_cd, direction_cd, fmp)
            )

        # 始点からリンクを作成
        self.linknet = LinkNet(self.start_point)

        # 施設情報を抽出
        filtered_facility = Facility.get_filtered_ldf(
                self.start_point.line_cd,
                self.start_point.direction_cd,
                self.start_point.fmp,
                Range.get_end_fmp(
                    self.start_point.line_cd,
                    self.start_point.direction_cd
                )
            )

        # ソート
        if self.start_point.direction_cd in [1, 3]:
            sorted_facility = Facility.sorted_by(filtered_facility, 'fmp', False)
        else:
            sorted_facility = Facility.sorted_by(filtered_facility, 'fmp')


        # 接続するポイントを作成し、リンクに接続する
        for n in range(0, len(sorted_facility)):
            next_point = Point(
                    sorted_facility.iloc[n]['line_cd'],
                    sorted_facility.iloc[n]['direction_cd'],
                    sorted_facility.iloc[n]['fmp'],
                    sorted_facility.iloc[n]['name'],
                    sorted_facility.iloc[n]['division_cd'],
                )
            if next_point.division_cd == 20:
                self.linknet.connect(next_point)
            self.linknet.append(next_point)


        # hubに追加された情報をもとにリンクに接続する
        for i in list(self.linknet.hubs.keys()):
            for j in range(0, len(self.linknet.hubs[i])):

                # 構築済みのリンクは再作成しない
                if self.linknet.hubs[i][j].other_link.head.point.str_ld() in self.linknet.constructed:
                    continue

                filtered_facility: pd.DataFrame = Facility.get_filtered_ldf(
                        self.linknet.hubs[i][j].other_link.head.point.line_cd,
                        self.linknet.hubs[i][j].other_link.head.point.direction_cd,
                        self.linknet.hubs[i][j].other_link.head.point.fmp,
                        Range.get_end_fmp(
                            self.linknet.hubs[i][j].other_link.head.point.line_cd,
                            self.linknet.hubs[i][j].other_link.head.point.direction_cd
                        )
                    )

                if self.linknet.hubs[i][j].other_link.head.point.direction_cd in [1, 3]:
                    sorted_facility: pd.DataFrame = Facility.sorted_by(filtered_facility, 'fmp', False)
                else:
                    sorted_facility: pd.DataFrame = Facility.sorted_by(filtered_facility, 'fmp')


                for n in range(0, len(sorted_facility)):
                    next_point = Point(
                            sorted_facility.iloc[n]['line_cd'],
                            sorted_facility.iloc[n]['direction_cd'],
                            sorted_facility.iloc[n]['fmp'],
                            sorted_facility.iloc[n]['name'],
                            sorted_facility.iloc[n]['division_cd'],
                        )
                    if next_point.division_cd == 20:
                        self.linknet.connect(next_point)
                    self.linknet.hubs[i][j].other_link.append(next_point)

        return True

