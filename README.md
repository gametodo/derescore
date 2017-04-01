# derescore デレステスコア計算機

入力（input.json: スキル、アピール値）に対する、スコアを計算します。

```
todo@main:~/derescore$ python derescore.py input.json 5
1276815.0
1281761.0
1274475.0
1266972.0
1270227.0
```

学ラン○位取れる確率の計算が他のツールでは計算できなそうなので作りました。

本レポジトリは以下のデータは仮のデータが登録されております。

* アイドルデータ
* 楽曲データ

特技 オーバーロード のライフ計算を行っておりません。

スキルブーストは 17% と 18%には対応しています。
フォーカス対応。検証する時間はありませんので、適当です。

## Requirement

* python2系

## アイドルデータ

idols/ にサンプルアイドルが配置されています。

idols.data/ に配置するとリポジトリから不可視となります。

サンプルアイドルは以下のフォーマットとなります。

```
[clp]SS[lmh][osc]VV.json
```

* c = cute, l=cool, p=passion
* SS=sec SS秒ごと
* l =低確率, m = 中確率, h = 高確率
* o = overload, s = score up, c = combo bonus
* VV = 効果量 18 = 18%

特技レベルは 10 固定です。

プログラムで使用しているのは type  skillです。

## 楽曲データ

musics/ にサンプル楽曲が配置されています。(goinのようですが、一部改変されてます。)

musics.data/ に配置するとリポジトリから不可視となります。

## 使い方

* input.json.example を input.json に copy して編集する。

scoreType "full"はスキルが100%発動します。
"prob" はスキルの発動がランダムとなります。

* 適宜ソース編集して、好きなデータを取得する。
    * 300番目のノーツタップ時のスコア等

* python derescore.py input.json [試行回数]

試行回数は デフォルト 1 です。

* データの加工をexcelとかで好きなように。

## ソースについて

書き捨てプログラムのつもりで作成したので、作りこんでいません。

## TODO

* python3化
* Exceptionがまだunicode対応していない。(python3化で直るかも)
* sqlite3化する。(楽曲データ、アイドルデータ、ローカルデータ)
* アイドル情報とポテンシャル情報、サポートメンバーから総アピール値の計算
* perfectの範囲内から、理想スキルを探す機能(最高スコア時のみ)
* オバロライフ対応
* 高速化
* 綺麗なコードを書く
* 英語を勉強する。(しない)
