import json
import random


def load_data_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        print(data)
    return data


def generate_random_temperature(min_temp, max_temp):

    return random.uniform(min_temp, max_temp)



def check_temperature(stanki_data, stank_number, current_temperature):
    if stank_number in stanki_data:
        min_temp = stanki_data[stank_number]['min_temp']
        max_temp = stanki_data[stank_number]['max_temp']
        print(current_temperature, current_temperature)
        if current_temperature < min_temp or current_temperature > max_temp:
            return True, {'stank_number': stank_number, 'critical_temperature': current_temperature}

    return False, None


def main(input_file, output_file):
    # Загрузка данных из JSON файла
    stanki_data = load_data_from_json(input_file)

    # Генерация случайных данных для проверки
    random_stank_number = random.choice(list(stanki_data.keys()))
    random_temperature = generate_random_temperature(
        stanki_data[random_stank_number]['min_temp'],
        stanki_data[random_stank_number]['max_temp']
    )

    # Проверка текущей температуры
    is_critical, critical_info = check_temperature(stanki_data, random_stank_number, random_temperature)

    # Если найдена критическая температура, записываем в файл
    if is_critical:
        with open(output_file, 'w') as f:
            json.dump(critical_info, f, indent=4)
            print(f"Critical temperature detected and written to {output_file}: {critical_info}")


if __name__ == "__main__":
    input_file = 'stanki_data.json'  # Замените на ваш файл с данными
    output_file = 'critical_temperature.json'  # Файл для записи критической температуры
    main(input_file, output_file)
