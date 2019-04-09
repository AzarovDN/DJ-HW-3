import datetime
import time


class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        year, month, day, *_ = time.strptime(value, "%Y-%m-%d")
        return datetime.date(year, month, day)

    def to_url(self, value):
        return value.__str__()