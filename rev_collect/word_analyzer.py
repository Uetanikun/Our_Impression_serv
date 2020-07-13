'''
path = "読み込むファイルの場所"
dic_list = "辞書読み込み用"
happy_word = "喜びカテゴリの辞書リスト"
enjoy_word = "楽しさカテゴリの辞書リスト"
relief_word = "安心カテゴリの辞書リスト"
like_word = "好きカテゴリの辞書リスト"
surprise_word = "驚きカテゴリの辞書リスト"
'''

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
