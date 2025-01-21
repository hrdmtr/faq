# faq chatbot

外部からドキュメントを追加しその内容を含めてLLMが日本語で回答します。

# 前提
1. curl、gitがインストールされていること
インストールされていない場合はインストールする
```
apt install curl git
```

SELECT
    X.K_CTLG_PRT_NO,
    X.K_SKU_CD,
    ROUND(P.UNITPR, 0) AS UNITPR,
    NVL(Y.K_BG_CTGRY_MGMT_CD, 'LLLL') AS K_BG_CTGRY_MGMT_CD,
    NVL(Y.K_MDL_CTGRY_MGMT_CD, 'MMMM') AS K_MDL_CTGRY_MGMT_CD,
    NVL(Y.K_SML_CTGRY_MGMT_CD, 'SSSS') AS K_SML_CTGRY_MGMT_CD,
    NVL(Y.K_BG_CTGRY_MGMT_NM, '大カテゴリ') AS K_BG_CTGRY_MGMT_NM,
    NVL(Y.K_MDL_CTGRY_MGMT_NM, '中カテゴリ') AS K_MDL_CTGRY_MGMT_NM,
    NVL(Y.K_SML_CTGRY_MGMT_NM, '小カテゴリ') AS K_SML_CTGRY_MGMT_NM,
    NVL(X.ECO_ADD_FLG14, 0) AS ECO_ADD_FLG14,
    DECODE(X.K_ECO_ADD_FLG14, '1', '1', '1', '2') AS ECO_FLAG_DECODED
FROM TAND2140 X
LEFT OUTER JOIN TMPPRICE P
    ON X.K_SKU_CD = P.K_SKU_CD
LEFT OUTER JOIN (
    SELECT
        K_BG_CTGRY_MGMT_CD,
        K_MDL_CTGRY_MGMT_CD,
        K_SML_CTGRY_MGMT_CD,
        K_BG_CTGRY_MGMT_NM,
        K_MDL_CTGRY_MGMT_NM,
        K_SML_CTGRY_MGMT_NM
    FROM Y_TABLE /* Yの実テーブル名に置き換えてください */
) Y
    ON X.K_BG_CTGRY_MGMT_CD = Y.K_BG_CTGRY_MGMT_CD
    AND X.K_MDL_CTGRY_MGMT_CD = Y.K_MDL_CTGRY_MGMT_CD
    AND X.K_SML_CTGRY_MGMT_CD = Y.K_SML_CTGRY_MGMT_CD
WHERE MOD(TO_NUMBER(X.K_CTLG_PRT_NO), 3) = 0;

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

=======

#　起動
次のコマンドで実行できます。
poetry run python src/gradio_app.py

