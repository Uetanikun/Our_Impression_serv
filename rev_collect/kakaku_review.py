'''
url = 解析先URL
req =
soup =
title = 対象物名
price = 最安値
revCount = レビュー数
review = レビュー文
'''

from bs4 import BeautifulSoup
import urllib.request as req
import MeCab


#htmlを取得
url = "https://review.kakaku.com/review/K0001201317/"
req = req.urlopen(url)

#htmlを解析
soup = BeautifulSoup(req, "html.parser")

#任意のデータを抽出
title = soup.select_one(".name").string
price = soup.select_one(".priceTxt").string
revCount = soup.select_one(".reviewernum > span").string
review = soup.select(".revEntryCont")

for rev_txt in review:
    rev_txt = rev_txt.text
    #print(rev_txt)
    #MeCabによる解析
    mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -Owakati')
    text = rev_txt
    result = mecab.parse(rev_txt)
    print(result.split(' ')) # \u3000は全角スペースらしい
    #mecab.parse('')
    #node = mecab.parseToNode(text)
    #print(result)

#口コミすべて抽出後、すべての口コミをテキスト化する。for文と配列カウントを活用

#感情語辞書の読み込み
path = 'dictionary/happy.csv'
with open(path)as f:
    dic_list = f.read()
    happy_word = dic_list.split(',')

path = 'dictionary/enjoy.csv'
with open(path)as f:
    dic_list = f.read()
    enjoy_word = dic_list.split(',')

path = 'dictionary/relief.csv'
with open(path)as f:
    dic_list = f.read()
    relief_word = dic_list.split(',')

path = 'dictionary/like.csv'
with open(path)as f:
    dic_list = f.read()
    like_word = dic_list.split(',')

path = 'dictionary/surprise.csv'
with open(path)as f:
    dic_list = f.read()
    surprise_word = dic_list.split(',')

#パターンマッチング


#対象物名
print(title)
#最安値
print(price)
#口コミ数
print(revCount)
