from django.test import TestCase
import user.models as usermodels


def test_usermodels_insert():
    usermodels.insert('마이콜', 'michol@gmail.com', '1234', 'male')


