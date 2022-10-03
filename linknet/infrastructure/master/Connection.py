# python external library
import pandas as pd
# infrastructure
from infrastructure.master.AbsMaster import AbsMaster

class Connection(AbsMaster):

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
            cls.df['source'] = cls.df['source'].astype(str)
            cls.df['line_cd'] = cls.df['line_cd'].astype(str)
            cls.df['direction_cd'] = cls.df['direction_cd'].astype(int)
            cls.df['fmp'] = cls.df['fmp'].astype(int)
            cls.df['name'] = cls.df['name'].astype(str)
            cls.df['division_cd'] = cls.df['division_cd'].astype(int)

