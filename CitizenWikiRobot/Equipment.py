# -*- coding: UTF-8 -*-


class ShipEquipment:
    # 飞船挂点 里面包含一个装备
    def __init__(self):
        self.ship_id = ""
        self.type = ""
        self.name = ""
        self.mounts = ""
        self.component_size = ""
        self.size = ""
        self.details = ""
        self.quantity = ""
        self.manufacturer = ""
        self.component_class = ""

    @staticmethod
    def get_insert_sql():
        sql = 'INSERT INTO ship_equipment_en ' \
              + '(' \
              + 'type ,' \
              + 'name ,' \
              + 'mounts ,' \
              + 'component_size ,' \
              + 'size ,' \
              + 'details ,' \
              + 'quantity ,' \
              + 'manufacturer ,' \
              + 'component_class ,' \
              + 'ship_id ' \
              + ') VALUE ('

        for time in range(0, 8):
            sql = sql + ' %s ,'
        sql = sql + '  %s )'

        return sql


class Manufacturer:
    def __init__(self):
        self.id = ""
        self.code = ""
        self.name = ""
        self.known_for = ""
        self.description = ""
        self.source_url = ""
        self.url = ""
