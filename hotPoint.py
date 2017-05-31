#!/usr/bin/python3

from urllib import request, parse
import re
import listDate

header = {'Cookie' : r'SINAGLOBAL=8957822691169.557.1495358359350; UOR=os.51cto.com,widget.weibo.com,www.njupt.edu.cn; _s_tentry=s.weibo.com; Apache=6216052847409.286.1496217402671; ULV=1496217402720:3:3:1:6216052847409.286.1496217402671:1495883107264; SWB=usrmdinst_2; WBtopGlobal_register_version=4641949e9f3439df; SCF=AuBQACkNsim7rps0XOLnFkThM_78kpKWfkXPaKZwp73saSGqNWqwA3hvbENIVgHtpD4iWGBJtPwV9PQOcX9mRfw.; SUB=_2A250KvuSDeThGeNJ4lQZ-CjFzj-IHXVXXmparDV8PUNbmtBeLVTdkW-VGxYk2WpGYZ3NdnYVyVeTQ5SXIA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhGggNG8ug7R5ABNUiC3Ij05JpX5KzhUgL.Fo-N1KqR1hq4SKe2dJLoI7UAMspXwPe_; SUHB=0OM0UlrsOBEb_8; ALF=1527758658; SSOLoginState=1496222659; WBStorage=02e13baf68409715|undefined'}

def getHot(movie, year, month, day):
    (year, month, day) = listDate.beforeDate(year, month, day)

    url = 'http://s.weibo.com/weibo/' + parse.quote(movie) + '&xsort=hot&suball=1&timescope=custom::%d-%d-%d&Refer=g' % (year, month, day)
    req = request.Request(url, headers = header)

    html = request.urlopen(req).read().decode('utf8')
    return len(re.findall('page=[0-9]+', html))
