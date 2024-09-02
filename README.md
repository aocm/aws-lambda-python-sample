# aws-lambda-python-sample


## 概要

wip

## 事前準備

poetry
https://python-poetry.org/docs/


## このリポジトリ同等の資材作り方・流れメモ
以下作業はこのリポジトリを利用する分には不要。

```bash
poetry init

# すべてyes
# poetry new aws-lambda-python-sample
# などでも可

# 必要なものを追加
poetry add pytest pre-commit black isort

#.pre-commit-config.yamlを作成し、blackとisortが起動するような記述後に下記を実行
poetry run pre-commit install
```
