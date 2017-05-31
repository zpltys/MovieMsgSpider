#!/usr/bin/python3

from urllib import request, parse
from lxml import etree
import re

def getMsg(movie):
    url = 'http://www.gewara.com/newSearchKey.xhtml?skey=' + parse.quote(movie) + '&channel=movie&category='

    print("url = %s" % url)
    html = request.urlopen(url).read().decode('utf8')

    selector = etree.HTML(html)

    for i in range(10):
        name = selector.xpath('/html/body/div[@class="ui_layout"]/div[@class="ui_panel"]/div[@class="search_body_left clear"]/dl[@class="ui_abeam search_channel"][%d]/dd[@class="uiText"]/h2/a//text()' % i)
        name = ''.join(name)
        if name != movie:
            continue

        movieType = selector.xpath('/html/body/div[@class="ui_layout"]/div[@class="ui_panel"]/div[@class="search_body_left clear"]/dl[@class="ui_abeam search_channel"][%d]/dd[@class="uiText"]/span[6]/text()' % i)
        if len(movieType) != 0:
            movieType = re.split(',| |/', movieType[0])
        else:
            movieType = ['unknown']

        country = selector.xpath('/html/body/div[@class="ui_layout"]/div[@class="ui_panel"]/div[@class="search_body_left clear"]/dl[@class="ui_abeam search_channel"][%d]/dd[@class="uiText"]/span[7]/text()' % i)
        if len(country) != 0:
            country = re.split(',|/', country[0])
        else:
            country = ['unknown']

        actor = selector.xpath('/html/body/div[@class="ui_layout"]/div[@class="ui_panel"]/div[@class="search_body_left clear"]/dl[@class="ui_abeam search_channel"][%d]/dd[@class="uiText"]/span[8]//text()' % i)
        actor = ''.join(actor)
        #print(actor)
        if len(actor) == 0:
            actor = ['unknown']
            director = ['unknown']
        else:
            actor = actor.split('：')[1]
            actor = actor.split('/')
            if len(actor) > 0:
                director = re.split(' +', actor[0])
            else:
                director = ['unknown']
            if len(actor) > 1:
                actor = re.split(' +', actor[1])
            else:
                actor = ['unknown']
        return (movieType, country, director, actor)
    return (['unknown'], ['unknown'], ['unknown'], ['unknown'])

if __name__ == '__main__':
    movie = '黄连有点甜'
    print(getMsg(movie))
