import pandas as pd
import plotly.express as px
import streamlit as st

from src.services.coffee import get_coffee_service


def dashboard_view_coffee():
    """Дашборд с данными о популярных вкусах"""
    st.set_page_config(page_title="Виды кофе", page_icon="☕", layout="wide")

    st.markdown("---")
    st.markdown(
        "<h2 style='text-align: center;'>☕ Виды кофе</h2>", unsafe_allow_html=True
    )
    st.markdown("---")
    service_coffee = get_coffee_service()
    # Получаем данные
    with st.spinner("Загрузка данных о ..."):
        data = service_coffee.get_more_popular_view_coffee()

    if not data:
        st.warning("Нет данных для отображения")
        return
    df = pd.DataFrame(data).iloc[1:6]
    df = df.rename(columns={"type_coffee": "Тип кофе", "count": "Количество покупок"})

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Таблица данных")
        st.dataframe(df, use_container_width=True)

    with col2:
        fig = px.bar(df, x="Тип кофе", y="Количество покупок")
        # Переименовываем оси
        fig.update_layout(
            xaxis_title="",
            xaxis_title_font=dict(size=20),
            yaxis_title="",
            yaxis_title_font=dict(size=16),
        )
        st.plotly_chart(fig, use_container_width=True)
