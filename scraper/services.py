from . import repository
from typing import Protocol


class ResourcesServicesInterface(Protocol):

    @staticmethod
    def get_data() -> list:
        ...


class ItemsServicesInterface(Protocol):
    @staticmethod
    def add_data(data: tuple) -> None:
        ...


class ResourcesServicesV1:
    resources_repository: repository.ResourcesRepositoryInterface = repository.ResourcesRepositoryV1()

    def get_data(self) -> list:
        return self.resources_repository.get_data()


class ItemsServicesV1:
    items_repository: repository.ItemsRepositoryInterface = repository.ItemsRepositoryV1()

    def add_data(self, data: tuple) -> None:
        self.items_repository.add_data(data)
