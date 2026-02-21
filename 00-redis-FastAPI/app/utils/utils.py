from datetime import datetime


def get_direction(last_three_hours, key: str):
    if last_three_hours[0][key] < last_three_hours[-1][key]:
        return "rising"
    elif last_three_hours[0][key] > last_three_hours[-1][key]:
        return "falling"
    return "flat"


def datetime_parser(dct):
    for k, v in dct.items():
        if isinstance(v, str) and v.endswith("+00:00"):
            try:
                dct[k] = datetime.fromisoformat(v)
            except Exception:
                pass
    return dct