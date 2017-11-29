from bs4 import BeautifulSoup
import requests

start_url = 'http://hz.58.com/sale.shtml'
url_host = 'http://hz.58.com'


def get_channel_urls(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select(('ul.ym-submnu > li > b > a'))
    # print(links[0])
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url[0])

if __name__ == '__main__':
    get_channel_urls(start_url)

channel_list = """
    http://hz.58.com/shouji/
    http://hz.58.com/tongxunyw/
    http://hz.58.com/danche/
    http://hz.58.com/fzixingche/
    http://hz.58.com/diandongche/
    http://hz.58.com/sanlunche/
    http://hz.58.com/peijianzhuangbei/
    http://hz.58.com/diannao/
    http://hz.58.com/bijiben/
    http://hz.58.com/pbdn/
    http://hz.58.com/diannaopeijian/
    http://hz.58.com/zhoubianshebei/
    http://hz.58.com/shuma/
    http://hz.58.com/shumaxiangji/
    http://hz.58.com/mpsanmpsi/
    http://hz.58.com/youxiji/
    http://hz.58.com/jiadian/
    http://hz.58.com/dianshiji/
    http://hz.58.com/ershoukongtiao/
    http://hz.58.com/xiyiji/
    http://hz.58.com/bingxiang/
    http://hz.58.com/binggui/
    http://hz.58.com/chuang/
    http://hz.58.com/ershoujiaju/
    http://hz.58.com/bangongshebei/
    http://hz.58.com/diannaohaocai/
    http://hz.58.com/bangongjiaju/
    http://hz.58.com/ershoushebei/
    http://hz.58.com/yingyou/
    http://hz.58.com/yingeryongpin/
    http://hz.58.com/muyingweiyang/
    http://hz.58.com/muyingtongchuang/
    http://hz.58.com/yunfuyongpin/
    http://hz.58.com/fushi/
    http://hz.58.com/nanzhuang/
    http://hz.58.com/fsxiemao/
    http://hz.58.com/xiangbao/
    http://hz.58.com/meirong/
    http://hz.58.com/yishu/
    http://hz.58.com/shufahuihua/
    http://hz.58.com/zhubaoshipin/
    http://hz.58.com/yuqi/
    http://hz.58.com/tushu/
    http://hz.58.com/tushubook/
    http://hz.58.com/wenti/
    http://hz.58.com/yundongfushi/
    http://hz.58.com/jianshenqixie/
    http://hz.58.com/huju/
    http://hz.58.com/qiulei/
    http://hz.58.com/yueqi/
    http://hz.58.com/chengren/
    http://hz.58.com/nvyongpin/
    http://hz.58.com/qinglvqingqu/
    http://hz.58.com/qingquneiyi/
    http://hz.58.com/chengren/
    http://hz.58.com/xiaoyuan/
    http://hz.58.com/ershouqiugou/
    http://hz.58.com/tiaozao/
    http://hz.58.com/tiaozao/
    http://hz.58.com/tiaozao/
    """
