from typing import Protocol
from . import database


class ResourcesRepositoryInterface(Protocol):
    @staticmethod
    def get_data() -> list:
        ...


class ItemsRepositoryInterface(Protocol):
    @staticmethod
    def add_data(data: list) -> None:
        ...


class ResourcesRepositoryV1:
    __database = database.Database()

    def get_data(self) -> list:
        self.__database.cursor.execute("SELECT * FROM resources;")
        resources = self.__database.cursor.fetchall()
        return resources


class ItemsRepositoryV1:
    __database = database.Database()

    def add_data(self, data: tuple) -> None:
        self.__database.cursor.execute("SELECT link FROM items;")
        items = self.__database.cursor.fetchall()
        link = (data[1],)
        if link in items:
            print(f'Новость {data[2]} уже в базе данных')
            return
        self.__database.cursor.execute(
            f"INSERT INTO items(res_id,link,title,content,nd_date,s_date,not_date) VALUES{data} ")
        self.__database.connection.commit()
        print(f'Новость {data[2]}  была добавлена в базу данных!')
