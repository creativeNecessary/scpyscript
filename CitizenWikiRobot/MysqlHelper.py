# -*- coding: UTF-8 -*-
import pymysql
from CitizenWikiRobot.StaticField import StaticField
from CitizenWikiRobot.Vehicle import Vehicle
from CitizenWikiRobot.Equipment import ShipEquipment, Manufacturer
from CitizenWikiRobot.Log import Log
from CitizenWikiRobot.ProjectConfig import ProjectConfig

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MysqlHelper:

    def __init__(self):
        self.database = pymysql.connect(host='localhost', user=ProjectConfig.user, passwd=ProjectConfig.passwd,
                                        db=ProjectConfig.db, charset=ProjectConfig.charset)
        # 清除挂点数据与图片数据
        self.clear_img_ship_equipment()

    @staticmethod
    def handle_opt_data(data):
        if data is None:
            return ''
        else:
            return str(data)

    def select_manufacture(self, manufacturer):
        cursor = self.database.cursor()
        select_sql = "SELECT id FROM manufacturer_en WHERE name = %s"
        cursor.execute(select_sql, (self.handle_opt_data(manufacturer.name)))
        if cursor.rowcount > 0:
            data = cursor.fetchone()
            m_id = data[0]
            if not m_id == -1:
                return True

        cursor.close()
        return False

    def select_ship_equipment(self, ship_equipment):
        cursor = self.database.cursor()
        select_sql = "SELECT id FROM ship_equipment_en WHERE tag = %s AND type = %s AND size = %s AND quantity = %s AND ship_id = %s"
        cursor.execute(select_sql, (self.handle_opt_data(ship_equipment.tag),
                                    self.handle_opt_data(ship_equipment.type),
                                    self.handle_opt_data(ship_equipment.size),
                                    self.handle_opt_data(ship_equipment.quantity),
                                    self.handle_opt_data(ship_equipment.ship_id)
                                    ))
        if cursor.rowcount > 0:
            data = cursor.fetchone()
            m_id = data[0]
            ship_equipment.id = m_id
        cursor.close()

    def select_equipment(self, equipment):
        cursor = self.database.cursor()
        # 先不插入设备的公司
        # if equipment.manufacturer is not None:
        #     self.insert_manufacture2mysql(equipment)
        select_sql = ' SELECT id FROM equipment_en WHERE name = %s AND size = %s AND type = %s AND manufacturer_id = %s '
        cursor.execute(select_sql, (self.handle_opt_data(equipment.name),
                                    self.handle_opt_data(equipment.size),
                                    self.handle_opt_data(equipment.type),
                                    self.handle_opt_data(equipment.manufacturer_id)
                                    ))
        if cursor.rowcount > 0:
            data = cursor.fetchone()
            m_id = data[0]
            equipment.id = m_id
            Log.d("具体设备ID查询到:" + str(equipment.id))
        cursor.close()

    def select_vehicle(self, vehicle):
        cursor = self.database.cursor()
        select_sql = "SELECT id FROM ship_en WHERE name = %s"
        cursor.execute(select_sql, vehicle.name)
        if cursor.rowcount > 0:
            data = cursor.fetchone()
            m_id = data[0]
            if not m_id == -1:
                return True

        cursor.close()
        return False

    def insert_manufacture2mysql(self, manufacturer):
        cursor = self.database.cursor()
        have_data = self.select_manufacture(manufacturer)
        if have_data:
            update_sql = 'UPDATE manufacturer_en SET code = %s , name = %s ,known_for = %s , description = %s , source_url = %s  ,url = %s WHERE id = %s'
            cursor.execute(update_sql,
                           (self.handle_opt_data(manufacturer.code),
                            self.handle_opt_data(manufacturer.name),
                            self.handle_opt_data(manufacturer.known_for),
                            self.handle_opt_data(manufacturer.description),
                            self.handle_opt_data(manufacturer.source_url),
                            self.handle_opt_data(manufacturer.url),
                            self.handle_opt_data(manufacturer.id))
                           )
            self.database.commit()

        else:
            sql = 'INSERT INTO manufacturer_en (id,code,name,known_for,description,source_url,url) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (
                                 self.handle_opt_data(manufacturer.id),
                                 self.handle_opt_data(manufacturer.code),
                                 self.handle_opt_data(manufacturer.name),
                                 self.handle_opt_data(manufacturer.known_for),
                                 self.handle_opt_data(manufacturer.description),
                                 self.handle_opt_data(manufacturer.source_url),
                                 self.handle_opt_data(manufacturer.url)
                                 ))
            self.database.commit()
        cursor.close()

    def insert_vehicle2mysql(self, vehicle):
        cursor = self.database.cursor()
        have_data = self.select_vehicle(vehicle)
        if have_data:
            sql = Vehicle.get_update_sql()

            rows = cursor.execute(sql, (
                self.handle_opt_data(vehicle.production_status),
                self.handle_opt_data(vehicle.production_note),
                self.handle_opt_data(vehicle.length),
                self.handle_opt_data(vehicle.beam),
                self.handle_opt_data(vehicle.height),
                self.handle_opt_data(vehicle.size),
                self.handle_opt_data(vehicle.mass),
                self.handle_opt_data(vehicle.type),
                self.handle_opt_data(vehicle.cargocapacity),
                self.handle_opt_data(vehicle.min_crew),
                self.handle_opt_data(vehicle.max_crew),
                self.handle_opt_data(vehicle.scm_speed),
                self.handle_opt_data(vehicle.afterburner_speed),
                self.handle_opt_data(vehicle.pitch_max),
                self.handle_opt_data(vehicle.yaw_max),
                self.handle_opt_data(vehicle.roll_max),
                self.handle_opt_data(vehicle.x_axis_acceleration),
                self.handle_opt_data(vehicle.y_axis_acceleration),
                self.handle_opt_data(vehicle.z_axis_acceleration),
                self.handle_opt_data(vehicle.manufacturer_code),
                self.handle_opt_data(vehicle.chassis_id),
                self.handle_opt_data(vehicle.time_modified),
                self.handle_opt_data(vehicle.name),
                self.handle_opt_data(vehicle.focus),
                self.handle_opt_data(vehicle.description),
                self.handle_opt_data(vehicle.url),
                self.handle_opt_data(vehicle.store_large),
                self.handle_opt_data(vehicle.id)

            ))
            self.database.commit()

        else:
            sql = Vehicle.get_insert_sql()
            Log.d('Insert Ship')
            Log.d(sql)
            Log.d(type(vehicle.id))
            rows = cursor.execute(sql, (
                self.handle_opt_data(vehicle.id),
                self.handle_opt_data(vehicle.production_status),
                self.handle_opt_data(vehicle.production_note),
                self.handle_opt_data(vehicle.length),
                self.handle_opt_data(vehicle.beam),
                self.handle_opt_data(vehicle.height),
                self.handle_opt_data(vehicle.size),
                self.handle_opt_data(vehicle.mass),
                self.handle_opt_data(vehicle.type),
                self.handle_opt_data(vehicle.cargocapacity),
                self.handle_opt_data(vehicle.min_crew),
                self.handle_opt_data(vehicle.max_crew),
                self.handle_opt_data(vehicle.scm_speed),
                self.handle_opt_data(vehicle.afterburner_speed),
                self.handle_opt_data(vehicle.pitch_max),
                self.handle_opt_data(vehicle.yaw_max),
                self.handle_opt_data(vehicle.roll_max),
                self.handle_opt_data(vehicle.x_axis_acceleration),
                self.handle_opt_data(vehicle.y_axis_acceleration),
                self.handle_opt_data(vehicle.z_axis_acceleration),
                self.handle_opt_data(vehicle.manufacturer_code),
                self.handle_opt_data(vehicle.chassis_id),
                self.handle_opt_data(vehicle.time_modified),
                self.handle_opt_data(vehicle.name),
                self.handle_opt_data(vehicle.focus),
                self.handle_opt_data(vehicle.description),
                self.handle_opt_data(vehicle.url),
                self.handle_opt_data(vehicle.store_large)
            ))
            self.database.commit()
        cursor.close()
        # 给所有的设备赋值飞船id

    def insert_ship_equipment(self, ship_equipment):
        # 还是先查询 更新 插入
        cursor = self.database.cursor()

        cursor.execute(ShipEquipment.get_insert_sql(), (self.handle_opt_data(ship_equipment.type),
                                                        self.handle_opt_data(ship_equipment.name),
                                                        self.handle_opt_data(ship_equipment.mounts),
                                                        self.handle_opt_data(ship_equipment.component_size),
                                                        self.handle_opt_data(ship_equipment.size),
                                                        self.handle_opt_data(ship_equipment.details),
                                                        self.handle_opt_data(ship_equipment.quantity),
                                                        self.handle_opt_data(ship_equipment.manufacturer),
                                                        self.handle_opt_data(ship_equipment.component_class),
                                                        self.handle_opt_data(ship_equipment.ship_id)
                                                        ))

        self.database.commit()
        self.select_ship_equipment(ship_equipment)
        cursor.close()

    def clear_img_ship_equipment(self):
        cursor = self.database.cursor()
        clear_img = ' TRUNCATE  TABLE  ship_url '
        cursor.execute(clear_img)
        clear_ship_equipment = 'TRUNCATE  TABLE ship_equipment_en'
        cursor.execute(clear_ship_equipment)
        cursor.close()

    def insert_img(self, vehicle):
        # 直接插入新的
        cursor = self.database.cursor()
        for img_url in vehicle.img_urls:
            sql = "INSERT INTO ship_url (url , type ,ship_id ) VALUE (%s , %s ,%s)"
            cursor.execute(sql, (img_url, 'image', vehicle.id))
            self.database.commit()
        cursor.close()

    def insert2mysql(self, vehicle):
        Log.d('insertShip ' + vehicle.name)
        self.insert_vehicle2mysql(vehicle)
        self.insert_img(vehicle)
        for equip in vehicle.ship_equipment_list:
            self.insert_ship_equipment(equip)

    def insert_manufacturer(self, manufacturer_list):
        for manufacturer in manufacturer_list:
            Log.d('insert公司 '+manufacturer.name)
            self.insert_manufacture2mysql(manufacturer)

# def insert_constant_translate(self):
#     for key in StaticField.SHIP_NAME_MAP.keys():
#         sql = "INSERT INTO constant_translate (original_text , translate_value) VALUE (%s , %s)"
#         cursor = self.database.cursor()
#         cursor.execute(sql, (key, StaticField.SHIP_NAME_MAP[key]))
#         self.database.commit()
#
#     for key in StaticField.COMPANY_MAP.keys():
#         sql = "INSERT INTO constant_translate (original_text , translate_value) VALUE (%s , %s)"
#         cursor = self.database.cursor()
#         cursor.execute(sql, (key, StaticField.COMPANY_MAP[key]))
#         self.database.commit()
#
#     for key in StaticField.CONSTANT_GROUP.keys():
#         sql = "INSERT INTO constant_translate (original_text , translate_value) VALUE (%s , %s)"
#         cursor = self.database.cursor()
#         cursor.execute(sql, (key, StaticField.CONSTANT_GROUP[key]))
#         self.database.commit()
#
#     self.database.close()
