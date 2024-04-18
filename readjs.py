import json

def read_file(file_name):
    """ 
        Прочитати порядково файл, повидаляти різне не потрібне
        Викоирстовувати для можливості роботи із лог-файлами.
    """
    # w = open('zizi.txt','w')
    t = open(file_name, 'r')
    w = open('js.json','w', encoding='utf-8')
    z = list(t.readlines())
    i = 1
    print  ('[')
    w.write('[\n')
    for l in z:
        if i==1:
            tt='{\n"mp3": "'+l[:-1]+'",'
            print  (tt)
            w.write(tt)
        if i==3:
            tt='\n"text": "'+l[:-1]+'"'+'\n'+'}\n'
            print  (tt)
            w.write(tt)
        i=i+1
        if i==6:
            i=1
    print  (']')
    w.write(']')
    return 0
def read_file_not_json(file_name):
    """
        Прочитати порядково файл, повидаляти різне не потрібне
        Викоирстовувати для можливості роботи із лог-файлами.
    """
    # w = open('zizi.txt','w')
    t = open(file_name, 'r')
    w = open('js.txt','w', encoding='utf-8')
    z = list(t.readlines())
    i = 1
    for l in z:
        if i==1:
            tt=l
            print  (tt)
            w.write(tt)
        if i==3:
            tt=l
            print  (tt)
            w.write(tt)
        i=i+1
        if i==6:
            i=1

    return 0

if __name__ == '__main__':
    read_file_not_json('app/templates/english.txt')
    '''with open('js.json',encoding='utf-8') as f:
        lll = json.load(f):
    print(lll)
    '''