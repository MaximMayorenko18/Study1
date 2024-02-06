def total_salary(path):
    try:
        total_sum = 0
        developers_count = 0
        
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_sum += int(salary)
                developers_count += 1
        
        average_salary = total_sum / developers_count if developers_count else 0
        return total_sum, average_salary
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

print(total_salary("D:\\ZP.txt"))
