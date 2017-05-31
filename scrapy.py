#!/usr/bin/python3

from urllib import request
import listDate
import getMovieMsg
import json
import hotPoint

if __name__ == '__main__':
    data = {}
    dayBox = []

    for date in listDate.dates(2014, 2017, 1, 5):
        year = date[0]
        month = date[1]
        day = date[2]
        weekDay = date[3]

        print(date)

        url = 'https://box.maoyan.com/promovie/api/box/second.json?beginDate=' + year + month + day

        jsonData = request.urlopen(url).read()
        jsonData = jsonData.decode('utf-8')
        msg = json.loads(jsonData)

        dayBox.append(date + (msg['data']['totalBoxInfo'], ))

        for info in msg['data']['list']:
            name = info['movieName']
            money = float(info['boxInfo'])
            release = info['releaseInfo']

            if(release[:2] != '上映'):
                continue

            if release[2:-1] == '首':
                release = 1
                data[name] = {}
                data[name]['total'] = 0.0
                data[name]['year'] = year
                data[name]['month'] = month
                data[name]['day'] = day
                movieMsg = getMovieMsg.getMsg(name)
                data[name]['type'] = movieMsg[0]
                data[name]['country'] = movieMsg[1]
                data[name]['director'] = movieMsg[2]
                data[name]['actor'] = movieMsg[3]
                data[name]['hot'] = hotPoint.getHot(name, year, month, day)
            else:
                release = int(release[2:-1])

            if name in data.keys():
                if release <= 20:
                    data[name][release] = money
                data[name]['total'] += money


    f = open('data.csv', 'w+')
    f.write('name,year,month,day,hot,type,country,director,actor,')
    f.write(','.join(str(i) for i in range(1, 21)))
    f.write(',total\n')

    for movie in data.keys():
        f.write(movie + ',')
        info = data[movie]
        f.write(str(info['year']) + ',' + str(info['month']) + ',' + str(info['day']) + ',' + str(info['hot']) + ',')
        f.write('/'.join(info['type']) + ',' + '/'.join(info['country']) + ',' + '/'.join(info['director']) + ',' +'/'.join(info['actor']) + ',')
        for i in range(1, 21):
            if i in info.keys():
                f.write('%.3f' % info[i])
            else:
                f.write('0')
            f.write(',')

        f.write('%.3f' % info['total'])
        f.write('\n')

    f.close()

    f = open('day.csv', 'w+')
    f.write('year,month,day,weekday,money\n')
    for date in dayBox:
        f.write(','.join(str(v) for v in date))
        f.write('\n')
    f.close()
