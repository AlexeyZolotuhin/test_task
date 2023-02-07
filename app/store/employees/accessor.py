import datetime

from app.store.base_accessor import BaseAccessor
from app.employees.models import EmployeesList, Employee, ConditionsEnum


class EmployeeAccessor(BaseAccessor):
    NAME_COLLECTION: str = "employees"

    async def get_employee_by_email(self, email: str):
        res = await self.app.mongodb.find_one_by_param(
            name_param='email',
            value=email,
            name_collection=self.NAME_COLLECTION
        )

        return res

    async def get_list_employees(self, params: dict) -> EmployeesList:
        if isinstance(params.get('join_date', None), str):
            date_str = params.get('join_date')
            date = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
            date_next = date + datetime.timedelta(days=1)
            date_next_str = date_next.strftime('%Y-%m-%dT%H:%M:%S%z')
            params['join_date'] = {ConditionsEnum.GREATER_EQUAL.value: date_str,
                                   ConditionsEnum.LESS_EQUAL.value: date_next_str}

        res = await self.app.mongodb.find_many_by_params(
            name_collection=self.NAME_COLLECTION,
            params=params, )
        return EmployeesList.parse_obj({"employees": res})
