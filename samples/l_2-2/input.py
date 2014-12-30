#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
パーフェクトPython P.054

2-2 入出力

"""

name = input("お名前は？")			#FIXME: コンソールから文字列のみインプットするとsyntaxエラーになる
age = input("何歳ですか？")

print("こんにちは%sさん（%s歳）" % (name, age))