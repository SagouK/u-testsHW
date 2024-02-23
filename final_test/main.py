# Задание 1. Создайте программу на Python или Java, которая принимает два списка чисел и выполняет следующие действия:
# a. Рассчитывает среднее значение каждого списка.
# b. Сравнивает эти средние значения и выводит соответствующее сообщение:
# - ""Первый список имеет большее среднее значение"", если среднее значение первого списка больше.
# - ""Второй список имеет большее среднее значение"", если среднее значение второго списка больше.
# - ""Средние значения равны"", если средние значения списков равны.


import pytest


class AverageNumber:
    @staticmethod
    def find_avg(nums1: list, nums2: list):
        if not isinstance(nums1, list) or not isinstance(nums2, list):
            raise TypeError('Переданный объект не является list')
        if not nums1 or not nums2:
            return 0
        avg_1 = sum(nums1) / len(nums1)
        avg_2 = sum(nums2) / len(nums2)
        tuple_args = (avg_1, avg_2)
        return tuple_args

    @staticmethod
    def compare_args(tuple_args: tuple) -> str:
        if tuple_args[0] == tuple_args[1]:
            str_ing = 'Средние значения равны'
        elif tuple_args[0] > tuple_args[1]:
            str_ing = 'Первый список имеет большее среднее значение'
        else:
            str_ing = 'Второй список имеет большее среднее значение'
        return str_ing


class TestLists:
    def test_find_avg(self):
        assert AverageNumber.find_avg([1, 2, 3], [4, 5, 6]) == (2, 5), \
            'Ожидаемое не сошлось с фактическим'
        assert AverageNumber.find_avg([5], [3]) == (5, 3)
        assert AverageNumber.find_avg([5, 8], [4, 3, 2]) == (6.5, 3)

    def test_zero(self):
        assert AverageNumber.find_avg([], []) == 0
        assert AverageNumber.find_avg([], [2, 5]) == 0

    def test_negative(self):
        assert AverageNumber.find_avg([-1, -2, -3], [-4, -5, -6]) == (-2, -5)

    def test_find_avg_type(self):
        with pytest.raises(TypeError):
            AverageNumber.find_avg('qwe', 1)
            # AverageNumber.find_avg([1, 3], [2, 3])

    def test_compares(self):
        assert AverageNumber.compare_args((3, 3)) == 'Средние значения равны'
        assert AverageNumber.compare_args((4, 3)) == 'Первый список имеет большее среднее значение'
        assert AverageNumber.compare_args((3, 7)) == 'Второй список имеет большее среднее значение'


if __name__ == '__main__':
    print(AverageNumber.compare_args(AverageNumber.find_avg([3, 9, 5], [4, 19])))
