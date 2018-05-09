# -*- coding: UTF-8 -*-


class Vehicle:
    EQUIPMENT_AVIONICS = 1
    EQUIPMENT_MODULAR = 2
    EQUIPMENT_PROPULSION = 3
    EQUIPMENT_THRUSTERS = 4
    EQUIPMENT_WEAPONS = 5

    def __init__(self, url):
        self.id = -1
        self.size = ""
        self.name = ""
        self.url = url
        self.manufacturer = None
        self.manufacturer_id = -1
        self.avionics = []
        self.modular = []
        self.propulsion = []
        self.thrusters = []
        self.weapons = []
        self.img_urls = []
        self.fields = dict()
        self.icon = ""
        self.model3d_url = ""

    def get_fields_data(self, data_key):
        data = self.fields.get(data_key)
        if data is None:
            return ""
        else:
            return data

    @staticmethod
    def get_update_sql():
        sql = 'UPDATE ship_en SET name = %s '\
              + ', url = %s' \
              + ', model3d_url = %s' \
              + ', description = %s'\
              + ', icon = %s' \
              + ', manufacturer = %s'\
              + ', size = %s'\
              + ', focus = %s'\
              + ', production_state = %s'\
              + ', max_crew = %s'\
              + ', min_crew = %s'\
              + ', pitch_max = %s'\
              + ', yaw_max = %s'\
              + ', roll_max = %s'\
              + ', x_axis_acceleration = %s'\
              + ', y_axis_acceleration = %s'\
              + ', z_axis_acceleration = %s'\
              + ', cargo_capacity = %s'\
              + ', mass = %s'\
              + ', scm_speed = %s'\
              + ', afterburner_speed = %s'\
              + ', length = %s'\
              + ', beam = %s'\
              + ', height = %s '\
              + 'WHERE id = %s'

        return sql

    @staticmethod
    def get_insert_sql():

        sql = 'INSERT INTO ship_en ' \
              + '(' \
              + 'name ,' \
              + 'url ,' \
              + 'model3d_url ,' \
              + 'description ,' \
              + 'icon ,' \
              + 'manufacturer ,' \
              + 'size ,' \
              + 'focus ,' \
              + 'production_state ,' \
              + 'max_crew ,' \
              + 'min_crew ,' \
              + 'pitch_max ,' \
              + 'yaw_max ,' \
              + 'roll_max ,' \
              + 'x_axis_acceleration ,' \
              + 'y_axis_acceleration ,' \
              + 'z_axis_acceleration ,' \
              + 'cargo_capacity ,' \
              + 'mass ,' \
              + 'scm_speed ,' \
              + 'afterburner_speed ,' \
              + 'length ,' \
              + 'beam ,' \
              + 'height ' \
              + ') VALUE ('

        for time in range(0, 23):
            sql = sql + ' %s ,'
        sql = sql + '  %s )'

        return sql

    def set_id2ship_equipment(self):
        equipment_list = [self.avionics, self.modular, self.propulsion, self.thrusters, self.weapons]
        for equipments in equipment_list:
            for ship_equipment in equipments:
                ship_equipment.ship_id = self.id
