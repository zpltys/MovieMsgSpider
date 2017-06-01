#!/usr/bin/python3

if __name__ == '__main__':
    data = open('data.csv', 'r')
    hot = open('temp.txt', 'r')

    first_line = data.readline()

    Hmap = {}
    out = open('n_data.csv', 'w+')
    out.write(first_line)

    for msg in hot:
        m = msg.split('\t')
        Hmap[m[0]] = int(m[1])
    hot.close()

    for line in data:
        l = line.split(',')
        l[4] = str(Hmap[l[0]])
        print(l)
        out.write(','.join(l))
    out.close()
    data.close()
