import streamlit as st

from src.handlers.coffee_network import (
    dashboard_avg_price,
    dashboard_coffee_network,
    dashboard_coffee_value_network,
    dashboard_more_popular_network,
)
from src.handlers.coffee_taste import dashboard_taste_coffee
from src.handlers.coffee_view import dashboard_view_coffee
from src.handlers.coffee_volume import dashboard_packing_volume
from src.services.coffee import get_coffee_service
from src.services.doc import get_doc_service


if __name__ == "__main__":
    doc_service = get_doc_service()
    date = doc_service.read_doc(
        "C:/Users/sereg/OneDrive/Рабочий стол/Dev/analysis/src/Задание.xlsx"
    )
    coffee_service = get_coffee_service()
    coffee_service.add_product_in_db(date)

    tab1, tab2 = st.tabs(["📊 Анализ кофе", "📈 Анализ торговых сетей"])
    with tab1:
        dashboard_view_coffee()
        dashboard_taste_coffee()
        dashboard_packing_volume()
    with tab2:
        dashboard_more_popular_network()
        dashboard_coffee_network()
        st.markdown("---")
        st.markdown(
            "<h3 style='text-align: center;'>Анализ объёма упаковок</h3>",
            unsafe_allow_html=True,
        )
        st.markdown("---")
        dashboard_coffee_value_network("Магнит")
        dashboard_coffee_value_network("Пятерочка")
        dashboard_coffee_value_network("OZON.ru")
        st.markdown("---")
        st.markdown(
            "<h3 style='text-align: center;'>Анализ средней цены на полках в торговых сетях</h3>",
            unsafe_allow_html=True,
        )
        st.markdown("---")
        dashboard_avg_price("Магнит")
        dashboard_avg_price("Пятерочка")
        dashboard_avg_price("OZON.ru")
