import requests
import json
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}#伪装Chrome headers

uid = input('请输入UID：')
while True:
    fans = requests.get('https://api.bilibili.com/x/relation/stat?vmid='+str(uid)+'&spm_id_from=333.788.b_636f6d6d656e74.317',headers = headers)#获取粉丝、关注数
    fans_data = json.loads(fans.text)
    id_data = requests.get('https://tenapi.cn/bilibili/?uid='+str(uid),headers = headers)#获取id、等级数
    if fans_data['message'] == '请求错误':
        print('未输入UID或UID不正确')
        input('点击回车退出')
        exit()
    id_data = json.loads(id_data.text)
    try:
        id_data = id_data['data']
    except:
        print('未输入UID或UID不正确')
        input('点击回车退出')
        exit()
    name = id_data['name']#id
    level = id_data['level']#等级
    description = id_data['description']#简介
    fans_data = fans_data['data']
    following = fans_data['following']#关注
    follower = fans_data['follower']#粉丝
    print('UID:',uid,'，关注数：',following,'，粉丝数：',follower,'，id：',name,'，等级：',level,'，个人简介：',description)
