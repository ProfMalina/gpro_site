from sqlalchemy.ext.declarative import declarative_base
import json
from sqlalchemy import Column, Integer, String, update
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

Base = declarative_base()


class Drivers(Base):
    """
    Класс описывающий объект пилота. Так же, осуществляется взаимодействие с БД.
    Описание полей таблицы ниже.
    """
    __tablename__ = 'new_scandrivers'
    id_driver = Column(Integer, primary_key=True)  # id пилота
    name = Column(String)  # Имя
    nat = Column(String)  # национальность
    oa = Column(Integer)  # уровень
    con = Column(Integer)  # концентрация
    tal = Column(Integer)  # талант
    exp = Column(Integer)  # опыт
    agg = Column(Integer)  # агрессивность
    tei = Column(Integer)  # ТЗ
    sta = Column(Integer)  # выносливость
    cha = Column(Integer)  # харизма
    mot = Column(Integer)  # мотивация
    rep = Column(Integer)  # репутация
    age = Column(Integer)  # возраст
    wei = Column(Integer)  # вес
    ret = Column(Integer)  # карьера
    sal = Column(Integer)  # зарплата
    fee = Column(Integer)  # премия
    fav = Column(String)  # любимая трасса
    off = Column(Integer)  # предложения
    date = Column(String)  # время добавления

    def __init__(self, id_driver, name, nat, oa, con, tal, exp, agg, tei, sta, cha, mot, rep, age, wei, ret, sal, fee, fav,
                 off, date):
        self.id_driver = id_driver
        self.name = name
        self.nat = nat
        self.oa = oa
        self.con = con
        self.tal = tal
        self.exp = exp
        self.agg = agg
        self.tei = tei
        self.sta = sta
        self.cha = cha
        self.mot = mot
        self.rep = rep
        self.age = age
        self.wei = wei
        self.ret = ret
        self.sal = sal
        self.fee = fee
        self.fav = fav
        self.off = off
        self.date = date

    def _keys(self):
        return (self.id_driver, self.name, self.nat, self.oa, self.con, self.tal, self.exp, self.agg, self.tei,
                self.sta, self.cha, self.mot, self.rep, self.age, self.wei, self.ret, self.sal, self.fee, self.fav,
                self.off, self.date)

    def __eq__(self, other):
        return self._keys() == other._keys()

    def __hash__(self):
        return hash(self._keys())

    def __repr__(self):
        return "<Drivers(id_driver='{}', name='{}', nat='{}', oa={}, con={}, " \
               "tal={}, exp={}, agg={}, tei={}, sta={}, cha={}, mot={}, rep={}, age={}, wei={}, " \
               "ret={}, sal={}, fee={}, fav='{}', off={}, date={})>" .format(
                                                                        self.id_driver,
                                                                        self.name,
                                                                        self.nat,
                                                                        self.oa,
                                                                        self.con,
                                                                        self.tal,
                                                                        self.exp,
                                                                        self.agg,
                                                                        self.tei,
                                                                        self.sta,
                                                                        self.cha,
                                                                        self.mot,
                                                                        self.rep,
                                                                        self.age,
                                                                        self.wei,
                                                                        self.ret,
                                                                        self.sal,
                                                                        self.fee,
                                                                        self.fav,
                                                                        self.off,
                                                                        self.date)


class Database:
    """
    Класс для обработки сессии SQLAlchemy.
    Так же включает в себя минимальный набор методов, вызываемых в управляющем классе.
    Названия методов говорящие.
    """

    def __init__(self, obj):
        engine = create_engine(obj, echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.drivers = []

    def get_drivers(self, drv):
        # date = int(time.mktime(time.localtime()))
        d = json.load(open(drv))
        date = d['Last updated']
        self.drivers += [Drivers(i['ID'], i['NAME'], i['NAT'], i['OA'], i['CON'], i['TAL'], i['EXP'], i['AGG'],
                                i['TEI'], i['STA'], i['CHA'], i['MOT'], i['REP'], i['AGE'], i['WEI'], i['RET'],
                                i['SAL'], i['FEE'], str(i['FAV']), i['OFF'], date) for i in d['drivers']]
        return self.drivers

    def add_driver(self, driver):
        self.session.add(driver)
        self.session.commit()

    def update_driver(self, drv):
        # d = json.load(open(drv))
        # date = int(time.mktime(time.localtime()))
        # date = d['Last updated']
        self.session.query(Drivers).filter_by(id_driver=drv.id_driver).update({
                                                                "id_driver": drv.id_driver, "name": drv.name,
                                                                "nat": drv.nat, "oa": drv.oa, "con": drv.con,
                                                                "tal": drv.tal, "exp": drv.exp, "agg": drv.agg,
                                                                "tei": drv.tei, "sta": drv.sta, "cha": drv.cha,
                                                                "mot": drv.mot, "rep": drv.rep, "age": drv.age,
                                                                "wei": drv.wei, "ret": drv.ret, "sal": drv.sal,
                                                                "fee": drv.fee, "fav": drv.fav, "off": drv.off,
                                                                "date": drv.date})
        self.session.commit()

    def find_driver(self, drv_id):
        if self.session.query(Drivers).filter_by(id_driver=drv_id).first():
            return self.session.query(Drivers).filter_by(id_driver=drv_id).first()
        else:
            return False

    def find_all_drivers(self):
        return self.session.query(Drivers).all()
