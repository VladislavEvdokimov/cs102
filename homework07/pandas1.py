# -*- coding: utf-8 -*-
"""assignment01_adult_pandas (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DL4r--P2g4vHb-rMHB-NIF-GGwKIOJbg

<img src="../../img/ods_stickers.jpg">

## <center> [mlcourse.ai](https://mlcourse.ai) – открытый курс OpenDataScience по машинному обучению

Автор материала: Юрий Кашницкий (@yorko в Slack ODS). Материал распространяется на условиях лицензии [Creative Commons CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). Можно использовать в любых целях (редактировать, поправлять и брать за основу), кроме коммерческих, но с обязательным упоминанием автора материала.

# <center>Домашнее задание № 1 (демо).<br> Анализ данных по доходу населения UCI Adult</center>

**В задании предлагается с помощью Pandas ответить на несколько вопросов по данным репозитория UCI [Adult](https://archive.ics.uci.edu/ml/datasets/Adult) (качать данные не надо – они уже есть в репозитории). Для отправки решений используйте [онлайн-форму](https://docs.google.com/forms/d/1xAzU-5N6oEeR4UG8G44V6XL-Kbr4WYcPBG45Kijge2Y).**

Уникальные значения признаков (больше информации по ссылке выше):
- age: continuous.
- workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
- fnlwgt: continuous.
- education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
- education-num: continuous.
- marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
- occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
- relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
- sex: Female, Male.
- capital-gain: continuous.
- capital-loss: continuous.
- hours-per-week: continuous.
- native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
- salary: >50K,<=50K
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import io
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv("adult.csv", delimiter=",", names = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"])

df.head()

"""**1. Сколько мужчин и женщин (признак *sex*) представлено в этом наборе данных?**"""

df['sex'].value_counts()

"""**2. Каков средний возраст (признак *age*) женщин?**"""

print('Средний возраст женщин', df.groupby('sex').age.mean()[:1])

"""**3. Какова доля граждан Германии (признак *native-country*)?**"""

print('Доля граждан Германиии', df['native-country'].value_counts(['Germany'])[4:5])

"""**4-5. Каковы средние значения и среднеквадратичные отклонения возраста тех, кто получает более 50K в год (признак *salary*) и тех, кто получает менее 50K в год? **"""

dm = df.groupby('salary')[['age']].mean()
ds = df.groupby('salary')[['age']].std()
d = pd.concat([dm,ds],axis=1)
d.columns = ['mean','std']
print(d)

"""**6. Правда ли, что люди, которые получают больше 50k, имеют как минимум высшее образование? (признак *education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters* или *Doctorate*)**"""

df.groupby(["education", "salary"]).salary.describe()

"""**7. Выведите статистику возраста для каждой расы (признак *race*) и каждого пола. Используйте *groupby* и *describe*. Найдите таким образом максимальный возраст мужчин расы *Amer-Indian-Eskimo*.**"""

for (race, sex), sub_df in df.groupby(['race', 'sex']):
    print("Race: {0}, sex: {1}".format(race, sex))
    print(sub_df['age'].describe())

df.groupby(['race', 'sex']).age.max().reset_index()[1:2]

"""**8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак *marital-status*)? Женатыми считаем тех, у кого *marital-status* начинается с *Married* (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.**"""

df[
    (df["sex"] == "Male")
    & (df["marital-status"].isin(["Never-married", "Separated", "Divorced"]))
]["salary"].value_counts()

df[(df["sex"] == "Male") & (df["marital-status"].str.startswith("Married"))][
    "salary"
].value_counts()

df["marital-status"].value_counts()

wealthy = df[df['salary']=='>50K']

wealthy['marital-status'].unique()

df[(df['sex'] == 'Male') & df['marital-status'].isin(['Never-married', 'Separated', 'Divorced'])]['salary'].value_counts()
df[(df['sex'] == 'Male') & (df['marital-status'].str.startswith('Married'))]['salary'].value_counts()

"""**9. Какое максимальное число часов человек работает в неделю (признак *hours-per-week*)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?**"""

max_load = df["hours-per-week"].max()
print("Max time - {0} hours./week.".format(max_load))

num_workaholics = df[df["hours-per-week"] == max_load].shape[0]
print("Total number of such hard workers {0}".format(num_workaholics))

rich_share = (float(df[(df["hours-per-week"] == 99) & (df["salary"] == ">50K")].shape[1]) / num_workaholics)
df[(df["hours-per-week"] == 99) & (df["salary"] == ">50K")].shape[1]
print("Percentage of rich among them {0}%".format(float(100 * rich_share)))

"""**10. Посчитайте среднее время работы (*hours-per-week*) зарабатывающих мало и много (*salary*) для каждой страны (*native-country*).**"""

pd.crosstab(
    df["native-country"],
    df["salary"],
    values=df["hours-per-week"],
    aggfunc=np.mean,
).T