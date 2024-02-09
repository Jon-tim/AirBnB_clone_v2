#!/usr/bin/python3
"""DB STORAGE"""
from sqlalchemy import create_engine


class DBStorage:
    """class db storage"""
    __engine: None
    __session: None

    def __init__(self):
        """instantiation"""
        self.__engine = create_engine(
            'mysql+mysqldb://root:pass@localhost/mydb', pool_pre_ping=True)
