import pandas as pd


article_read = pd.read_csv(
        'https://github.com/putilov-va/pythonProject3/raw/refs/heads/main/kc_house_data.csv',
# article_read = pd.read_csv(
#         'kc_house_data.csv',
        delimiter=',',
        usecols=["price", 'floors', "bedrooms", "lat", "long"]
        ) #
  #  Разделение основного файла на два файла
k = 2           # Количество файлов
size = 4        # Количество строк
for i in range(k):
        house_data = article_read[size * i: size * (i + 1)]      #
        house_data.to_csv(f'kc_house_data_{i + 1}.csv', index=False)    #  Присвоение Имени файлу

house_data_1 = pd.read_csv(
        "kc_house_data_1.csv",
        # delimiter=',',
        # header=0,
        index_col=["bedrooms"],
        usecols=["price", 'floors', "bedrooms", "lat", "long"]
        )
print(f'\n Начало первой части файла "kc_house_data".')
print(f'{house_data_1}\n')

# house_data_2 = house_data.read_csv(
#         "kc_house_data_2.csv",
#         # delimiter=',',
#         # header=0,
#         index_col=["bedrooms"],
#         usecols=["price", 'floors', "bedrooms", "lat", "long"],
#         nrows=6)

# # print( f'{house_data_2}\n')
#
# # print(article_read)           #
# # ar = article_read.tail(15)    #
# # ar = article_read.describe(5) #
# # ar = article_read.head(10)       #

# Создаём отдельный файл по этажности- 3,5.
for (floors), group in article_read.groupby(['floors']):
        group.to_csv(f'floors_{floors}.csv', index=False)
print(f'Этажность: 3,5')
print(pd.read_csv(
        "floors_(3.5,).csv",
        usecols=["price", 'floors', 'bedrooms', "lat", "long"]
        ))

# Группируем по количеству комнат, и Определяем среднее значение стоимости (mean).
ar_g = article_read.groupby('bedrooms')['price'].mean() #
print(f'\nСреднее значение стоимости относительно количества комнат')
print(f'{ar_g}\n')

bedrooms_2 = article_read[article_read.bedrooms == 2]
print(f'Стоимость двух комнатных домов')
print(bedrooms_2)