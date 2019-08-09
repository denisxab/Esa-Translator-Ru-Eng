# -*- coding: utf-8 -*-
# pylint: disable=C0103
# pylint: disable=W0105
# pylint: disable=C0303
"""
from Check_class import Check_class
@Check_class(1) # None пропустить элемент
def Entrance_VK(logins:str, li:None,passwords:None)-> True:
    pass

Entrance_VK(123,[],'12312')
"""

import time
import sys

def Check_class(Reg=0):
    """s
    Декоратор для проверки типов входящих переменных
    """
    
    def actual_decorator(func):
        def decorator_function(*Items, **Dicts):
            """
            Комбенированная проврека
            0.003 Длительность проверки
            """
            def statistics(reg):
                """
                Информация
                """
                if reg == 0:
                    print(
                        '______________________________________________________________________')
                    print(f'Name: {func.__name__}')

                    if Dicts:
                        print('**Kargs:')
                        for x in enumerate(['{0} |=| {1} |=|{2}Бт'.format(str(x)[:35].ljust(35),
                                                                          type(
                                x).__name__[:7].center(7),
                                sys.getsizeof(x)) for x in Dicts.values()]):
                            print(f'{x[0]}=> : {x[1]}')

                    if Items:
                        print('*Arg:')
                        for x in enumerate(['{0} |=| {1} |=|{2}Бт'.format(str(x)[:35].ljust(35),
                                                                          type(
                                x).__name__[:7].center(7),
                                sys.getsizeof(x)) for x in Items]):
                            print(f'{x[0]}=> : {x[1]}')

                if reg == 1:
                    start = time.time()
                    print(
                        '\\-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - /')
                    func_Time = func(*Items, **Dicts)
                    print(
                        '/-  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  - \\')

                    print('>>> : {0} |=| {1} |=|{2}Бт'.format(str(func_Time)[:35].ljust(35), type(func_Time).__name__[:7].center(7), sys.getsizeof(func_Time)))
                    print(
                        'Time: {0}.Сек |=| {1} '.format(str(time.time()-start).ljust(31),func.__name__.ljust(7)))
                    print(
                        '----------------------------------------------------------------------')

                    return func_Time

            if Reg:
                statistics(0)

            if func.__class__.__name__ == 'type':
                func_Time = statistics(1)
                return func_Time

            value_function = func.__annotations__
            if value_function.get('return'):  # отчистка от ->
                value_function.pop('return')

            # Если значения переданы без присваивания - fanc(login,password_VK)
            if Items:
                test_Gen_Items = [x for x in zip(
                    value_function.keys(), Items, value_function.values())]
                for x in test_Gen_Items:
                    if x[2] == None:  # pylint: disable=C0121
                        continue
                    if not isinstance(x[1], x[2]):
                        print(x[1], x[2])
                        raise Exception(f'\n\n{func.__name__} *Args-| {x[0]} != {x[2].__name__}\n')

            # Если присваиваться значение - fanc(passwords=password_VK)
            if Dicts:
                test_Gen_Dicts = [list(x)+[value_function.get(x[0])]
                                  for x in zip(Dicts.keys(), Dicts.values())]
                for x in test_Gen_Dicts:
                    if not isinstance(x[1], x[2]):
                        raise Exception(f'\n\n{func.__name__} **Kargs-| {x[0]} != {x[2].__name__}\n')

            if Reg:
                func_Time = statistics(1)
                return func_Time

            return func(*Items, **Dicts)
        return decorator_function
    return actual_decorator


if __name__ == '__main__':
    Check_class()
