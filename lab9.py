import streamlit as st
import matplotlib.pyplot as plt

with open("data.csv") as f:
    st.title("Подсчитать количество погибших мужчин старше указанного возраста по каждому пункту посадки")
    option=st.slider("Выберите возрастной порог", min_value=1, max_value=100)
    notSurvivedC = 0
    notSurvivedQ = 0
    notSurvivedS = 0
    next(f)
    for line in f:
        data = line.split(",")
        sex = data[5]
        port=data[12].strip()
        if data[6] != "":
            age = float(data[6])
        if sex == "male" and age >option:
            if port == "C":
                notSurvivedC+=1
            if port == "Q":
                notSurvivedQ+=1
            if port == "S":
                notSurvivedS+=1
    table = st.table({"Порт": ["Шербур", "Квинстаун", "Саутгемптон"], "Погибших": [notSurvivedC, notSurvivedQ, notSurvivedS]})
    fig = plt.figure(figsize=(10, 5))
    plt.xlabel("Порт")
    plt.ylabel("Количество")
    plt.title("Количество погибших мужчин старше выбранного возраста")
    plt.bar(["Шербур", "Квинстаун", "Саутгемптон"], [notSurvivedC, notSurvivedQ, notSurvivedS])
    st.pyplot(fig)
