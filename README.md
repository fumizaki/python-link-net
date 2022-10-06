# python-link-net

入力値をもとに施設(facility.csv)の情報を接続し、単方向連結リストを作成します。
接続定義(connection.csv)に従って、施設-他の単方向連結リストを接続します。


## 必要なライブラリ

### Pandas

~~~
pip install pandas
~~~


## 実行

### コマンド

~~~
python main.py
~~~

### 入力例

~~~
please input line_cd >
1000
please input direction_cd >
1
please input fmp >
300
~~~

## 設定

### facility.csv

施設情報を記載する

- line_cd: 任意の文字列

- direction_cd(1, 3): fmpが小さい方向に構築を行う。

- direction_cd(2, 4): fmpが大きい方向に構築を行う。

- fmp: 距離を管理するための便宜上の地点数値情報

- name: 任意の文字列

- division_cd: 他のラインと接続する場合、20を設定する

### range.csv

ラインの最大最小を記載する

- line_cd: 任意の文字列

- direction_cd: 任意の方向

- start_fmp: ラインの最後尾

- end_fmp: ラインの先頭

### connection.csv

ラインの接続情報を記載する

- source: 接続元のline_cd, direction_cd, fmpを使用して、{line_cd}_{direction_cd}_{fmp}の形式で設定

- line_cd: 接続先のline_cd

- direction_cd: 接続先のdirection_cd

- fmp: 接続先のfmp

- name: 接続先のname

- division_cd: 接続先のdivision_cd


