# -*- coding: UTF-8 -*-
import pymysql
from CitizenWikiRobot.StaticField import StaticField
from CitizenWikiRobot.Vehicle import Vehicle
from CitizenWikiRobot.Equipment import ShipEquipment, Equipment, Manufacturer
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
            return ""
        else:
            return data

    def select_manufacture(self, manufacturer_data):
        manufacturer = manufacturer_data.manufacturer
        cursor = self.database.cursor()
        select_sql = "SELECT id FROM manufacturer_en WHERE name = %s"
        cursor.execute(select_sql, (self.handle_opt_data(manufacturer.name)))
        if cursor.rowcount > 0:
            data = cursor.fetchone()
            m_id = data[0]
            manufacturer.id = m_id
            manufacturer_data.manufacturer_id = m_id
        cursor.close()

    def select_ship_equipment(self, ship_equipment):
        cursor = self.database.cursor()
        select_sql = "SELECT id FROM ship_equipment_en WHERE tag = %s AND type = %s AND size = %s AND quantity = %s AND ship_id = %s"
        cursor.execute(select_sql, (self.handle_opt_data(ship_equipment.tag),
                                    self.handle_opt_data(ship_equipment.type),
                                    self.handle_opt_data(ship_equipment.size),
                                    self.handle_opt_data(ship_equipment.quantity),
                                    self.handle_opt_data(ship_equipment.ship_id),
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
                                    str(equipment.manufacturer_id)
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
        cursor.execute(select_sql, (self.handle_opt_data(vehicle.name)))
        if cursor.rowcount > 0:
            data = cursor.fetchone()
            m_id = data[0]
            vehicle.id = m_id
            Log.d("查询到了飞船ID ：" + str(vehicle.id))
        cursor.close()

    def insert_manufacture2mysql(self, manufacturer_data):
        manufacturer = manufacturer_data.manufacturer
        cursor = self.database.cursor()
        self.select_manufacture(manufacturer_data)
        if manufacturer.id != -1:
            update_sql = 'UPDATE manufacturer_en SET name = %s , icon = %s ,code = %s , known_for = %s , description = %s WHERE id = %s'
            cursor.execute(update_sql,
                           (self.handle_opt_data(manufacturer.name),
                            self.handle_opt_data(manufacturer.icon),
                            self.handle_opt_data(manufacturer.code),
                            self.handle_opt_data(manufacturer.known_for),
                            self.handle_opt_data(manufacturer.description),
                            manufacturer.id))
            self.database.commit()

        else:
            sql = 'INSERT INTO manufacturer_en (name,code,icon,known_for,description) VALUES (%s,%s,%s,%s,%s)'
            cursor.execute(sql, (self.handle_opt_data(manufacturer.name),
                                 self.handle_opt_data(manufacturer.icon),
                                 self.handle_opt_data(manufacturer.code),
                                 self.handle_opt_data(manufacturer.known_for),
                                 self.handle_opt_data(manufacturer.description)))
            self.database.commit()
            self.select_manufacture(manufacturer_data)
        cursor.close()

    def insert_vehicle2mysql(self, vehicle):
        cursor = self.database.cursor()
        self.select_vehicle(vehicle)
        if vehicle.id != -1:
            sql = Vehicle.get_update_sql()
            rows = cursor.execute(sql, (self.handle_opt_data(vehicle.name),
                                        self.handle_opt_data(vehicle.url),
                                        self.handle_opt_data(vehicle.model3d_url),
                                        vehicle.get_fields_data(StaticField.Description),
                                        self.handle_opt_data(vehicle.icon),
                                        str(vehicle.manufacturer_id),
                                        self.handle_opt_data(vehicle.size),
                                        vehicle.get_fields_data(StaticField.Focus),
                                        vehicle.get_fields_data(StaticField.Production_State),
                                        vehicle.get_fields_data(StaticField.Max_Crew),
                                        vehicle.get_fields_data(StaticField.Min_Crew),
                                        vehicle.get_fields_data(StaticField.Pitch_Max),
                                        vehicle.get_fields_data(StaticField.Yaw_Max),
                                        vehicle.get_fields_data(StaticField.Roll_Max),
                                        vehicle.get_fields_data(StaticField.X_Axis_Acceleration),
                                        vehicle.get_fields_data(StaticField.Y_Axis_Acceleration),
                                        vehicle.get_fields_data(StaticField.Z_Axis_Acceleration),
                                        vehicle.get_fields_data(StaticField.Cargo_Capacity),
                                        vehicle.get_fields_data(StaticField.Mass),
                                        vehicle.get_fields_data(StaticField.SCM_Speed),
                                        vehicle.get_fields_data(StaticField.Afterburner_Speed),
                                        vehicle.get_fields_data(StaticField.Length),
                                        vehicle.get_fields_data(StaticField.Beam),
                                        vehicle.get_fields_data(StaticField.Height),
                                        str(vehicle.id)
                                        ))
            self.database.commit()

        else:
            sql = Vehicle.get_insert_sql()
            rows = cursor.execute(sql, (
                self.handle_opt_data(vehicle.name),
                self.handle_opt_data(vehicle.url),
                self.handle_opt_data(vehicle.model3d_url),
                vehicle.get_fields_data(StaticField.Description),
                self.handle_opt_data(vehicle.icon),
                str(vehicle.manufacturer_id),
                self.handle_opt_data(vehicle.size),
                vehicle.get_fields_data(StaticField.Focus),
                vehicle.get_fields_data(StaticField.Production_State),
                vehicle.get_fields_data(StaticField.Max_Crew),
                vehicle.get_fields_data(StaticField.Min_Crew),
                vehicle.get_fields_data(StaticField.Pitch_Max),
                vehicle.get_fields_data(StaticField.Yaw_Max),
                vehicle.get_fields_data(StaticField.Roll_Max),
                vehicle.get_fields_data(StaticField.X_Axis_Acceleration),
                vehicle.get_fields_data(StaticField.Y_Axis_Acceleration),
                vehicle.get_fields_data(StaticField.Z_Axis_Acceleration),
                vehicle.get_fields_data(StaticField.Cargo_Capacity),
                vehicle.get_fields_data(StaticField.Mass),
                vehicle.get_fields_data(StaticField.SCM_Speed),
                vehicle.get_fields_data(StaticField.Afterburner_Speed),
                vehicle.get_fields_data(StaticField.Length),
                vehicle.get_fields_data(StaticField.Beam),
                vehicle.get_fields_data(StaticField.Height),
            ))
            self.database.commit()
            self.select_vehicle(vehicle)
        cursor.close()
        # 给所有的设备赋值飞船id

    def insert_ship_equipment(self, ship_equipment):
        # 还是先查询 更新 插入
        cursor = self.database.cursor()
        Log.d("插入舰船设备 舰船ID： " + str(ship_equipment.ship_id))
        cursor.execute(ShipEquipment.get_insert_sql(), (self.handle_opt_data(ship_equipment.type),
                                                        self.handle_opt_data(ship_equipment.size),
                                                        self.handle_opt_data(ship_equipment.quantity),
                                                        self.handle_opt_data(ship_equipment.details),
                                                        self.handle_opt_data(ship_equipment.tag),
                                                        self.handle_opt_data(ship_equipment.equipment_id),
                                                        self.handle_opt_data(ship_equipment.ship_id),
                                                        ))
        self.database.commit()
        self.select_ship_equipment(ship_equipment)
        cursor.close()

    def insert_equipment(self, equipment):
        cursor = self.database.cursor()
        insert_sql = Equipment.get_insert_sql()
        cursor.execute(insert_sql, (self.handle_opt_data(equipment.type),
                                    self.handle_opt_data(equipment.size),
                                    self.handle_opt_data(equipment.name),
                                    str(equipment.manufacturer_id)
                                    ))
        # 验证插入成功
        Log.d("插入具体设备sql " + insert_sql)
        self.select_equipment(equipment)

        cursor.close()

    def clear_img_ship_equipment(self):
        cursor = self.database.cursor()
        clear_img = ' TRUNCATE  TABLE  ship_url '
        cursor.execute(clear_img)
        clear_ship_equipment = 'TRUNCATE  TABLE ship_equipment_en'
        cursor.execute(clear_ship_equipment)
        clear_equipment = 'TRUNCATE  TABLE equipment_en'
        cursor.execute(clear_equipment)
        cursor.close()

    def insert_img(self, vehicle):
        # 直接插入新的
        cursor = self.database.cursor()
        for img_url in vehicle.img_urls:
            sql = "INSERT INTO ship_url (url , type ,ship_id ) VALUE (%s , %s ,%s)"
            cursor.execute(sql, (img_url, 'image', vehicle.id))
            self.database.commit()
        cursor.close()

    def select_vehicle_img(self, vehicle):
        # 先查询 图片的id
        cursor = self.database.cursor()
        select_img_sql = 'SELECT id FROM ship_url WHERE ship_id = %s AND type = %s'
        cursor.execute(select_img_sql, (vehicle.id, "image"))
        ids = cursor.fetchall()
        img_ids = ""
        for data in ids:
            img_ids = img_ids + str(data[0]) + ','
        img_ids = img_ids[0:len(img_ids) - 1]
        cursor.close()
        return img_ids
        # 插入装备

    def insert2mysql(self, vehicle):
        # 插入公司
        if vehicle.manufacturer is not None:
            self.insert_manufacture2mysql(vehicle)
        # 插入飞船载具 在此处 飞船获取到了数据库id
        self.insert_vehicle2mysql(vehicle)
        if vehicle.id != -1:
            vehicle.set_id2ship_equipment()
        # 插入url 数组数据库
        self.insert_img(vehicle)

        # image_ids = self.select_vehicle_img(vehicle)
        self.insert_equipment2mysql(vehicle.avionics)
        self.insert_equipment2mysql(vehicle.modular)
        self.insert_equipment2mysql(vehicle.propulsion)
        self.insert_equipment2mysql(vehicle.thrusters)
        self.insert_equipment2mysql(vehicle.weapons)
        # 更新飞船

        update_sql = 'UPDATE ship_en SET pic_url = %s ' \
                     ', avionics = %s ' \
                     ', modular = %s ' \
                     ', propulsion = %s ' \
                     ', thrusters = %s ' \
                     ', weapons = %s ' \
                     'WHERE id = %s'
        cursor = self.database.cursor()
        insert_id = str(vehicle.id)
        cursor.execute(update_sql, (
            insert_id, insert_id, insert_id, insert_id, insert_id, insert_id, insert_id))
        self.database.commit()
        cursor.close()

    def insert_equipment2mysql(self, equipment_list):
        # ids = ""
        for equip in equipment_list:
            if equip.equipment is not None:
                self.insert_equipment(equip.equipment)
                equip.equipment_id = equip.equipment.id
            self.insert_ship_equipment(equip)
            # ids = str(equip.id) + "," + ids
            # Log.d("equip.id" + str(equip.id))
        # return ids[0:len(ids) - 1]

    def close_db(self):
        self.database.close()

    def insert_constant_translate(self):
        for key in StaticField.CONSTANT_GROUP.keys():
            sql = "INSERT INTO constant_translate (original_text , translate_value) VALUE (%s , %s)"
            cursor = self.database.cursor()
            cursor.execute(sql, (key, StaticField.CONSTANT_GROUP[key]))
            self.database.commit()
        self.database.close()
