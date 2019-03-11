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
# id INT NOT NULL DEFAULT -1,
# production_status VARCHAR(50) NOT NULL DEFAULT '',
# production_note VARCHAR(2000) NOT NULL DEFAULT '',
# length VARCHAR(10) NOT NULL DEFAULT '',
# beam VARCHAR(10) NOT NULL DEFAULT '',
# height VARCHAR(10) NOT NULL DEFAULT '',
# size VARCHAR(10) NOT NULL DEFAULT '',
# mass VARCHAR(15) NOT NULL DEFAULT '',
# type VARCHAR(100) NOT NULL DEFAULT '',
# cargocapacity VARCHAR(20) NOT NULL DEFAULT '',
# min_crew VARCHAR(10) NOT NULL DEFAULT '',
# max_crew VARCHAR(10) NOT NULL DEFAULT '',
# scm_speed VARCHAR(15) NOT NULL DEFAULT '',
# afterburner_speed VARCHAR(15) NOT NULL DEFAULT '',
# pitch_max VARCHAR(15) NOT NULL DEFAULT '',
# yaw_max VARCHAR(15) NOT NULL DEFAULT '',
# roll_max VARCHAR(15) NOT NULL DEFAULT '',
# x_axis_acceleration VARCHAR(15) NOT NULL DEFAULT '',
# y_axis_acceleration VARCHAR(15) NOT NULL DEFAULT '',
# z_axis_acceleration VARCHAR(15) NOT NULL DEFAULT '',
# manufacturer_code VARCHAR(300) NOT NULL DEFAULT '',
# chassis_id VARCHAR(15) NOT NULL DEFAULT '',
# time_modified VARCHAR(500) NOT NULL DEFAULT '',
# name VARCHAR(50) NOT NULL DEFAULT '',
# focus VARCHAR(50) NOT NULL DEFAULT '',
# description VARCHAR(3000) NOT NULL DEFAULT '',
# url VARCHAR(3000) NOT NULL DEFAULT '',
# store_large VARCHAR(3000) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

#
# CREATE TABLE ship_equipment_en (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# type VARCHAR(40) NOT NULL DEFAULT '',
# name VARCHAR(40) NOT NULL DEFAULT '',
# mounts VARCHAR(40) NOT NULL DEFAULT '',
# component_size VARCHAR(40) NOT NULL DEFAULT '',
# size VARCHAR(20) NOT NULL DEFAULT '',
# details VARCHAR(3000) NOT NULL DEFAULT '',
# quantity VARCHAR(40) NOT NULL DEFAULT '',
# manufacturer VARCHAR(100) NOT NULL DEFAULT '',
# component_class VARCHAR(100) NOT NULL DEFAULT '',
# ship_id INT NOT NULL DEFAULT -1,
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

#
# CREATE TABLE manufacturer_en (
# id INT NOT NULL DEFAULT -1,
# code VARCHAR(100) NOT NULL DEFAULT '',
# name VARCHAR(100) NOT NULL DEFAULT '',
# known_for VARCHAR(500) NOT NULL DEFAULT '',
# description VARCHAR(3000) NOT NULL DEFAULT '',
# source_url VARCHAR(3000) NOT NULL DEFAULT '',
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

# CREATE TABLE app_version (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# version_code VARCHAR(500) NOT NULL DEFAULT '',
# version_name VARCHAR(500) NOT NULL DEFAULT '',
# version_focus VARCHAR(500) NOT NULL DEFAULT '',
# apk_file_name VARCHAR(500) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

# INSERT INTO app_version(version_code,version_name,version_focus,apk_file_name) VALUES ('1','1.0.0','FirstVersion','sc_date_view_1.0.0-release.apk');

# INSERT INTO app_version(version_code,version_name,version_focus,apk_file_name) VALUES ('2','1.0.1','Update new Version','sc_date_view_1.0.1-release.apk');

# CREATE TABLE comm_link (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# url VARCHAR(3000) NOT NULL DEFAULT '',
# background VARCHAR(3000) NOT NULL DEFAULT '',
# title VARCHAR(3000) NOT NULL DEFAULT '',
# type VARCHAR(3000) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));
#
# CREATE TABLE comm_link_content (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# data_index INT NOT NULL DEFAULT -1,
# comm_link_id VARCHAR(100) NOT NULL DEFAULT '',
# content_type VARCHAR(100) NOT NULL DEFAULT '',
# content_data VARCHAR(3000) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
# machine_translate_data VARCHAR(3000) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
# human_translate_data VARCHAR(3000) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

# CREATE TABLE ship_type (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# ship_id INT NOT NULL DEFAULT -1,
# type_content VARCHAR(100) NOT NULL DEFAULT '',
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

# DELETE FROM ship_en  WHERE name = 'AEGIS Hammerhead';
# DELETE FROM ship_en  WHERE name = 'ANVIL Hawk';
# DELETE FROM ship_en  WHERE name = 'AEGIS Vulcan';
# DELETE FROM ship_en  WHERE name = 'Tumbril - Nova Tank';
# DELETE FROM ship_equipment_en  WHERE ship_id = '150';

# type 常量库
# CREATE TABLE ship_type_constant (
# id INT UNSIGNED NOT NULL AUTO_INCREMENT,
# type_en VARCHAR(500) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
# type_ch VARCHAR(500) CHARACTER SET utf8 NOT NULL DEFAULT '' ,
# update_time timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# PRIMARY KEY ( id ));

# alter table app_version add column state  VARCHAR(100) NOT NULL DEFAULT '';
# alter table app_version add column apk_download_path  VARCHAR(2000) NOT NULL DEFAULT '';
# ALTER TABLE app_version CHANGE version_focus version_focus VARCHAR(500) CHARACTER SET utf8 NOT NULL DEFAULT '';
# ALTER TABLE app_version CHANGE apk_down_path apk_download_path VARCHAR(2000) CHARACTER SET utf8 NOT NULL DEFAULT '';
# alter table `constant_translate` convert to character set utf8;
# alter table ship_en add column ship_price  VARCHAR(3000) NOT NULL DEFAULT '';

