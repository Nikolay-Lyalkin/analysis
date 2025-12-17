import pandas as pd
import plotly.express as px
import streamlit as st

from src.services.coffee import get_coffee_service


def dashboard_taste_coffee():
    """Дашборд с данными о популярных вкусах"""
    st.set_page_config(
        page_title="Популярные вкусы кофе", page_icon="☕", layout="wide"
    )

    ol1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        # Заголовок
        st.title("☕ Самые популярные вкусы кофе")
        st.markdown("---")

    service_coffee = get_coffee_service()
    # Получаем данные
    with st.spinner("Загрузка данных о вкусах..."):
        data = service_coffee.get_more_popular_taste()

    if not data:
        st.warning("Нет данных для отображения")
        return
    df = pd.DataFrame(data).iloc[1:11]
    df = df.rename(
        columns={"normalized_name": "Название вкуса", "count": "Количество покупок"}
    )
    col1, col2 = st.columns(2)
    with col2:
        st.subheader("Таблица данных")
        st.dataframe(df, use_container_width=True)
    with col1:
        st.subheader("График популярности")
        fig = px.bar(df, x="Название вкуса", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Название вкуса",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)


def dashboard_packing_volume():
    """Дашборд с данными о популярных вкусах"""
    st.set_page_config(
        page_title="Востребованность объёма упаковок", page_icon="☕", layout="wide"
    )

    ol1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        # Заголовок
        st.title("☕ Востребованность объёма упаковок")
        st.markdown("---")

    service_coffee = get_coffee_service()
    # Получаем данные
    with st.spinner("Загрузка данных о ..."):
        data_3in1 = service_coffee.get_more_popular_volume_3in1()
        data_ground_coffee = service_coffee.get_more_popular_volume_ground_coffee()
        data_coffee_beans = service_coffee.get_more_popular_volume_coffee_beans()

    if not data_3in1 or not data_ground_coffee or not data_coffee_beans:
        st.warning("Нет данных для отображения")
        return
    df_3in1 = pd.DataFrame(data_3in1).iloc[0:5]
    df_3in1 = df_3in1.rename(
        columns={"packing_volume": "Объём упаковки", "count": "Количество покупок"}
    )
    df_ground_coffee = pd.DataFrame(data_ground_coffee).iloc[0:5]
    df_ground_coffee = df_ground_coffee.rename(
        columns={"packing_volume": "Объём упаковки", "count": "Количество покупок"}
    )
    df_coffee_beans = pd.DataFrame(data_coffee_beans).iloc[0:5]
    df_coffee_beans = df_coffee_beans.rename(
        columns={"packing_volume": "Объём упаковки", "count": "Количество покупок"}
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "<h3 style='text-align: center;'>Кофе 3в1</h3>", unsafe_allow_html=True
        )
        fig = px.bar(df_3in1, x="Объём упаковки", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Объём упаковки",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(
            "<h3 style='text-align: center;'>Молотый кофе</h3>", unsafe_allow_html=True
        )
        fig = px.bar(df_ground_coffee, x="Объём упаковки", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Объём упаковки",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.markdown(
            "<h3 style='text-align: center;'>Кофе в зёрнах</h3>", unsafe_allow_html=True
        )
        fig = px.bar(df_coffee_beans, x="Объём упаковки", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Объём упаковки",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)
