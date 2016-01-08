'''
根据物流防伪码，查询所购商品是否正品

中国质量检验协会防伪溯源和物流管理服务系统：http://www.c315.cn/
'''

from pyquery import PyQuery as pq
import re,random
import urllib.request


# 进行校验
def get_check(id):
    url='http://www.c315.cn/test2.asp?imageField.x=10&imageField.y=8&textfield2=&textfield='+id
    html = urllib.request.urlopen(url).read().decode('gbk')
    m = re.search(r'<td width="570">.*?<p align="left">(.*?)</td>',html,re.S).group(0)
    d = pq(m)
    text = d('td').text()
    print('您的质检码为：%s，质检结果为：%s' % (id,text))

# 随机生成20为质检码
def get_random():
    seed = '0123456789'
    sa = ''
    for i in range(20):
        sa += random.choice(seed)
    return sa

# 主程序
if __name__ == '__main__':
    for x in range(10):
        get_check(get_random())
'''
您的质检码为：07157880942653588411，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：48504867345475249029，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：70715268433244542717，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：17657087774562721449，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：40862402100150573973，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：32295594508977858364，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：21980233972863266518，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：32455966347223517644，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：98826997478893667764，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
您的质检码为：86009268066314845474，质检结果为：数码无效，谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
'''
if __name__ != '__main__':
    get_check('66254574712580337665')

'''
您的质检码为：66254574712580337665，质检结果为：数码已经被查询过,谨防假冒！--国家质检总局/中国质量检验协会防伪溯源物流管理服务中心。
'''