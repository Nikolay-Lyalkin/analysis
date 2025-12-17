import pandas as pd
import plotly.express as px
import streamlit as st

from src.services.network import get_network_service


def dashboard_more_popular_network():
    """Дашборд с данными о самой популярной сети"""
    st.set_page_config(page_title="Виды кофе", page_icon="☕", layout="wide")

    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center;'>☕ Торговые сети</h2>", unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("---")
    st.markdown(
        "<h3 style='text-align: center;'>Торговые сети с самыми большими продажами</h3>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    service_coffee = get_network_service()
    # Получаем данные
    with st.spinner("Загрузка данных о ..."):
        data = service_coffee.get_more_popular_network()

    if not data:
        st.warning("Нет данных для отображения")
        return

    df = pd.DataFrame(data).iloc[0:20]
    df = df.rename(
        columns={"network_name": "Наименование сети", "count": "Количество продаж"}
    )

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Таблица данных")
        st.dataframe(df, use_container_width=True)

    with col2:
        fig = px.pie(df, names="Наименование сети", values="Количество продаж")
        st.plotly_chart(fig, use_container_width=True)


def dashboard_coffee_network():
    """Дашборд с данными о торговых сетях и их реализации кофе"""
    st.set_page_config(page_title="Виды кофе", page_icon="☕", layout="wide")

    st.markdown("---")
    st.markdown(
        "<h3 style='text-align: center;'>Анализ популярности брендов в тороговых сетях</h3>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    service_coffee = get_network_service()
    # Получаем данные
    with st.spinner("Загрузка данных о ..."):
        data_magnit = service_coffee.get_more_popular_coffee_in_network("магнит")
        data_x5 = service_coffee.get_more_popular_coffee_in_network("пятёрочка")
        data_ozon = service_coffee.get_more_popular_coffee_in_network("ozon.ru")

    if not data_magnit or not data_x5 or not data_ozon:
        st.warning("Нет данных для отображения")
        return

    df_magnit = pd.DataFrame(data_magnit).iloc[0:5]
    df_magnit = df_magnit.rename(
        columns={"brand_name": "Брэнд кофе", "count": "Количество покупок"}
    )

    df_x5 = pd.DataFrame(data_x5).iloc[0:5]
    df_x5 = df_x5.rename(
        columns={"brand_name": "Брэнд кофе", "count": "Количество покупок"}
    )

    df_ozon = pd.DataFrame(data_ozon).iloc[0:5]
    df_ozon = df_ozon.rename(
        columns={"brand_name": "Брэнд кофе", "count": "Количество покупок"}
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            "<h2 style='text-align: center;'>Магнит</h2>", unsafe_allow_html=True
        )
        fig = px.bar(df_magnit, x="Брэнд кофе", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Брэнд кофе",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown(
            "<h2 style='text-align: center;'>Пятерочка</h2>", unsafe_allow_html=True
        )
        fig = px.bar(df_x5, x="Брэнд кофе", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Брэнд кофе",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.markdown("<h2 style='text-align: center;'>OZON</h2>", unsafe_allow_html=True)
        fig = px.bar(df_ozon, x="Брэнд кофе", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="Брэнд кофе",
            xaxis_title_font=dict(size=20),
            yaxis_title="Количество покупок",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)


def dashboard_coffee_value_network(network):
    """Дашборд с данными о наиболее востребованных упаковках кофе"""
    st.set_page_config(page_title="Виды кофе", page_icon="☕", layout="wide")

    service_coffee = get_network_service()
    # Получаем данные
    with st.spinner("Загрузка данных о ..."):
        data_3in1 = service_coffee.get_more_popular_volume_3in1_in_network(network)
        data_ground_coffee = (
            service_coffee.get_more_popular_volume_ground_coffee_in_network(network)
        )
        data_beans_coffee = (
            service_coffee.get_more_popular_volume_coffee_beans_in_network(network)
        )

        if not data_3in1:
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

        df_beans_coffee = pd.DataFrame(data_beans_coffee).iloc[0:5]
        df_beans_coffee = df_beans_coffee.rename(
            columns={"packing_volume": "Объём упаковки", "count": "Количество покупок"}
        )
        st.markdown(
            f"<h3 style='text-align: center;'>{network}</h3>", unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            fig = px.bar(
                df_3in1,
                x="Объём упаковки",
                y="Количество покупок",
                color="Объём упаковки",
            )
            # Переименовываем оси
            fig.update_layout(
                xaxis_title="Кофе 3в1",
                xaxis_title_font=dict(size=20),
                yaxis_title="Количество покупок",
                yaxis_title_font=dict(size=16),
            )
            fig.update_xaxes(showticklabels=False)
            st.plotly_chart(fig, use_container_width=True, key=f"3in1_{network}")

        with col2:
            fig = px.bar(
                df_ground_coffee,
                x="Объём упаковки",
                y="Количество покупок",
                color="Объём упаковки",
            )
            # Переименовываем оси
            fig.update_layout(
                xaxis_title="Молотый кофе",
                xaxis_title_font=dict(size=20),
                yaxis_title="Количество покупок",
                yaxis_title_font=dict(size=16),
            )
            fig.update_xaxes(showticklabels=False)
            st.plotly_chart(
                fig, use_container_width=True, key=f"ground_coffee_{network}"
            )

        with col3:
            fig = px.bar(
                df_beans_coffee,
                x="Объём упаковки",
                y="Количество покупок",
                color="Объём упаковки",
            )
            # Переименовываем оси
            fig.update_layout(
                xaxis_title="Кофе в зёрных",
                xaxis_title_font=dict(size=20),
                yaxis_title="Количество покупок",
                yaxis_title_font=dict(size=16),
            )
            fig.update_xaxes(showticklabels=False)
            st.plotly_chart(fig, use_container_width=True, key=f"chart_beans_{network}")


def dashboard_avg_price(network):
    """Дашборд с данными о средней цене кофе в торговых сетях"""
    st.set_page_config(page_title="Виды кофе", page_icon="☕", layout="wide")

    service_coffee = get_network_service()
    # Получаем данные
    with st.spinner("Загрузка данных о ..."):
        data = service_coffee.get_avg_price_in_network(network)

        if not data:
            st.warning("Нет данных для отображения")
            return

        df_fig = pd.DataFrame(data).iloc[0:10]
        df_tab = pd.DataFrame(data)
        df_fig = df_fig.rename(
            columns={"brand_name": "Наименование бренда", "count": "Средняя цена"}
        )
        df_tab = df_tab.rename(
            columns={"brand_name": "Наименование бренда", "count": "Средняя ценак"}
        )

        st.markdown(
            f"<h3 style='text-align: center;'>{network}</h3>", unsafe_allow_html=True
        )
        col1, col2 = st.columns(2)
        with col1:
            fig = px.bar(
                df_fig,
                x="Наименование бренда",
                y="Средняя цена",
                color="Наименование бренда",
            )
            # Переименовываем оси
            fig.update_layout(
                xaxis_title="",
                xaxis_title_font=dict(size=20),
                yaxis_title="Средняя цена",
                yaxis_title_font=dict(size=16),
            )
            fig.update_xaxes(showticklabels=False)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.subheader("")
            st.dataframe(df_tab, use_container_width=True)
