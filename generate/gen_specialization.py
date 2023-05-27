import json

text = """
1. Кардиология
2. Пульмонология
3. Неврология
4. Гастроэнтерология
5. Онкология
6. Эндокринология
7. Аллергология и иммунология
8. Дерматология
9. Ортопедия
10. Урология
11. Гинекология
12. Педиатрия
13. Офтальмология
14. Отоларингология
15. Нейрохирургия
16. Ревматология
17. Акушерство
18. Гериатрия
19. Эндоскопия
20. Реабилитация и физиотерапия
"""

lines = text.strip().split('\n')

data = {}

for line in lines:
    parts = line.strip().split('. ')
    print(parts)
    number = parts[0]
    description = parts[1]
    data[number] = description

json_data = json.dumps(data, indent=4, ensure_ascii=False)

with open('specialization.json', 'w') as file:
    file.write(json_data)

print("JSON файл успешно создан.")
