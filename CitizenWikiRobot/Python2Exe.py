# # #!/usr/bin/env python
# # # -*- coding: utf-8 -*-
# # from PyInstaller.__main__ import run
# #
# #
# # if __name__ == '__main__':
# #     opts = ['-F', 'ship_robot.py']
# #     # opts = ['ship_robot.py', '-F', '-w']
# #     # opts = ['ship_robot.py', '-F', '-w', '--icon=TargetOpinionMain.ico','--upx-dir','upx391w']
# #     run(opts)
#
# # CREATE DATABASE StarCitizen
#
# CREATE TABLE ship_en (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# name VARCHAR(50) NOT NULL DEFAULT '',
# url VARCHAR(3000) NOT NULL DEFAULT '',
# description VARCHAR(3000) NOT NULL DEFAULT '',
# json_str INT  NOT NULL DEFAULT -1,
# icon VARCHAR(3000) NOT NULL DEFAULT '',
# pic_url VARCHAR(2000) NOT NULL DEFAULT '',
# manufacturer_id VARCHAR(10) NOT NULL DEFAULT '',
# size VARCHAR(10) NOT NULL DEFAULT '',
# focus VARCHAR(50) NOT NULL DEFAULT '',
# production_state VARCHAR(50) NOT NULL DEFAULT '',
#
# max_crew VARCHAR(10) NOT NULL DEFAULT '',
# min_crew VARCHAR(10) NOT NULL DEFAULT '',
# pitch_max VARCHAR(15) NOT NULL DEFAULT '',
# yaw_max VARCHAR(15) NOT NULL DEFAULT '',
# roll_max VARCHAR(15) NOT NULL DEFAULT '',
# x_axis_acceleration VARCHAR(15) NOT NULL DEFAULT '',
# y_axis_acceleration VARCHAR(15) NOT NULL DEFAULT '',
# z_axis_acceleration VARCHAR(15) NOT NULL DEFAULT '',
#
# cargo_capacity VARCHAR(15) NOT NULL DEFAULT '',
# rec_cost VARCHAR(10) NOT NULL DEFAULT '',
# pledge_cost VARCHAR(10) NOT NULL DEFAULT '',
# mass VARCHAR(15) NOT NULL DEFAULT '',
# scm_speed VARCHAR(15) NOT NULL DEFAULT '',
# afterburner_speed VARCHAR(15) NOT NULL DEFAULT '',
# length VARCHAR(10) NOT NULL DEFAULT '',
# beam VARCHAR(10) NOT NULL DEFAULT '',
# height VARCHAR(10) NOT NULL DEFAULT '',
#
# avionics VARCHAR(2000) NOT NULL DEFAULT '',
# modular VARCHAR(2000)  NOT NULL DEFAULT '',
# propulsion VARCHAR(2000)  NOT NULL DEFAULT '',
# thrusters VARCHAR(2000)  NOT NULL DEFAULT '',
# weapons VARCHAR(2000)  NOT NULL DEFAULT '',
#
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
# #
# #
# CREATE TABLE field_ch (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# original VARCHAR(100) NOT NULL DEFAULT '',
# content VARCHAR(100) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
#
# # Manufacturer = "Manufacturer"
# # Size = "Size"
# # Focus = "Focus"
# # Production_State = "Production State"
# # Maximum_Crew = "Maximum Crew"
# # Cargo_Capacity = "Cargo Capacity"
# # REC_Cost = "REC Cost"
# # Pledge_Cost = "Pledge Cost"
# # Null_cargo_Mass = "Null-cargo Mass"
# # SCM_Speed = "SCM Speed"
# # Afterburner_Speed = "Afterburner Speed"
# # Length = "Length"
# # Beam = "Beam"
# # Height = "Height"
# #
# #
# # INSERT INTO field_original (original) VALUE ('Manufacturer')
# #
# # INSERT INTO field_original (original) VALUE ('Size')
# # INSERT INTO field_original (original) VALUE ('Focus')
# # INSERT INTO field_original (original) VALUE ('Production State')
# # INSERT INTO field_original (original) VALUE ('Maximum Crew')
# # INSERT INTO field_original (original) VALUE ('Cargo Capacity')
# # INSERT INTO field_original (original) VALUE ('REC Cost')
# # INSERT INTO field_original (original) VALUE ('Pledge Cost')
# # INSERT INTO field_original (original) VALUE ('Null-cargo Mass')
# # INSERT INTO field_original (original) VALUE ('SCM Speed')
# # INSERT INTO field_original (original) VALUE ('Afterburner Speed')
# # INSERT INTO field_original (original) VALUE ('Length')
# # INSERT INTO field_original (original) VALUE ('Beam')
# # INSERT INTO field_original (original) VALUE ('Height')
# #
# # INSERT INTO field_original (original) VALUE ('Radar')
# # INSERT INTO field_original (original) VALUE ('Computers')
# # INSERT INTO field_original (original) VALUE ('Power Plants')
# # INSERT INTO field_original (original) VALUE ('Coolers')
# # INSERT INTO field_original (original) VALUE ('Shield Generators')
# # INSERT INTO field_original (original) VALUE ('Fuel Intakes')
# # INSERT INTO field_original (original) VALUE ('Fuel Tanks')
# # INSERT INTO field_original (original) VALUE ('Quantum Drives')
# # INSERT INTO field_original (original) VALUE ('Jump Modules')
# # INSERT INTO field_original (original) VALUE ('Quantum Fuel Tanks')
# # INSERT INTO field_original (original) VALUE ('Main Thrusters')
# # INSERT INTO field_original (original) VALUE ('Maneuvering Thrusters')
# # INSERT INTO field_original (original) VALUE ('Weapons')
# # INSERT INTO field_original (original) VALUE ('Turrets')
# # INSERT INTO field_original (original) VALUE ('Missiles')
# # INSERT INTO field_original (original) VALUE ('Utility Items')
# #
# # INSERT INTO field_original (original) VALUE ('Avionics')
# # INSERT INTO field_original (original) VALUE ('Systems')
# # INSERT INTO field_original (original) VALUE ('Propulsion')
# # INSERT INTO field_original (original) VALUE ('Thrusters')
# # INSERT INTO field_original (original) VALUE ('Weaponry')
# #
# #
# CREATE TABLE ship_equipment_en (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# type VARCHAR(40) NOT NULL DEFAULT '',
# size VARCHAR(20) NOT NULL DEFAULT '',
# quantity VARCHAR(10) NOT NULL DEFAULT '',
# details VARCHAR(500) NOT NULL DEFAULT '',
# tag VARCHAR(40) NOT NULL DEFAULT '',
# equipment_id INT NOT NULL DEFAULT -1,
# ship_id INT NOT NULL DEFAULT -1,
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
# #
# CREATE TABLE equipment_en (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# type VARCHAR(40) NOT NULL DEFAULT '',
# size VARCHAR(20) NOT NULL DEFAULT '',
# name VARCHAR(40) NOT NULL DEFAULT '',
# manufacturer_id VARCHAR(10) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
#
# CREATE TABLE manufacturer_en (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# name VARCHAR(100) NOT NULL DEFAULT '',
# code VARCHAR(100) NOT NULL DEFAULT '',
# known_for VARCHAR(100) NOT NULL DEFAULT '',
# description VARCHAR(5000) NOT NULL DEFAULT '',
# icon VARCHAR(3000) NOT NULL DEFAULT '',
# url VARCHAR(3000) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
#
#
#
# CREATE TABLE ship_json (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# json_data TEXT NOT NULL ,
# ship_id INT NOT NULL DEFAULT -1,
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
#
# #
# # 英文原文数据库
# CREATE TABLE field_original (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# original VARCHAR(100) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
# #
# # 中文数据库
# CREATE TABLE field_ch (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# original VARCHAR(100) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
#
#
# # url 数据库
# CREATE TABLE ship_url (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# url VARCHAR(4000) NOT NULL DEFAULT '',
# type VARCHAR(20) NOT NULL DEFAULT '',
# ship_id VARCHAR(10) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

