# -*- coding: UTF-8 -*-


class Equipment:
    # 具体装备
    def __init__(self):
        self.type = ""
        self.size = ""
        self.name = ""
        self.manufacturer = None
        self.manufacturer_id = -1
        self.id = -1

    @staticmethod
    def get_update_sql():
        sql = 'UPDATE equipment_en SET type = %s ' \
              + ', size = %s' \
              + ', name = %s' \
              + ', manufacturer_id = %s ' \
              + 'WHERE id = %s'

        return sql

    @staticmethod
    def get_insert_sql():
        sql = 'INSERT INTO equipment_en ' \
              + '(' \
              + 'type ,' \
              + 'size ,' \
              + 'name ,' \
              + 'manufacturer_id ' \
              + ') VALUE ('

        for time in range(0, 3):
            sql = sql + ' %s ,'
        sql = sql + '  %s )'

        return sql


class ShipEquipment:
    # 飞船挂点 里面包含一个装备
    def __init__(self):
        self.type = ""
        self.id = -1
        self.ship_id = -1
        self.size = ""
        self.quantity = ""
        self.details = ""
        self.belong_to = ""
        self.equipment = None
        self.equipment_id = -1
        self.tag = ""

    @staticmethod
    def get_update_sql():
        sql = 'UPDATE ship_equipment_en SET  ' \
              + '  type = %s' \
              + ', size = %s' \
              + ', quantity = %s' \
              + ', details = %s ' \
              + ', tag = %s ' \
              + ', equipment =%s ' \
              + ', ship_id = %s ' \
              + 'WHERE id = %s '
        return sql

    @staticmethod
    def get_insert_sql():
        sql = 'INSERT INTO ship_equipment_en ' \
              + '(' \
              + 'type ,' \
              + 'size ,' \
              + 'quantity ,' \
              + 'details ,' \
              + 'tag ,' \
              + 'equipment ,' \
              + 'ship_id ' \
              + ') VALUE ('

        for time in range(0, 6):
            sql = sql + ' %s ,'
        sql = sql + '  %s )'

        return sql


class Manufacturer:
    def __init__(self):
        self.id = -1
        self.code = ""
        self.name = ""
        self.known_for = ""
        self.description = ""
        self.icon = ""
        self.url = ""
