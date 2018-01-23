import json
import pymysql
# 连接数据库
conn = pymysql.connect(host='', port=3306, user='root',
                       passwd='5515lsT@', db='toutiao')  # db：库名

cur = conn.cursor()
# path = r"./students_toutiao.json"
# file = open(path, "rb")
# fileJson = json.load(file)
# alldata = fileJson['RECORDS']
# for i in alldata:
#     # print()
#     id = i['id']
#     image_url = i['image_url']
#     title=i['title']
#     media_creator_id = i['media_creator_id']
#     media_name = i['media_name']
#     print(media_name+title)
#     cur.execute('insert into weixin_toutiao(id,image_url, title,media_creator_id,media_name) values(%s,%s,%s,%s,%s)',
#     (id,
#      image_url, 
#      title,
#      media_creator_id,
#       media_name
#       )
#       )
cur.execute('insert into weixin_toutiao(id,image_url, title,media_creator_id,media_name) values(%s,%s,%s,%s,%s)', ('id', 'image_url', 'title', '的风格大方', 'media_name'))

conn.commit()
# 关闭指针对象
# ret = cur.executemany( "insert into weixin_toutiao(id,image_url, title,media_creator_id,media_name) values(%s,%s,%s,%s,%s)", alldata)
# 提交


# 打印结果
# for i in alldata:
#     print(i)
#     Toutiao.objects.create(i)
