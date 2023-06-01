# TODO Написать 3 класса с документацией и аннотацией типов
def check(min_num, max_num, units):
    def decorate(func):
        def wrapper(*arg):
            if isinstance(arg[-1], (int, float)):

                if not max_num >= arg[-1] >= min_num:
                    raise ValueError(
                        f"Значение должно находиться в промежутке от {min_num}{units} до {max_num}{units}. Введенное значение -  {arg[-1]}")
                else:
                    ret = list(func(arg[0], arg[-1]))
                    return ret[0]
            else:
                raise ValueError(f"Значение должно быть числом (типа int или float)")

        return wrapper

    return decorate


class Giraffe:
    def __init__(self, weight, neck_length, spots):
        self.neck_length = self.check_neck_len(neck_length)
        self.spots = self.check_spots(spots)
        self.weight = self.check_weight(weight)
        print(self.neck_length, self.spots, self.weight)

    @check(min_num=2000, max_num=3000, units='см')
    def check_neck_len(self, *neck_length):
        return neck_length

    @check(min_num=400, max_num=500, units='ед')
    def check_spots(self, *spots):
        return spots

    @check(min_num=550, max_num=1900, units='кг')
    def check_weight(self, *weight):
        return weight


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest

    tomas = Giraffe(555, 2000, 456)
    print(tomas.neck_length)
