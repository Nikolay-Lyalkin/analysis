from sqlalchemy import text

from src.db.mysql import get_session_ctx


class NetworkService:

    def get_more_popular_coffee_in_network(self, name):
        """Показывает наиболее продаваемый кофе в торговой сети"""

        session = get_session_ctx()
        query_magnit = text(
            f"""SELECT brand_name, 
            COUNT(*) as count
            FROM coffee
            WHERE LOWER(network_name) = LOWER('{name}')
            GROUP BY brand_name
            ORDER BY count DESC;"""
        )

        result = session.execute(query_magnit)
        data = [
            {"brand_name": row.brand_name, "count": row.count} for row in result.all()
        ]

        session.close()
        return data

    def get_more_popular_volume_3in1_in_network(self, name):
        """Показывает востребованность упаковок 3в1"""

        session = get_session_ctx()
        query = text(
            f"""select
            case
            when product_name like '%13,5%' or product_name like '%13%' then '13 г'
            when product_name like '%14,5%' or product_name like '%14%' then '14 г'
            when product_name like '%15%' or product_name like '%15,5%' then '15 г'
            when product_name like '%16%' or product_name like '%16,5%' then '16 г'
            when product_name like '%17%' or product_name like '%17,5%' then '17 г'
            when product_name like '%18%' or product_name like '%18,5%' then '18 г'
            when product_name like '%19%' or product_name like '%19,5%' then '19 г'
            when product_name like '%25%' or product_name like '%25,5%' then '25 г'
            when product_name like '%20%' or product_name like '%20,5%'then '20 г'
            else '> 20 г'
            end as packing_volume,
            count(*) as count
            from coffee
            where garbage_name like'%3в1%' or garbage_name like '%3в 1%' and LOWER(network_name) = LOWER('{name}')
            group by packing_volume
            order by count desc;"""
        )

        result = session.execute(query)
        data = [
            {"packing_volume": row.packing_volume, "count": row.count}
            for row in result.all()
        ]
        session.close()
        return data

    def get_more_popular_volume_ground_coffee_in_network(self, name):
        """Показывает востребованность упаковок молотого кофе"""

        session = get_session_ctx()
        query = text(
            f"""WITH extracted_weights AS (
            SELECT *,
            CAST(
            REGEXP_SUBSTR(product_name, '[0-9]+') AS UNSIGNED
            ) AS weight_num
            FROM coffee
            WHERE garbage_name LIKE '%молот%' and lower(network_name) = LOWER('{name}')
            )
            SELECT
            CASE
            WHEN weight_num BETWEEN 10 AND 49 THEN '10-49 г'
            WHEN weight_num BETWEEN 50 AND 99 THEN '50-99 г'
            WHEN weight_num BETWEEN 100 AND 149 THEN '100-149 г'
            WHEN weight_num BETWEEN 150 AND 199 THEN '150-199 г'
            WHEN weight_num BETWEEN 200 AND 249 THEN '200-249 г'
            WHEN weight_num BETWEEN 250 AND 299 THEN '250-299 г'
            WHEN weight_num BETWEEN 300 AND 349 THEN '300-349 г'
            WHEN weight_num BETWEEN 350 AND 399 THEN '350-399 г'
            WHEN weight_num BETWEEN 400 AND 449 THEN '400-449 г'
            WHEN weight_num BETWEEN 450 AND 499 THEN '450-499 г'
            WHEN weight_num BETWEEN 500 AND 549 THEN '500-549 г'
            WHEN weight_num BETWEEN 550 AND 1000 THEN '>550г'
            ELSE 'Иные'
            END AS packing_volume,
            COUNT(*) AS count
            FROM extracted_weights
            GROUP BY packing_volume
            ORDER BY count DESC;"""
        )

        result = session.execute(query)
        data = [
            {"packing_volume": row.packing_volume, "count": row.count}
            for row in result.all()
        ]

        session.close()
        return data

    def get_more_popular_volume_coffee_beans_in_network(self, name):
        """Показывает востребованность упаковок зернового кофе"""

        session = get_session_ctx()
        query = text(
            f"""WITH extracted_weights AS (
            SELECT *,
            CAST(
            REGEXP_SUBSTR(product_name, '[0-9]+') AS UNSIGNED
            ) AS weight_num
            FROM coffee
            WHERE garbage_name LIKE '%зёрн%' and network_name = LOWER('{name}')
            )
            SELECT
            CASE
            WHEN weight_num BETWEEN 2 AND 100 THEN '2-99 г'
            WHEN weight_num BETWEEN 100 AND 199 THEN '100-200г'
            WHEN weight_num BETWEEN 200 AND 299 THEN '200-299 г'
            WHEN weight_num BETWEEN 300 AND 399 THEN '300-399 г'
            WHEN weight_num BETWEEN 400 AND 499 THEN '400-499 г'
            WHEN weight_num BETWEEN 500 AND 599 THEN '500-599 г'
            WHEN weight_num BETWEEN 600 AND 699 THEN '600-699 г'
            WHEN weight_num BETWEEN 700 AND 799 THEN '700-799 г'
            WHEN weight_num BETWEEN 800 AND 899 THEN '800-899 г'
            WHEN weight_num BETWEEN 900 AND 999 THEN '900-999 г'
            WHEN weight_num BETWEEN 1000 AND 1100 THEN '1000-1100г'
            WHEN weight_num BETWEEN 1101 AND 5000 THEN '1101-5000г'
            ELSE 'Иные'
            END AS packing_volume,
            COUNT(*) AS count
            FROM extracted_weights
            GROUP BY packing_volume
            ORDER BY count DESC;"""
        )

        result = session.execute(query)
        data = [
            {"packing_volume": row.packing_volume, "count": row.count}
            for row in result.all()
        ]

        session.close()
        return data

    def get_more_popular_network(self):
        """Показывает востребованность упаковок зернового кофе"""

        session = get_session_ctx()
        query = text(
            f"""SELECT network_name, COUNT(*) AS count
        from coffee
        GROUP BY network_name
        ORDER BY count DESC;"""
        )

        result = session.execute(query)
        data = [
            {"network_name": row.network_name, "count": row.count}
            for row in result.all()
        ]

        session.close()
        return data

    def get_avg_price_in_network(self, name):
        """Демонстрирует среднюю цену по всем брендам в конкретной торговой сети"""
        session = get_session_ctx()
        query = text(
            f"""SELECT brand_name, 
            ROUND(AVG(price), 2) AS count
            FROM coffee
            WHERE LOWER(network_name) = LOWER('{name}')
            GROUP BY brand_name
            ORDER BY count desc;"""
        )

        result = session.execute(query)
        data = [
            {"brand_name": row.brand_name, "count": row.count} for row in result.all()
        ]

        session.close()
        return data


def get_network_service() -> NetworkService:
    result = NetworkService()
    return result
