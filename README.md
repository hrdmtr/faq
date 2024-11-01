# faq chatbot
外部からドキュメントを追加しその内容を含めてLLMが日本語で回答します。

# 前提
1. curl、gitがインストールされていること
インストールされていない場合はインストールする
```
apt install curl git
```


```
asdf install
```

```
python --version
```
でバージョンを確認する


2. asdfがインストールされていること
インストールされていない場合はインストールする
詳細は以下サイトに従いインストールする
https://asdf-vm.com/ja-jp/guide/getting-started.html

正しくインストールされたらasdf versionコマンドで確かめる。

```
$ asdf version
v0.14.1-f00f759

```




環境にPythonがインストールされてない場合は、
asdf plugin-add python
でPythonもインストールしてください。

3. poetryがインストールされていること
poetryのインストール

```
asdf plugin-add poetry
```

# 起動
次のコマンドで実行できます。
poetry run python src/gradio_app.py

