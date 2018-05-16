# -*- coding: UTF-8 -*-
from CitizenWikiRobot.Log import Log
from CitizenWikiRobot.Equipment import Manufacturer, ShipEquipment


class Vehicle:
    EQUIPMENT_AVIONICS = 1
    EQUIPMENT_MODULAR = 2
    EQUIPMENT_PROPULSION = 3
    EQUIPMENT_THRUSTERS = 4
    EQUIPMENT_WEAPONS = 5

    def __init__(self, url):
        self.data_json = None
        self.id = ""
        self.production_status = ""
        self.production_note = ""
        self.length = ""
        self.beam = ""
        self.height = ""
        self.size = ""
        self.mass = ""
        self.type = ""
        self.cargocapacity = ""
        self.min_crew = ""
        self.max_crew = ""
        self.scm_speed = ""
        self.afterburner_speed = ""
        self.pitch_max = ""
        self.yaw_max = ""
        self.roll_max = ""
        self.x_axis_acceleration = ""
        self.y_axis_acceleration = ""
        self.z_axis_acceleration = ""
        self.manufacturer_code = ""
        self.chassis_id = ""
        self.time_modified = ""
        self.name = ""
        self.focus = ""
        self.description = ""
        self.url = url
        self.store_large = ""
        self.image = []
        self.ship_equipment_list = []

    # def get_fields_data(self, data_key):
    #     data = self.fields.get(data_key)
    #     if data is None:
    #         return ""
    #     else:
    #         return data

    def init_ship_equipments(self, rsi_name, equipment_type):
        compiled = self.data_json.get('compiled')
        rsi_json = compiled.get(rsi_name)
        equipment_list_json = rsi_json.get(equipment_type)
        for equipment_json in equipment_list_json:
            ship_equipment = ShipEquipment()
            ship_equipment.type = equipment_json.get('type')
            ship_equipment.name = equipment_json.get('name')
            ship_equipment.mounts = equipment_json.get('mounts')
            ship_equipment.component_size = equipment_json.get('component_size')
            ship_equipment.size = equipment_json.get('size')
            ship_equipment.details = equipment_json.get('details')
            ship_equipment.quantity = equipment_json.get('quantity')
            ship_equipment.manufacturer = equipment_json.get('manufacturer')
            ship_equipment.component_class = equipment_json.get('component_class')
            ship_equipment.ship_id = self.id

            self.ship_equipment_list.append(ship_equipment)

    def init_with_data_json(self):
        self.id = self.data_json.get('id')
        self.production_status = self.data_json.get('production_status')
        self.production_note = self.data_json.get('production_note')
        self.length = self.data_json.get('length')
        self.beam = self.data_json.get('beam')
        self.height = self.data_json.get('height')
        self.size = self.data_json.get('size')
        self.mass = self.data_json.get('mass')
        self.type = self.data_json.get('type')
        self.cargocapacity = self.data_json.get('cargocapacity')
        self.min_crew = self.data_json.get('min_crew')
        self.max_crew = self.data_json.get('max_crew')
        self.scm_speed = self.data_json.get('scm_speed')
        self.afterburner_speed = self.data_json.get('afterburner_speed')
        self.pitch_max = self.data_json.get('pitch_max')
        self.yaw_max = self.data_json.get('yaw_max')
        self.roll_max = self.data_json.get('roll_max')
        self.x_axis_acceleration = self.data_json.get('x_axis_acceleration')
        self.y_axis_acceleration = self.data_json.get('y_axis_acceleration')
        self.z_axis_acceleration = self.data_json.get('z_axis_acceleration')
        self.chassis_id = self.data_json.get('chassis_id')
        self.time_modified = self.data_json.get('time_modified')
        self.name = self.data_json.get('name')
        self.focus = self.data_json.get('focus')
        self.description = self.data_json.get('description')
        self.store_large = self.data_json.get('store_large')

        Log.d('Loading Ship ' + self.name)

        manufacturer_json = self.data_json.get('manufacturer')
        manufacturer = Manufacturer()
        manufacturer.id = manufacturer_json.get('id')
        manufacturer.code = manufacturer_json.get('code')
        manufacturer.name = manufacturer_json.get('name')
        manufacturer.known_for = manufacturer_json.get('known_for')
        manufacturer.description = manufacturer_json.get('description')
        manufacturer.source_url = manufacturer_json.get('source_url')
        from CitizenWikiRobot.ship_robot import append_manufacturer
        append_manufacturer(manufacturer)
        self.manufacturer_code = manufacturer.code
        self.init_ship_equipments('RSIAvionic', 'radar')
        self.init_ship_equipments('RSIAvionic', 'computers')
        self.init_ship_equipments('RSIPropulsion', 'fuel_intakes')
        self.init_ship_equipments('RSIPropulsion', 'fuel_tanks')
        self.init_ship_equipments('RSIPropulsion', 'quantum_drives')
        self.init_ship_equipments('RSIPropulsion', 'jump_modules')
        self.init_ship_equipments('RSIPropulsion', 'quantum_fuel_tanks')
        self.init_ship_equipments('RSIThruster', 'main_thrusters')
        self.init_ship_equipments('RSIThruster', 'maneuvering_thrusters')
        self.init_ship_equipments('RSIModular', 'power_plants')
        self.init_ship_equipments('RSIModular', 'coolers')
        self.init_ship_equipments('RSIModular', 'shield_generators')
        self.init_ship_equipments('RSIWeapon', 'weapons')
        self.init_ship_equipments('RSIWeapon', 'turrets')
        self.init_ship_equipments('RSIWeapon', 'missiles')
        self.init_ship_equipments('RSIWeapon', 'utility_items')

    @staticmethod
    def get_update_sql():
        sql = 'UPDATE ship_en SET ' \
              'production_status = %s ' \
              + ', production_note = %s' \
              + ', length = %s' \
              + ', beam = %s' \
              + ', height = %s' \
              + ', size = %s' \
              + ', mass = %s' \
              + ', type = %s' \
              + ', cargocapacity = %s' \
              + ', min_crew = %s' \
              + ', max_crew = %s' \
              + ', scm_speed = %s' \
              + ', afterburner_speed = %s' \
              + ', pitch_max = %s' \
              + ', yaw_max = %s' \
              + ', roll_max = %s' \
              + ', x_axis_acceleration = %s' \
              + ', y_axis_acceleration = %s' \
              + ', z_axis_acceleration = %s' \
              + ', manufacturer_code = %s' \
              + ', chassis_id = %s' \
              + ', time_modified = %s' \
              + ', name = %s' \
              + ', focus = %s' \
              + ', description = %s' \
              + ', url = %s' \
              + ', store_large = %s' \
              + 'WHERE id = %s'

        return sql

    @staticmethod
    def get_insert_sql():

        sql = 'INSERT INTO ship_en ' \
              + '(' \
              + '  id = %s ' \
              + '  production_status = %s ' \
              + ', production_note = %s' \
              + ', length = %s' \
              + ', beam = %s' \
              + ', height = %s' \
              + ', size = %s' \
              + ', mass = %s' \
              + ', type = %s' \
              + ', cargocapacity = %s' \
              + ', min_crew = %s' \
              + ', max_crew = %s' \
              + ', scm_speed = %s' \
              + ', afterburner_speed = %s' \
              + ', pitch_max = %s' \
              + ', yaw_max = %s' \
              + ', roll_max = %s' \
              + ', x_axis_acceleration = %s' \
              + ', y_axis_acceleration = %s' \
              + ', z_axis_acceleration = %s' \
              + ', manufacturer_code = %s' \
              + ', chassis_id = %s' \
              + ', time_modified = %s' \
              + ', name = %s' \
              + ', focus = %s' \
              + ', description = %s' \
              + ', url = %s' \
              + ', store_large = %s' \
              + ') VALUE ('

        for time in range(0, 26):
            sql = sql + ' %s ,'
        sql = sql + '  %s )'

        return sql

    def set_id2ship_equipment(self):
        equipment_list = [self.avionics, self.modular, self.propulsion, self.thrusters, self.weapons]
        for equipments in equipment_list:
            for ship_equipment in equipments:
                ship_equipment.ship_id = self.id
