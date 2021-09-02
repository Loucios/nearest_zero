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
    def __init__(self, length_street, street, nearest_number=0) -> None:
        self.length_street = length_street
        self.street = street
        self.nearest_number = nearest_number

    def get_result(self) -> 'list[int]':

        def run_iterrator(iterrator) -> int:

            distance, symbol_index = None, None
            for i in iterrator:
                if self.street[i] == 0:
                    distance = 0
                    symbol_index = i
                result_distances[i] = min(result_distances[i], distance)
                distance += 1
            return symbol_index

        result_distances = [float('inf')] * self.length_street
        last_symbol_index = run_iterrator(
            range(self.street.index(self.nearest_number), self.length_street)
        )
        run_iterrator(reversed(range(last_symbol_index + 1)))

        return result_distances

    def __str__(self) -> str:
        result = self.get_result()
        return ' '.join(map(str, result))


def main():
    try:
        length_street = int(input())
        street = [int(house) for house in input().split()]
    except ValueError as e:
        print(f'Wrong input {e}')
        return

    nearest_zero = NearestZero(length_street, street)

    print(nearest_zero)


if __name__ == "__main__":
    main()
