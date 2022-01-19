import cv2 as cv
import glob
import os
import random
import sys
import configparser

#iniファイルを読み込む
config_ini=configparser.ConfigParser()
inifile=sys.argv[1]
config_ini.read(inifile, encoding="utf-8")

#iniファイルから変数を読み込む
pic_directory=config_ini["CUTOUT"]["pic_directory"] #空撮画像のディレクトリの位置
box_volume=int(config_ini["CUTOUT"]["box_volume"]) #cutout時に書き込む箱の数
pic_width=int(config_ini["CUTOUT"]["pic_width"]) #空撮画像の横幅
pic_height=int(config_ini["CUTOUT"]["pic_height"]) #空撮画像の縦幅
box_width=int(config_ini["CUTOUT"]["box_width"]) #書き込む箱の横幅
box_height=int(config_ini["CUTOUT"]["box_height"]) #書き込む箱の縦幅
blue=int(config_ini["COLOR"]["blue"]) #箱の色(青)
green=int(config_ini["COLOR"]["green"]) #箱の色(緑)
red=int(config_ini["COLOR"]["red"]) #箱の色(赤)
saving_directory=config_ini["CUTOUT"]["saving_directory"] #cutout後の画像の保存先

#ディレクトリ中の空撮画像をすべて読み込む
files=glob.glob(pic_directory+"*.JPG")

for file in files: #空撮画像をすべて読み込むまで続く
    img=cv.imread(file) #画像を読み込む
    print(file) #ファイル名をパスとともにコンソールに出力
    filename=os.path.basename(file) #ファイル名を格納
    count=0 #書き込んだ箱を数える用の変数
    while count<box_volume: #箱をすべて書き込むまで続ける
        #書き込む箱の始点の座標をランダムに取得
        x1=random.randint(0,pic_width-box_width)
        y1=random.randint(0,pic_height-box_height)
        #書き込む箱の終点の座標を決める
        x2=x1+box_width
        y2=y1+box_height
        #箱の色を設定
        img=cv.rectangle(img,(x1,y1),(x2,y2),(blue,green,red),-1,4) #(blue,green,red)
        cv.imwrite(saving_directory+filename,img)#画像に箱を書き込む
        count+=1
