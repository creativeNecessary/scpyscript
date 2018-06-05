# -*- coding: UTF-8 -*-
import pymysql
from CitizenWikiRobot.StaticField import StaticField
from CitizenWikiRobot.Vehicle import Vehicle
from CitizenWikiRobot.Equipment import ShipEquipment, Manufacturer
from CitizenWikiRobot.Log import Log
from CitizenWikiRobot.ProjectConfig import ProjectConfig
from CitizenWikiRobot.comm_link import CommLink, CommLinkContent

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MysqlHelper:

    def __init__(self):
        self.database = pymysql.connect(host='localhost', user=ProjectConfig.user, passwd=ProjectConfig.passwd,
                                        db=ProjectConfig.db, charset=ProjectConfig.charset)

    @staticmethod
    def handle_opt_data(data):
        if data is None:
            return ''
        else:
            return str(data)

    def __select_manufacture(self, manufacturer):
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

    def __select_vehicle(self, vehicle):
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

    def __insert_manufacture2mysql(self, manufacturer):
        cursor = self.database.cursor()
        have_data = self.__select_manufacture(manufacturer)
        if have_data:
            Log.d('UPDATE公司 ' + manufacturer.name)
            update_sql = 'UPDATE manufacturer_en SET code = %s , name = %s ,known_for = %s , description = %s , source_url = %s   WHERE id = %s'
            cursor.execute(update_sql,
                           (self.handle_opt_data(manufacturer.code),
                            self.handle_opt_data(manufacturer.name),
                            self.handle_opt_data(manufacturer.known_for),
                            self.handle_opt_data(manufacturer.description),
                            self.handle_opt_data(manufacturer.source_url),
                            int(self.handle_opt_data(manufacturer.id)))
                           )
            self.database.commit()

        else:
            Log.d('insert公司 ' + manufacturer.name)
            sql = 'INSERT INTO manufacturer_en (id,code,name,known_for,description,source_url) VALUES (%s,%s,%s,%s,%s,%s)'
            cursor.execute(sql, (
                int(self.handle_opt_data(manufacturer.id)),
                self.handle_opt_data(manufacturer.code),
                self.handle_opt_data(manufacturer.name),
                self.handle_opt_data(manufacturer.known_for),
                self.handle_opt_data(manufacturer.description),
                self.handle_opt_data(manufacturer.source_url)
            ))
            self.database.commit()
        cursor.close()

    def __insert_vehicle2mysql(self, vehicle):
        cursor = self.database.cursor()
        have_data = self.__select_vehicle(vehicle)
        if have_data:
            Log.d('Update Ship' + vehicle.name)
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
                int(self.handle_opt_data(vehicle.id))

            ))

            self.database.commit()

        else:
            Log.d('Insert Ship' + vehicle.name)
            sql = Vehicle.get_insert_sql()
            rows = cursor.execute(sql, (
                int(self.handle_opt_data(vehicle.id)),
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
            vehicle.id = cursor.lastrowid
        cursor.close()
        # 给所有的设备赋值飞船id

    def __insert_ship_equipment(self, ship_equipment):
        # 还是先查询 更新 插入
        cursor = self.database.cursor()
        Log.d("插入装备 " + ship_equipment.type)
        cursor.execute(ShipEquipment.get_insert_sql(), (self.handle_opt_data(ship_equipment.type),
                                                        self.handle_opt_data(ship_equipment.name),
                                                        self.handle_opt_data(ship_equipment.mounts),
                                                        self.handle_opt_data(ship_equipment.component_size),
                                                        self.handle_opt_data(ship_equipment.size),
                                                        self.handle_opt_data(ship_equipment.details),
                                                        self.handle_opt_data(ship_equipment.quantity),
                                                        self.handle_opt_data(ship_equipment.manufacturer),
                                                        self.handle_opt_data(ship_equipment.component_class),
                                                        int(self.handle_opt_data(ship_equipment.ship_id))
                                                        ))

        self.database.commit()
        cursor.close()

    def __insert_img(self, vehicle):
        # 直接插入新的
        cursor = self.database.cursor()
        # 先删除旧的
        delete_sql = "DELETE FROM ship_url WHERE ship_id = %s"
        cursor.execute(delete_sql, vehicle.id)
        self.database.commit()

        for img_url in vehicle.img_urls:
            sql = "INSERT INTO ship_url (url , type ,ship_id ) VALUE (%s , %s ,%s)"
            cursor.execute(sql, (img_url, 'image', vehicle.id))
            self.database.commit()
        cursor.close()

    def insert_vehicle(self, vehicle):
        # 更新载具
        self.__insert_vehicle2mysql(vehicle)
        # 更新载具url
        self.__insert_img(vehicle)
        # 更新载具类型
        self.__insert_ship_type(vehicle)
        # 更新载具装备
        # 先删除旧的装备
        cursor = self.database.cursor()
        delete_sql = "DELETE FROM ship_equipment_en WHERE ship_id = %s "
        cursor.execute(delete_sql, vehicle.id)
        Log.d("id : " + str(vehicle.id))
        Log.d("删除了 : " + str(cursor.rowcount))
        self.database.commit()
        cursor.close()

        for equip in vehicle.ship_equipment_list:
            self.__insert_ship_equipment(equip)

    def insert_manufacturer(self, manufacturer_list):
        for manufacturer in manufacturer_list:
            self.__insert_manufacture2mysql(manufacturer)

    def __insert_ship_type(self, vehicle):
        cursor = self.database.cursor()
        # 先删除旧的
        delete_sql = "DELETE FROM ship_type WHERE ship_id = %s"
        cursor.execute(delete_sql, vehicle.id)
        self.database.commit()

        ship_types = []
        focus = vehicle.focus
        keys_data = StaticField.SHIP_TYPE_MAP.keys()
        if focus is None:
            return
        data = focus.split("/")
        for ship_type in data:
            ship_type = ship_type.strip()
            if 'Gun Ship' in ship_type:
                ship_types.append('Gunship')
            for key_type in keys_data:
                if key_type in ship_type:
                    ship_types.append(key_type)
        for type_content in ship_types:
            insert_sql = "INSERT INTO ship_type (ship_id , type_content ) VALUE (%s , %s )"
            cursor.execute(insert_sql, (vehicle.id, type_content))
        cursor.close()
        self.database.commit()

    def insert_comm_link(self, comm_link):
        cursor = self.database.cursor()
        # query
        select_sql = "SELECT id FROM comm_link WHERE url = %s "
        cursor.execute(select_sql, comm_link.url)
        if cursor.rowcount > 0:
            Log.d("update comm_link ")
            Log.d(comm_link.title)
            # 有数据 update
            data = cursor.fetchone()
            m_id = data[0]
            comm_link.id = m_id
            update_sql = 'UPDATE comm_link SET url = %s , background = %s ,title = %s , type = %s  WHERE id = %s'
            cursor.execute(update_sql, (comm_link.url, comm_link.background, comm_link.title, comm_link.type, m_id))

        else:
            # 无数据 insert
            Log.d("insert comm_link ")
            Log.d(comm_link.title)
            insert_sql = "INSERT INTO comm_link (url , background , title , type) VALUE (%s , %s , %s, %s)"
            cursor.execute(insert_sql, (comm_link.url, comm_link.background, comm_link.title, comm_link.type))

            comm_link.id = cursor.lastrowid

        self.database.commit()
        cursor.close()
        self.__insert_comm_link_content(comm_link)

    def __insert_comm_link_content(self, comm_link):
        cursor = self.database.cursor()
        select_sql = "SELECT id FROM comm_link_content WHERE comm_link_id = %s "
        cursor.execute(select_sql, comm_link.id)
        count = cursor.rowcount
        if count != len(comm_link.content):
            Log.d("链接内容与数据库不符合 删除重新插入! ")
            # 删除旧的
            delete_sql = "DELETE FROM comm_link_content WHERE comm_link_id = %s"
            cursor.execute(delete_sql, comm_link.id)
        for content in comm_link.content:
            select_item = "SELECT id FROM comm_link_content WHERE comm_link_id = %s AND data_index = %s"
            cursor.execute(select_item, (comm_link.id, content.data_index))
            if cursor.rowcount <= 0:
                Log.d("未查询到链接内容 插入--")
                insert_item_sql = "INSERT INTO comm_link_content (data_index , comm_link_id , content_type , content_data , machine_translate_data , human_translate_data) VALUE (%s , %s , %s, %s, %s, %s )"
                cursor.execute(insert_item_sql, (
                    content.data_index, comm_link.id, content.content_type, content.content_data,
                    content.machine_translate_data, content.human_translate_data))

            else:
                Log.d("查询到链接内容 更新--")
                update_item_sql = "UPDATE comm_link_content SET content_type = %s , content_data = %s ,machine_translate_data = %s , human_translate_data = %s  WHERE comm_link_id = %s AND data_index = %s"
                cursor.execute(update_item_sql, (content.content_type, content.content_data,
                                                 content.machine_translate_data, content.human_translate_data,
                                                 comm_link.id, content.data_index))
            self.database.commit()
        cursor.close()

    def insert_constant_translate(self):
        cursor = self.database.cursor()
        clear_constant_translate = ' TRUNCATE  TABLE  constant_translate '
        cursor.execute(clear_constant_translate)
        self.database.commit()

        for key in StaticField.SHIP_NAME_MAP.keys():
            sql = "INSERT INTO constant_translate (original_text , translate_value) VALUE (%s , %s)"
            cursor.execute(sql, (key, StaticField.SHIP_NAME_MAP[key]))
            self.database.commit()

        for key in StaticField.COMPANY_MAP.keys():
            sql = "INSERT INTO constant_translate (original_text , translate_value) VALUE (%s , %s)"
            cursor.execute(sql, (key, StaticField.COMPANY_MAP[key]))
            self.database.commit()

        for key in StaticField.CONSTANT_GROUP.keys():
            sql = "INSERT INTO constant_translate (original_text , translate_value) VALUE (%s , %s)"
            cursor.execute(sql, (key, StaticField.CONSTANT_GROUP[key]))
            self.database.commit()

    def insert_all_ship_type(self):
        cursor = self.database.cursor()
        clear_constant_translate = ' TRUNCATE  TABLE  ship_type_constant '
        cursor.execute(clear_constant_translate)
        self.database.commit()

        for key in StaticField.SHIP_TYPE_MAP.keys():
            sql = "INSERT INTO ship_type_constant (type_en , type_ch) VALUE (%s , %s)"
            cursor.execute(sql, (key, StaticField.SHIP_TYPE_MAP[key]))
            self.database.commit()
