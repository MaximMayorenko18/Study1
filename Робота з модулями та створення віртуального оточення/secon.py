def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                id, name, age = line.strip().split(',')
                cat_dict = {
                    "id": id,
                    "name": name,
                    "age": int(age)
                }
                cats_list.append(cat_dict)
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    return cats_list
print(get_cats_info("D:\\Cat.txt"))