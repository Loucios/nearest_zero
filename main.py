def input_data() -> 'list[int, list[int]]':
    length_street = int(input())

    street = input()
    street = street.split(' ')
    street = list(map(int, street))

    return [length_street, street]


# ID 52516422
class NearestZero():
    '''Решение задачи Ближайший ноль.

    1. Заполняем пустой лист result_distances бесконечностями.
    Длина листа как у "улицы".
    2. С перового нуля проходим по "улице" в конец, вычисляя расстояния
    до участков. Записываем в лист result_distances
    min(текущая дистанция от предыдущего 0, result_distances[текущий индекс]).
    3. С последнего нуля идём в начало "улицы" беря
    min(текущая дистанция от предыдущего 0, result_distances[текущий индекс]).
    '''
    def __init__(self, length_street, street, search_number=0):
        self.length_street = length_street
        self.street = street
        self.search_number = search_number

    def __run_the_street(self, result_distances, is_back=False):

        empty_lot = -1
        for i in range(self.length_street):

            if is_back:
                j = - (i + 1)
            else:
                j = i

            if self.street[j] == self.search_number:
                empty_lot = i

            if empty_lot != -1:
                result_distances[j] = min(result_distances[j], i - empty_lot)

        return result_distances

    def get_result(self) -> 'list[int]':
        result_distances = [float('inf') for q in range(self.length_street)]
        result_distances = self.__run_the_street(result_distances)
        return self.__run_the_street(result_distances, is_back=True)

    def __str__(self) -> str:
        result = self.get_result()
        return ' '.join(map(str, result))


def main():
    length_street, street = input_data()

    nearest_zero = NearestZero(length_street, street)

    print(nearest_zero)


if __name__ == "__main__":
    main()
