# presentation
from presentation.schema.LinkNet import LinkNet
from presentation.controller.LinkNetController import LinkNetController
# infrastructure
from infrastructure.master.Facility import Facility
from infrastructure.master.Connection import Connection
from infrastructure.master.Range import Range

class Main:

    @staticmethod
    def entry(scm: LinkNet):
        if LinkNetController.linknet(scm):
            print('--- Mission Accomplished ---')
        else:
            print('--- Mission Failed ---')



if __name__ == '__main__':

    # マスタデータのロード
    Facility.set('./infrastructure/file/master/', 'facility.csv')
    Facility.load()
    Connection.set('./infrastructure/file/master/', 'connection.csv')
    Connection.load()
    Range.set('./infrastructure/file/master/', 'range.csv')
    Range.load()

    print('please input line_cd >')
    line_cd = input()

    print('please input direction_cd >')
    direction_cd = int(input())

    print('please input fmp >')
    fmp = int(input())

    Main.entry(LinkNet(line_cd, direction_cd, fmp))