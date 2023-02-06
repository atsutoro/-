import os
import samplecreates

#パスの取得&リスト作成　
path = r'C:\Users\m22e1\Geeksalon\cv\pos' #ポジティブ画像があるファイルのフルパス
files = os.listdir(path)

for dir in files:
    samplecreates.main(dir)