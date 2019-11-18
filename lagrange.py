import csv

def get_values():
    with open('cidade06.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        return list(csv_reader)

def get_x_and_y(values):
    x_list = []
    y_list = []

    for value in values:
        if value[0].isnumeric():
            x_list.append(float(value[0]))
            y_list.append(float(value[1].replace(",", ".")))

    return x_list, y_list


if __name__ == '__main__':
    values = get_values()
    x_list, y_list = get_x_and_y(values)
