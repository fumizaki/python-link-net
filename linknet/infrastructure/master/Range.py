# python external library
import pandas as pd
# infrastructure
from infrastructure.master.AbsMaster import AbsMaster

class Range(AbsMaster):

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
            cls.df['start_fmp'] = cls.df['start_fmp'].astype(int)
            cls.df['end_fmp'] = cls.df['end_fmp'].astype(int)


    @classmethod
    def get_start_fmp(cls, line_cd: str, direction_cd: int):
        return cls.df[(cls.df['line_cd'] == line_cd) & (cls.df['direction_cd'] == direction_cd)].iloc[0]['start_fmp']


    @classmethod
    def get_end_fmp(cls, line_cd: str, direction_cd: int):
        return cls.df[(cls.df['line_cd'] == line_cd) & (cls.df['direction_cd'] == direction_cd)].iloc[0]['end_fmp']
