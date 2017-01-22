# derescore デレステスコア計算機

シンプルなデレステスコア計算機。

学ラン○位取れる確率は他のツールでは計算できなそうなので作りました。

本レポジトリは以下のデータを含んでおりません。

* アイドルデータ
* 楽曲データ

また、スコア計算結果が正しいかどうか、十分には検証されておりません。

特技 オーバーロード のライフ計算を行っておりません。

## Requirement

* python2系

## アイドルデータ

idols/ に配置します。

例： idols/uduki2.json (utf-8)

```
{
    "name": "[ピースフルデイズ]島村卯月",
    "type": "cute",
    "Vo": "4596",
    "Da": "3725",
    "Vi": "7381",
    "Life": "44",
    "skill": "11秒毎、中確率でかなりの間、COMBOボーナス18%アップ",
    "centerSkill": "3タイプ全てのアイドル編成時、全員のビジュアルアピール値100%アップ"
}
```

特技レベルは 10 固定です。

プログラムで使用しているのは type  skill centerskillです。

## 楽曲データ

musics 以下に配置します。

* 例： musics/toware.json (utf-8)

```
{
    "type": "cute",
    "title": "秘密のトワレ",
    "debutLv": "9",
    "debutQuantity": "127",
    "regularLv": "13",
    "regularQuantity": "206",
    "proLv": "19",
    "proQuantity": "368",
    "masterLv": "28",
    "masterQuantity": "773",
    "master+Lv": null,
    "master+Quantity": null,
    "length": "125"
}
```

* 例： musics/toware-master-notes.json

ノーツが来るタイミング(秒)を定義します。

```
0,3.27,3.4,3.53,3.67,3.8...
```

## 使い方

* derescore.py の以下を編集する。

```
totalApeal = 100000
musicName = "toware"
difficalty = "master"
idolNames = ["uduki2", "shoko2", "kaede2", "mayu2", "shiki"]
scoreType = Skill.Skill.FULL
```

scoreType"Skill.Skill.FULL"は全てのスキルが発動すること。
"Skill.Skill.PROB" はスキルの発動がランダムとなります。

* 適宜ソース変更して、好きなデータを取得する。
    * 300番目のノーツ時のスコア等

* config ディレクトリを用意しておりますが使用しておりません。

* python derescore.py [試行回数]

* データの加工をexcelとかでして好きなように。

試行回数は デフォルト 1 です。

## TODO

* 計算結果を検証する。(正しい結果自体がわかっていない)
* perfectの範囲内から、理想スキルを探す機能
* オバロ対応
* Exceptionを直す
* 高速化
* パラメータセットを一纏めにして引数に渡す。(データベース化)
* sqlite3化する。(楽曲データ、アイドルデータ、ローカルデータ)
* 綺麗なコードを書く
* 英語を勉強する。(しない)
