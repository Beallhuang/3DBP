# ======================
# -*- coding:utf-8 -*-
# @author:Beall
# @time  :2021/11/24 9:27
# @file  :3D装箱算法.py
# ======================
from three_box import Packer, Bin, Item


def main(box_list, item_list):
    """
    装箱算法, 输入可用箱体积参数, 货品体积参数
    :param box_list: 待装箱体积参数列表
    :param item_list: 待装箱货品体积参数列表
    :return: 箱和货品
    """
    packer = Packer()
    if isinstance(box_list, list) and isinstance(item_list, list):
        for i, v in enumerate(box_list):
            if isinstance(v, tuple):
                packer.add_bin(Bin(f'box{i+1}', v[0], v[1], v[2], v[3]))
            else:
                raise '参数输入错误'
        for i, v in enumerate(item_list):
            if isinstance(v, tuple):
                packer.add_item(Item(f'item{i+1}', v[0], v[1], v[2], v[3]))
            else:
                raise '参数输入错误'
        packer.pack()
        for b in packer.bins:
            print(":::::::::::", b.string())
            print("FITTED ITEMS:")
            for item in b.items:
                print("====> ", item.string())
            print("UNFITTED ITEMS:")
            for item in b.unfitted_items:
                print("====> ", item.string())
            print("***************************************************")
            print("***************************************************")
    else:
        raise '参数输入错误'


if __name__ == '__main__':
    main([(3, 4, 5, 999)], [(3, 4, 5, 0.1), (6, 8, 9, 0.1)])