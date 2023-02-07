from typing_extensions import Any


def json_response(data: Any = None, status: str = "ok"):
    if data is None:
        data = {}

    return {
        "status": status,
        "data": data,
    }
