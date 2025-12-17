import pandas as pd
import plotly.express as px
import streamlit as st

from src.services.coffee import get_coffee_service


def dashboard_packing_volume():
    """Дашборд с данными о популярных вкусах"""
    st.set_page_config(
        page_title="Востребованность объёма упаковок", page_icon="☕", layout="wide"
    )

    service_coffee = get_coffee_service()
    # Получаем данные
    with st.spinner("Загрузка данных о ..."):
        data_3in1 = service_coffee.get_more_popular_volume_3in1()
        data_ground_coffee = service_coffee.get_more_popular_volume_ground_coffee()
        data_coffee_beans = service_coffee.get_more_popular_volume_coffee_beans()
        data_type_pack = service_coffee.get_more_popular_type_pack()

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

    df_type_pack = pd.DataFrame(data_type_pack).iloc[0:5]
    df_type_pack = df_type_pack.rename(
        columns={"cover_name": "Тип упаковки", "count": "Количество покупок"}
    )

    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center;'>☕ Тип упаковки</h2>", unsafe_allow_html=True
    )
    st.markdown("---")
    fig = px.bar(df_type_pack, x="Тип упаковки", y="Количество покупок")
    # Переименовываем оси
    fig.update_layout(
        xaxis_title="",
        xaxis_title_font=dict(size=20),
        yaxis_title="Количество покупок",
        yaxis_title_font=dict(size=16),
    )
    st.plotly_chart(fig, use_container_width=True)

    ol1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        # Заголовок
        st.markdown("---")
        st.title("☕ Востребованность объёма упаковок")
        st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "<h3 style='text-align: center;'>Кофе 3в1</h3>", unsafe_allow_html=True
        )
        fig = px.bar(
            df_3in1, x="Объём упаковки", y="Количество покупок", color="Объём упаковки"
        )
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Объём упаковки",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(
            "<h3 style='text-align: center;'>Молотый кофе</h3>", unsafe_allow_html=True
        )
        fig = px.bar(
            df_ground_coffee,
            x="Объём упаковки",
            y="Количество покупок",
            color="Объём упаковки",
        )
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Объём упаковки",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.markdown(
            "<h3 style='text-align: center;'>Кофе в зёрнах</h3>", unsafe_allow_html=True
        )
        fig = px.bar(
            df_coffee_beans,
            x="Объём упаковки",
            y="Количество покупок",
            color="Объём упаковки",
        )
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Объём упаковки",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
            showlegend=False,
        )
        st.plotly_chart(fig, use_container_width=True)