# alter table ship_en add column model3d_url VARCHAR(3000) NOT NULL DEFAULT '';

# alter table ship_en change manufacturer_id manufacturer VARCHAR(10) NOT NULL DEFAULT '';

# alter table ship_equipment_en change equipment_id equipment INT NOT NULL DEFAULT -1;

# CREATE TABLE sc_translate (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# type VARCHAR(100) NOT NULL DEFAULT '',
# belong_to VARCHAR(100) NOT NULL DEFAULT '',
# tag VARCHAR(100) NOT NULL DEFAULT '',
# translate_value VARCHAR(100) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

# CREATE TABLE table_update_info (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# table_name VARCHAR(100) NOT NULL DEFAULT '',
# operate VARCHAR(100) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

# insert into table_update_info (table_name,operate) values ('sc_translate','create');
# 触发器
# delimiter //
# create trigger sc_translate_after_insert after insert on sc_translate for each row
# begin
# update table_update_info set operate = 'insert' where table_name = 'sc_translate';
# end;


# create trigger sc_translate_after_delete after delete on sc_translate for each row
# begin
# update table_update_info set operate = 'delete' where table_name = 'sc_translate';
# end;


# create trigger sc_translate_after_update after update on sc_translate for each row
# begin
# update table_update_info set operate = 'update' where table_name = 'sc_translate';
# end;

# alter table sc_translate add column original_text  VARCHAR(3000) NOT NULL DEFAULT '' after tag;
#
# alter  table sc_translate modify  column translate_value  VARCHAR(3000) NOT NULL DEFAULT '';

# CREATE TABLE constant_translate (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# original_text VARCHAR(3000) NOT NULL DEFAULT '',
# translate_value VARCHAR(3000) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));


# SHOW CREATE TABLE constant_translate;
# ALTER TABLE constant_translate DEFAULT CHARACTER SET utf8;
# ALTER TABLE sc_translate DEFAULT CHARACTER SET utf8;
#
# ALTER TABLE constant_translate CHANGE translate_value translate_value VARCHAR(3000) CHARACTER SET utf8;
# ALTER TABLE sc_translate CHANGE translate_value translate_value VARCHAR(3000) CHARACTER SET utf8;
# alter  table constant_translate modify  column translate_value  VARCHAR(3000) NOT NULL DEFAULT '';
# alter  table sc_translate modify  column translate_value  VARCHAR(3000) NOT NULL DEFAULT '';
