from sqlalchemy import text

from src.db.mysql import get_session_ctx
from src.models.coffee import Coffee


class CoffeeService:

    def add_product_in_db(self, products: list[dict]):
        session = get_session_ctx()
        for product in products:
            coffee = Coffee(
                city_name=product.get("city_name"),
                shop_type_name=product.get("shop_type_name"),
                network_name=product.get("network_name"),
                brand_owner_name=product.get("brand_owner_name"),
                brand_name=product.get("brand_name"),
                subbrand_name=product.get("subbrand_name"),
                garbage_name=product.get("garbage_name"),
                product_name=product.get("product_name"),
                quantity=product.get("quantity"),
                price=product.get("price"),
                cover_name=product.get("cover_name"),
            )
            session.add(coffee)

        session.commit()

        return "База данных успешно заполнена"

    def get_more_popular_taste(self):
        """Наиболее популярные вкусы"""
        session = get_session_ctx()
        query = text(
            """SELECT 
                CASE 
                WHEN LOWER(TRIM(subbrand_name)) IN ('классик', 'classic') 
                THEN 'классик'
                ELSE TRIM(subbrand_name)  -- Обрезаем пробелы у всех остальных
                END as normalized_name,
                COUNT(*) as count 
                FROM coffee 
                GROUP BY normalized_name 
                ORDER BY count DESC;"""
        )

        result = session.execute(query)
        data = [
            {"normalized_name": row.normalized_name, "count": row.count}
            for row in result.all()
        ]
        session.close()
        return data

    def get_more_popular_view_coffee(self):
        """Наиболее популярный вид кофе(3в1, растворимый и т.д"""
        """SET SESSION sql_mode = (SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''));"""

        session = get_session_ctx()
        query = text(
            """select
        case 
        when product_name like '%раствор%' then 'Растворимый кофе'
        when product_name like '%молот%' then 'Молотый кофе'
        when product_name like '%3в 1%' or garbage_name LIKE '%3в1%' then 'Кофе 3в1'
        when product_name like '%зерн%' then 'Кофе в зёрнах'
        when product_name like '%капсул%' then 'Кофе в капсулах'
        else 'Другой' 
        end as type_coffee,
        count(*) count
        from coffee
        group by type_coffee
        order by count desc;"""
        )

        result = session.execute(query)
        data = [
            {"type_coffee": row.type_coffee, "count": row.count} for row in result.all()
        ]
        session.close()
        return data

    def get_more_popular_volume_3in1(self):
        """Показывает востребованность упаковок 3в1"""

        session = get_session_ctx()
        query = text(
            """select
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
            where garbage_name like'%3в1%' or garbage_name like '%3в 1%'
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

    def get_more_popular_volume_ground_coffee(self):
        """Показывает востребованность упаковок молотого кофе"""

        session = get_session_ctx()
        query = text(
            """WITH extracted_weights AS (
            SELECT *,
            CAST(
            REGEXP_SUBSTR(product_name, '[0-9]+') AS UNSIGNED
            ) AS weight_num
            FROM coffee
            WHERE garbage_name LIKE '%молот%'
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

    def get_more_popular_volume_coffee_beans(self):
        """Показывает востребованность упаковок зернового кофе"""

        session = get_session_ctx()
        query = text(
            """WITH extracted_weights AS (
            SELECT *,
            CAST(
            REGEXP_SUBSTR(product_name, '[0-9]+') AS UNSIGNED
            ) AS weight_num
            FROM coffee
            WHERE garbage_name LIKE '%зёрн%'
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

    def get_more_popular_type_pack(self):
        """Показывает востребованность типов упаковок"""

        session = get_session_ctx()
        query = text(
            """SELECT cover_name, COUNT(*) 
            AS count
            FROM coffee
            GROUP BY cover_name;"""
        )

        result = session.execute(query)
        data = [
            {"cover_name": row.cover_name, "count": row.count} for row in result.all()
        ]

        session.close()
        return data


def get_coffee_service() -> CoffeeService:
    result = CoffeeService()
    return result
