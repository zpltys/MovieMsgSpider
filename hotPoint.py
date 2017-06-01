#!/usr/bin/python3

from urllib import request, parse
import re
import time
import listDate

headers = {'Cookie' : r'SINAGLOBAL=8957822691169.557.1495358359350; _s_tentry=s.weibo.com; Apache=6216052847409.286.1496217402671; ULV=1496217402720:3:3:1:6216052847409.286.1496217402671:1495883107264; SWB=usrmdinst_2; ULOGIN_IMG=14962325518543; login_sid_t=f4baf730d4e72b443ca13e7d67bd003a; un=15851817252; UOR=os.51cto.com,widget.weibo.com,login.sina.com.cn; WBtopGlobal_register_version=4641949e9f3439df; SCF=AuBQACkNsim7rps0XOLnFkThM_78kpKWfkXPaKZwp73sg6iFXr5rt801j0GMUd8qrxZZH7HuD2r44m-gTS33C6Y.; SUB=_2A250KqeoDeThGeNJ4lQZ-CjFzj-IHXVXQZ5grDV8PUNbmtBeLUrQkW9JqSVF2feePcu-7xe6BpKGK-0Ipw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhGggNG8ug7R5ABNUiC3Ij05JpX5K2hUgL.Fo-N1KqR1hq4SKe2dJLoI7UAMspXwPe_; SUHB=0auQh7INUslnaf; ALF=1496846968; SSOLoginState=1496242168; un=zpltys@163.com; WBStorage=02e13baf68409715|undefined'}

def getHot(movie, year, month, day):
    (year, month, day) = listDate.beforeDate(year, month, day)

    url = 'http://s.weibo.com/weibo/' + parse.quote(movie) + '&xsort=hot&suball=1&timescope=custom::%d-%d-%d&Refer=g' % (year, month, day)

    print('url:' + url)
    req = request.Request(url, headers = headers)

    html = request.urlopen(req).read().decode('utf8')
    #time.sleep(15)
    return len(re.findall('page=[0-9]+', html))

if __name__ == '__main__':
    info = {}
    temp = open('temp.txt', 'r')
    for hav in temp:
        h = hav.split('\t')
        info[h[0]] = int(h[1])
    temp.close()

    cou = 0

    f = open('data.csv', 'r')
    f.readline()
    for line in f:
        msg = line.split(',')
        name = msg[0]
        if name in info.keys():
            continue
        year = msg[1]
        month = msg[2]
        day = msg[3]
        hot = getHot(name, year, month, day)
        print(name + ": " + str(hot))
        if hot == 0:
            hot = 1
        info[name] = hot
        temp = open('temp.txt', 'a+')
        temp.write(name + '\t' + str(hot) + '\n')
        temp.close()
        cou += 1
        if cou % 5 == 0:
            time.sleep(0)
        time.sleep(15)
    f.close()
