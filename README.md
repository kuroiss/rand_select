# このソースファイルについて
+ 発狂難易度表を読んできてランダムセレクトするだけのプログラムです

## get_insane.py
[ここ](http://www.dream-pro.info/~lavalse/LR2IR/search.cgi?mode=search&type=insane)からtableタグを読んできてcsvファイルにぶち込むプログラムです</br>
そのうち次のランセレプログラムと合体させます

参考 : [Qiita - 【Python】BeautifulSoupを使ってテーブルをスクレイピング](https://qiita.com/hujuu/items/b0339404b8b0460087f9)

## random_select_music.py
get_insane.pyで作ったinsane_n.csvから曲目を読んできてランダムセレクトするプログラムです
> csvファイルを読みに行く部分はファイルを置いたパスに替えといてください

難易度に幅を持たせる部分、すげー適当に書いたのでそのうち正規表現で書き替えときます
