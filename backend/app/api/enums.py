from enum import Enum


class Tags(Enum):
    test = "test",
    user = "user"


class UserLevels(Enum):
    admin = "ADMIN",
    gym = "GYM",
    coach = "COACH",
    client = "CLIENT",
    guest = "GUEST"


class Gender(Enum):
    male = "Male",
    female = "Female",
    other = "Other"
