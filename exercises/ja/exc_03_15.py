import json
from spacy.lang.ja import Japanese
from spacy.tokens import Doc

with open("exercises/ja/bookquotes.json") as f:
    DATA = json.loads(f.read())

nlp = Japanese()

# デフォルト値がNoneのDoc拡張属性「author」を登録
____

# デフォルト値がNoneのDoc拡張属性「book」を登録
____

for doc, ____ in ____(____, ____):
    # doc._.bookとdoc._.author属性にコンテキストからデータをセット
    doc._.book = ____
    doc._.author = ____

    # テキストとカスタム属性を表示
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
