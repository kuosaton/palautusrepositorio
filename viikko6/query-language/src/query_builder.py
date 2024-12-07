from matchers import *


class QueryBuilder:
    def __init__(self, matchers=None):
        if matchers is None:
            self._matchers = []
        else:
            self._matchers = matchers

    def plays_in(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self

    def build(self):
        if not self._matchers:
            return All()
        return And(*self._matchers)
