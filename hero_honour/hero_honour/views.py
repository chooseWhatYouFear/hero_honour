
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')

def hero_honour(request):
    data = {
        "data": [
            {
                'src': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562662695279&di=cdaf31ead70bbce4e3f933b2b9407501&imgtype=0&src=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F9602138793_640330%2F0',
                'hero_name': '妲己',
                'username': '虎牙曹不亏',
                'sub_src':'/static/images/1-1.jpg'},

            {
                'src': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562662746062&di=d1be925adc5232fd08899c0e6523f8b4&imgtype=0&src=http%3A%2F%2F02imgmini.eastday.com%2Fmobile%2F20181208%2F20181208200153_d41d8cd98f00b204e9800998ecf8427e_1.jpeg',
                'hero_name': '后羿',
                'username': '虎牙影不了',
                'sub_src':'/static/images/1-2.jpg'},
            {
                'src': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562662767512&di=171a99f07edad8d003431ed3755b7e10&imgtype=0&src=http%3A%2F%2Fwww.33lc.com%2Fuploadfile%2F2017%2F1015%2F20171015113647374.jpg',
                'hero_name': '孙悟空',
                'username': '虎牙锤不懂',
                'sub_src': '/static/images/1-3.jpg'},
            {
                'src': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562662787507&di=f551062d8051a056446b8609dc9b8605&imgtype=jpg&src=http%3A%2F%2Fimg2.imgtn.bdimg.com%2Fit%2Fu%3D3700556682%2C432632555%26fm%3D214%26gp%3D0.jpg',
                'hero_name': '小乔',
                'username': '虎牙心态蹦',
                'sub_src': '/static/images/1-4.jpg'},
            {
                'src': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3104505103,3755269023&fm=26&gp=0.jpg',
                'hero_name': '项羽',
                'username': '虎牙酒馆',
                'sub_src': '/static/images/1-5.jpg'},

        ],
        'data1': [
            {
                'src': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1852308621,3289368726&fm=26&gp=0.jpg',
                'hero_name': '百里守约',
                'username': 'estar猫神',
                'sub_src': '/static/images/1-6.jpg'},
            {
                'src': 'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=502762904,202325748&fm=26&gp=0.jpg',
                'hero_name': '雅典娜',
                'username': 'estarOrange',
                'sub_src': '/static/images/1-6.jpg'},
            {
                'src': 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3625221823,2708898073&fm=26&gp=0.jpg',
                'hero_name': '橘右京',
                'username': 'estar诺言',
                'sub_src': '/static/images/1-8.jpg'},
            {
                'src': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2641317659,3806137162&fm=26&gp=0.jpg',
                'hero_name': '周瑜',
                'username': 'estar伪装',
                'sub_src': '/static/images/1-2.jpg'},
            {
                'src': 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1779574644,3949549106&fm=26&gp=0.jpg',
                'hero_name': '鲁班大师',
                'username': 'estarTiger',
                'sub_src': '/static/images/1-10.jpg'}
        ]

    }
    return render_to_response('hero_honour.html',locals())