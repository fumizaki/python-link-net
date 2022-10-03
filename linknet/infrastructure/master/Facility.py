# python external library
import pandas as pd
# infrastructure
from infrastructure.master.AbsMaster import AbsMaster

class Facility(AbsMaster):

    df: pd.DataFrame = None
    source: str = None
    encoding: str = None



    @classmethod
    def set(cls, source_dir: str, source_file: str, encoding: str='utf-8'):
        cls.source = source_dir + source_file
        cls.encoding = encoding


    @classmethod
    def load(cls):
        if cls.source is None:
            print('please set master file path')

        else:
            cls.df = pd.read_csv(cls.source, encoding=cls.encoding)
            cls.df['line_cd'] = cls.df['line_cd'].astype(str)
            cls.df['direction_cd'] = cls.df['direction_cd'].astype(int)
            cls.df['fmp'] = cls.df['fmp'].astype(int)
            cls.df['name'] = cls.df['name'].astype(str)
            cls.df['division_cd'] = cls.df['division_cd'].astype(int)


    @classmethod
    def validate_ldf(cls, line_cd: str, direction_cd: int, fmp: int):
        record = cls.df[
            (cls.df['line_cd'] == line_cd) & \
            (cls.df['direction_cd'] == direction_cd) & \
            (cls.df['fmp'] == fmp)
            ]

        if len(record) == 0:
            return False

        return True


    @classmethod
    def get_name(cls, line_cd: str, direction_cd: int, fmp: int):
        return cls.df[(cls.df['line_cd'] == line_cd) & (cls.df['direction_cd'] == direction_cd) & (cls.df['fmp'] == fmp)].iloc[0]['name']


    @classmethod
    def get_division_cd(cls, line_cd: str, direction_cd: int, fmp: int):
        return cls.df[(cls.df['line_cd'] == line_cd) & (cls.df['direction_cd'] == direction_cd) & (cls.df['fmp'] == fmp)].iloc[0]['division_cd']


    @classmethod
    def get_filtered_ldf(cls, line_cd: str, direction_cd: int, fmp: int, border_fmp: int):
        if direction_cd in [1, 3]:
            return cls.df[
                (cls.df['line_cd'] == line_cd) & \
                (cls.df['direction_cd'] == direction_cd) & \
                (cls.df['fmp'] < fmp) & \
                (border_fmp <= cls.df['fmp'])
            ]
        else:
            return cls.df[
                (cls.df['line_cd'] == line_cd) & \
                (cls.df['direction_cd'] == direction_cd) & \
                (cls.df['fmp'] <= border_fmp) & \
                (fmp < cls.df['fmp'])
            ]
