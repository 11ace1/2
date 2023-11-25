from pprint import pprint

if __name__ == '__main__':

    goods = [
        {
            'name' : 'Iphone 15',
            'brend' : 'Apple',
            'price' : 50_000
        },
        {
            'name' : 'A10',
            'brend' : 'Samsung',
            'price' : 40_000
        },
        {
            'name' : 'M 11',
            'brend' : 'Xiaomi',
            'price' : 30_000
        },
    ]
    def item_price(item):
        return item['price']




    #pprint(sorted(goods, key=lambda item : item['price']))

    # for item in goods:
    #     if item['brend'] == 'Apple':
    #         print(item)

    # apple_list = filter(lambda item : item['brend'] == 'Apple', goods)
    # print(apple_list)
    # print(isinstance(apple_list))

    # apple_list = list(filter(lambda item : item['brend'] == 'Apple', goods))
    # print(apple_list)
    # with open('1.txt') as f:
    #     lst=[list(map(int, i.split())) for i in f]
    # print(lst)

    # a= input('')
    # print(sum(list(map(int, a.split()))))

    # lst=['1','2','3','4']
    # lst_new = list(map(int,lst))
    # print(lst_new)

    names=['Иван', 'Петя','Гриша','Женя','Леша']
    surnames=['Иванов', 'Петров','Григорьев','Сидоров','Лошаков']
    patronymic_list = ['Иванович','Петрович','Григорьевич', 'Алексееч','Иванович']


    # full_name = list(map(lambda names, surnames: f'{surnames} {names}', names, surnames))
    # print(full_name)


    # indexes_goods = []
    # for i in range(len(goods)):
    #     indexes_goods.append({i : goods[i]})
    #
    # indexes_goods = []
    # for index, item in enumerate(goods):
    #     indexes_goods.append({index:item})
    #
    # print(indexes_goods)

    for names, surnames, patronymic in zip(names,surnames,patronymic_list):
        print(surnames,names,patronymic)

print(__name__)
