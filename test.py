ids = ['1111:271', '1111:190', '1231:106', '1211:104', '1111:201', '1231:120', '1001:205', '1001:223', '1001:127', '1001:236', \
      '1111:229', '1231:286', '1231:195', '1001:279', '1001:124', '1111:292', '1505:219', '1231:259', '1231:253', '1001:220', '1001:202',\
      '1231:103', '1211:249', '1212:275']
count = [111, 3, 13, 111, 9, 5, 17, 10, 13, 3, 16, 4, 16, 11, 18, 12, 14, 4, 3, 2, 14, 14, 10, 10]


# Ваш код здесь
items_count = dict(zip(ids, count))


def create_category(items_count):
    category = {}
    for k,v in items_count.items():
        s1, s2 = k.split(':')
        category.setdefault(s1, {})[s2] = v
    return category

def average_count(items):
    return sum(items.values())

category = create_category(items_count)

category_avg = round(sum(average_count(category[cat]) for cat in category) / len(category), 1)
avg_count = sum(len(category[cat]) for cat in category) / len(category)
cat_with_max = [k for k, v in items_count.items() if v == max(items_count.values())]

print("Количество уникальных категорий:\n", len({ item.split(':')[0] for item in ids}))
print('Среднее количество **единиц товара** на складе в категории\n', category_avg)
print('Среднее количество **уникальных товаров** в категории\n', avg_count)
print('ID товаров с максимальным количеством единиц на складе\n', cat_with_max)
