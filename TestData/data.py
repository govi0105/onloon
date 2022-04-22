import random
import datetime
class Data:
    #登录数据
    data = [
        {"username": "15727679977","passwd": "gw12345","msg":"主账号"},
        {"username": "gw679977@163.com","passwd": "gw12345","msg":"子账号1"},
        {"username": "540104071@qq.com","passwd": "f3fRePNKSsq7LWBC","msg":"子账号2"},
        {"username": "gaowei","passwd": "1234546565465","msg":"账号错误"}]
    login_data={"username": "15727679977","passwd": "gw12345","msg":"主账号"}
    #驱动位置
    #driving ="C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    user_txt="您好，祝您工作顺利"

    # 登录地址
    login_url ="https://ydt.onloon.net/#/login"
    # 邮箱页面地址
    mail_url="https://ydt.onloon.net/#/mail/list"

    # 随机邮箱
    listemail=["wuwanhua@loonxi.com","liutongbin@loon.com","huanghexiang@loonxi.com","gw679977@163.com","houshihang@loonxi.com","lifei@loonxi.com"]
    num1=len(listemail)-1
    emmail = listemail[random.randint(0,num1)]
    # 邮箱主题
    dtatime=datetime.date.today()
    themelist = ["咖啡", "奶茶", "水果", "豆浆", "凉茶", "快乐肥宅水","绿茶","红茶","中餐","西餐"]
    num2 = len(themelist)-1
    txt = themelist[random.randint(0, num2)]
    themetext=str(dtatime)+' '+str(txt)
    # 邮箱内容
    mail_text="杭州龙席网络科技股份有限公司成立于2013年4月，总部位于浙江杭州，在全国17个城市设有分支机构和研发团队、市场及服务运营团队。依托龙席实力团队的行业理解力、互联网创新能力和对B端、C端客户需求的深刻理解，主打业务涵盖供应链相关软件研发与服务、跨境社群电商整体解决方案、企业互联网战略规划及咨询服务等领域，累计服务企业上万家。龙席网络一直坚持“成就客户在互联网领域的新发展、新成功”为己任，致力于成为“让全世界的生意人和消费者都爱上未来龙席的产品和服务”的新一代互联网公司。"