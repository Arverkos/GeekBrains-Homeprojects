class NotNum(Exception):
    def __init__(self, txt):
        self.txt = txt


new_list = []
while True:
    try:
        inp_num = input('Введите число, либо "stop" чтобы закончить ввод: ')

        if inp_num == 'stop':
            break
        if inp_num.isalpha():
            raise NotNum('Вы ввели не число!')
    except NotNum as err:
        print(err)
    else:
        new_list.append(int(inp_num))

print(new_list)
