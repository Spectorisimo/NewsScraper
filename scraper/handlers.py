from typing import Protocol
import time
from . import services
from datetime import datetime

class ResourcesHandlerInterface(Protocol):
    @staticmethod
    def get_data() -> list:
        ...


class ItemsHandlerInterface(Protocol):
    @staticmethod
    def add_data(data: tuple) -> None:
        ...


class ResourcesHandlerV1:
    resources_services: services.ResourcesServicesInterface = services.ResourcesServicesV1()

    def get_data(self) -> list:
        resources = []
        for resource in self.resources_services.get_data():
            resources.append(
                {
                    'id': resource[0],
                    'resource_name': resource[1],
                    'resource_url': resource[2],
                    'top_tag': resource[3],
                    'bottom_tag': resource[4],
                    'title_cut': resource[5],
                    'date_cut': resource[6],
                }
            )
        return resources


class ItemsHandlerV1:
    items_services: services.ItemsServicesInterface = services.ItemsServicesV1()

    def add_data(self, *args) -> None:
        resource_id = args[0]
        link = args[1]
        title = (args[2].text).rstrip().lstrip()
        content = (''.join(args[4])).rstrip().lstrip()

        raw_datetime = datetime.fromisoformat(args[3]['datetime'])
        raw_currenty_datetime = datetime.now()

        nd_date = self.convert_to_unix_datetime(raw_datetime)
        s_date = self.convert_to_unix_datetime(raw_currenty_datetime)
        not_date = raw_datetime.strftime('%Y-%m-%d')

        data = resource_id,link,title,content,nd_date,s_date,not_date
        self.items_services.add_data(data)



    @staticmethod
    def convert_to_unix_datetime(raw_datetime: datetime) -> float:
        return time.mktime(raw_datetime.timetuple())
