from datetime import date, timedelta
import requests


class Student:
    """A student class as base for method testing"""

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self._naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def email(self):
        fname = self._first_name.lower()
        lname = self._last_name.lower()
        return f"{fname}.{lname}@email.com"

    def alert_santa(self):
        self.naughty_list = True

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)

    def course_schedule(self):
        fname = self._first_name
        lname = self._last_name

        response = requests.get(
            f"http://company.com/course-schedule/{lname}/{fname}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"
