# -*- coding: UTF-8 -*-
import os
import platform
from CitizenWikiRobot.TranslateEntity import TranslateEntity


class StaticField:

    def __init__(self):
        print ""

    BASE_URL = "https://robertsspaceindustries.com"
    BASE_SHIP_URL = "https://starcitizen.tools/Ships"
    CTM_MODEL_PATH = "/home/ftpuser/ctmfiles/"
    IMAGE_PATH = "/var/www/html/scdata/resources/media/image/"

    FATHER_PATH = os.path.abspath(os.path.dirname(__file__))

    SHIP_NAME_MAP = dict()
    COMPANY_MAP = dict()
    SHIP_GROUP = dict()
    CONSTANT_GROUP = dict()

    Radar = "radar"
    Computers = "computers"
    Power_Plants = "power_plants"
    Coolers = "coolers"
    Shield_Generators = "shield_generators"
    Fuel_Intakes = "fuel_intakes"
    Fuel_Tanks = "fuel_tanks"
    Quantum_Drives = "quantum_drives"
    Jump_Modules = "jump_modules"
    Quantum_Fuel_Tanks = "quantum_fuel_tanks"
    Main_Thrusters = "main_thrusters"
    Maneuvering_Thrusters = "maneuvering_thrusters"
    Weapons = "weapons"
    Turrets = "turrets"
    Missiles = "missiles"
    Utility_Items = "utility_items"

    CONSTANT_GROUP['radar'] = '雷达'
    CONSTANT_GROUP['computers'] = '计算机'
    CONSTANT_GROUP['power_plants'] = '发电装置'
    CONSTANT_GROUP['coolers'] = '冷却装置'
    CONSTANT_GROUP['shield_generators'] = '护盾发生器'
    CONSTANT_GROUP['fuel_intakes'] = '喷油器'
    CONSTANT_GROUP['fuel_tanks'] = '燃料箱'
    CONSTANT_GROUP['quantum_drives'] = '量子引擎'
    CONSTANT_GROUP['jump_modules'] = '跳跃模块'
    CONSTANT_GROUP['quantum_fuel_tanks'] = '量子燃料箱'
    CONSTANT_GROUP['main_thrusters'] = '主推进器'
    CONSTANT_GROUP['maneuvering_thrusters'] = '辅助推进器'
    CONSTANT_GROUP['weapons'] = '武器'
    CONSTANT_GROUP['turrets'] = '炮塔'
    CONSTANT_GROUP['missiles'] = '导弹'
    CONSTANT_GROUP['utility_items'] = '功能扩展'

    COMPANY_MAP['Aegis Dynamics'] = '圣盾动力'
    COMPANY_MAP['Anvil Aerospace'] = '铁砧航空'
    COMPANY_MAP['AopoA'] = 'AopoA'
    COMPANY_MAP['ARGO Astronautics'] = 'ARGO'
    COMPANY_MAP['Banu'] = '巴奴'
    COMPANY_MAP['Consolidated Outland'] = '联合外域'
    COMPANY_MAP['Crusader Industries'] = '十字军'
    COMPANY_MAP['Drake Interplanetary'] = '德雷克'
    COMPANY_MAP['Esperia Inc.'] = '埃斯佩拉'
    COMPANY_MAP['Kruger Intergalactic'] = '克鲁格'
    COMPANY_MAP['Musashi Industrial and Starflight Concern'] = '武藏工业'
    COMPANY_MAP['Origin Jumpworks GmbH'] = '起源跳跃'
    COMPANY_MAP['Roberts Space Industries'] = '罗伯茨太空工业'

    SHIP_NAME_MAP['Avenger Stalker'] = '复仇者潜行'
    SHIP_NAME_MAP['Avenger Titan'] = '复仇者泰坦'
    SHIP_NAME_MAP['Avenger Titan Renegade'] = '复仇者变节者'
    SHIP_NAME_MAP['Avenger Warlock'] = '复仇者封锁'
    SHIP_NAME_MAP['Eclipse'] = '日蚀'
    SHIP_NAME_MAP['Gladius'] = '短剑'
    SHIP_NAME_MAP['Gladius Valiant'] = '短剑勇士'
    SHIP_NAME_MAP['AEGIS Hammerhead'] = '锤头鲨'
    SHIP_NAME_MAP['Idris-M'] = '伊德里斯M'
    SHIP_NAME_MAP['Idris-P'] = '伊德里斯P'
    SHIP_NAME_MAP['Javelin'] = '标枪'
    SHIP_NAME_MAP['N6G Avenger Trainer'] = '复仇者教练'
    SHIP_NAME_MAP['Reclaimer'] = '再生者'
    SHIP_NAME_MAP['Redeemer'] = '救赎'
    SHIP_NAME_MAP['Retaliator'] = '报复'
    SHIP_NAME_MAP['Sabre'] = '军刀'
    SHIP_NAME_MAP['Sabre Comet'] = '军刀彗星'
    SHIP_NAME_MAP['Sabre Raven'] = '军刀渡鸦'
    SHIP_NAME_MAP['Vanguard Harbinger'] = '先锋先遣'
    SHIP_NAME_MAP['Vanguard Hoplite'] = '先锋重装'
    SHIP_NAME_MAP['Vanguard Sentinel'] = '先锋哨卫'
    SHIP_NAME_MAP['Vanguard Warden'] = '先锋巡猎'
    SHIP_NAME_MAP['Carrack'] = '克拉克'
    SHIP_NAME_MAP['Crucible'] = '坩埚'
    SHIP_NAME_MAP['DireHawk'] = 'DireHawk'
    SHIP_NAME_MAP['F7A Hornet'] = 'F7A大黄蜂'
    SHIP_NAME_MAP['F7A Hornet Mk II'] = 'F7A大黄蜂MK2'
    SHIP_NAME_MAP['F7A-R Hornet Tracker'] = 'F7A大黄蜂追踪'
    SHIP_NAME_MAP['F7C Hornet'] = '大黄蜂基础'
    SHIP_NAME_MAP['F7C Hornet Wildfire'] = '大黄蜂野火'
    SHIP_NAME_MAP['F7C-M Super Hornet'] = '超级大黄蜂'
    SHIP_NAME_MAP['F7C-R Hornet Tracker'] = '大黄蜂追踪'
    SHIP_NAME_MAP['F7C-S Hornet Ghost'] = '大黄蜂幽灵'
    SHIP_NAME_MAP['F8 Lightning'] = 'F8闪电'
    SHIP_NAME_MAP['Gladiator'] = '角斗士'
    SHIP_NAME_MAP['ANVIL Hawk'] = '鹰'
    SHIP_NAME_MAP['Hurricane'] = '飓风'
    SHIP_NAME_MAP['ShadowHawk'] = 'ShadowHawk'
    SHIP_NAME_MAP['T8A Gladiator'] = 'T8A角斗士'
    SHIP_NAME_MAP['Terrapin'] = '水龟'
    SHIP_NAME_MAP['Khartu-al'] = '卡图'
    SHIP_NAME_MAP['Nox'] = 'Nox'
    SHIP_NAME_MAP['Nox Kue'] = 'Nox Kue'
    SHIP_NAME_MAP['Qhire Khartu'] = 'Qhire卡图'
    SHIP_NAME_MAP['Volper'] = 'Volper'
    SHIP_NAME_MAP['MPUV Cargo'] = '南船座货运'
    SHIP_NAME_MAP['MPUV Personnel'] = '南船座客运'
    SHIP_NAME_MAP['Mustang Alpha'] = '野马A'
    SHIP_NAME_MAP['Mustang Beta'] = '野马B'
    SHIP_NAME_MAP['Mustang Delta'] = '野马D'
    SHIP_NAME_MAP['Mustang Gamma'] = '野马G'
    SHIP_NAME_MAP['Mustang Omega'] = '野马O'
    SHIP_NAME_MAP['Pioneer'] = '开拓者'
    SHIP_NAME_MAP['Genesis'] = '创世纪'
    SHIP_NAME_MAP['Buccaneer'] = '掠夺者'
    SHIP_NAME_MAP['Caterpillar'] = '毛虫'
    SHIP_NAME_MAP['Caterpillar Pirate Edition'] = '毛虫还盗版'
    SHIP_NAME_MAP['Cutlass Black'] = '黑弯刀'
    SHIP_NAME_MAP['Cutlass Blue'] = '蓝弯刀'
    SHIP_NAME_MAP['Cutlass Red'] = '红弯刀'
    SHIP_NAME_MAP['Dragonfly'] = '蜻蜓'
    SHIP_NAME_MAP['Dragonfly Yellowjacket'] = '黄蜻蜓'
    SHIP_NAME_MAP['Dragonfly Black'] = '黑蜻蜓'
    SHIP_NAME_MAP['Herald'] = '信使'
    SHIP_NAME_MAP['Blade (replica)'] = '刀锋'
    SHIP_NAME_MAP['Glaive (replica)'] = '长刀'
    SHIP_NAME_MAP['Prowler'] = '徘徊'
    SHIP_NAME_MAP['Scythe (replica)'] = '死镰'
    SHIP_NAME_MAP['P52 Merlin'] = 'P52梅林'
    SHIP_NAME_MAP['P72 Archimedes'] = 'P72'
    SHIP_NAME_MAP['Endeavor'] = '奋进'
    SHIP_NAME_MAP['Freelancer'] = '自由行者'
    SHIP_NAME_MAP['Freelancer DUR'] = '自由DUR'
    SHIP_NAME_MAP['Freelancer MAX'] = '自由MAX'
    SHIP_NAME_MAP['Freelancer MIS'] = '自由MIS'
    SHIP_NAME_MAP['Hull A'] = '货轮A'
    SHIP_NAME_MAP['Hull B'] = '货轮B'
    SHIP_NAME_MAP['Hull C'] = '货轮C'
    SHIP_NAME_MAP['Hull D'] = '货轮D'
    SHIP_NAME_MAP['Hull E'] = '货轮E'
    SHIP_NAME_MAP['Prospector'] = '勘探者'
    SHIP_NAME_MAP['Razor'] = '剃刀'
    SHIP_NAME_MAP['Reliant Kore'] = '信赖Kore'
    SHIP_NAME_MAP['Reliant Mako'] = '信赖Mako'
    SHIP_NAME_MAP['Reliant Sen'] = '信赖Sen'
    SHIP_NAME_MAP['Reliant Tana'] = '信赖Tana'
    SHIP_NAME_MAP['Starfarer'] = '星际远航者'
    SHIP_NAME_MAP['Starfarer Gemini'] = '星际远航者双子座'
    SHIP_NAME_MAP['300i'] = '300i'
    SHIP_NAME_MAP['315p'] = '315p'
    SHIP_NAME_MAP['325a'] = '325a'
    SHIP_NAME_MAP['350r'] = '350r'
    SHIP_NAME_MAP['600i Explorer'] = '600i探索'
    SHIP_NAME_MAP['600i Touring'] = '600i游览'
    SHIP_NAME_MAP['85X'] = '85X'
    SHIP_NAME_MAP['890 Jump'] = '890'
    SHIP_NAME_MAP['M50'] = 'M50'
    SHIP_NAME_MAP['X1'] = 'X1'
    SHIP_NAME_MAP['X1 Force'] = 'X1F'
    SHIP_NAME_MAP['X1 Velocity'] = 'X1V'
    SHIP_NAME_MAP['Aurora CL'] = '极光CL'
    SHIP_NAME_MAP['Aurora ES'] = '极光ES'
    SHIP_NAME_MAP['Aurora LN'] = '极光LN'
    SHIP_NAME_MAP['Aurora LX'] = '极光LX'
    SHIP_NAME_MAP['Aurora MR'] = '极光MR'
    SHIP_NAME_MAP['Bengal'] = '孟加拉'
    SHIP_NAME_MAP['Constellation Andromeda'] = '仙女座'
    SHIP_NAME_MAP['Constellation Aquila'] = '天鹰座'
    SHIP_NAME_MAP['Constellation Phoenix'] = '凤凰座'
    SHIP_NAME_MAP['Constellation Taurus'] = '金牛座'
    SHIP_NAME_MAP['Nova'] = 'Nova'
    SHIP_NAME_MAP['Orion'] = '猎户座'
    SHIP_NAME_MAP['Pegasus'] = '飞马座'
    SHIP_NAME_MAP['Polaris'] = '北极星'
    SHIP_NAME_MAP['Zeus'] = '宙斯'
    SHIP_NAME_MAP['Defender'] = '守卫者'
    SHIP_NAME_MAP['Merchantman'] = '巴奴商船'
    SHIP_NAME_MAP['Khartu-Al'] = '卡图AL'
    SHIP_NAME_MAP['Constellation Phoenix Emerald'] = '翡翠凤凰座'
    SHIP_NAME_MAP['AEGIS Vulcan'] = '火神'
    SHIP_NAME_MAP['Tumbril - Nova Tank'] = 'Nova Tank'

    Description = "Description"
    Size = "Size"
    Focus = "Focus"
    Production_State = "Production State"
    Max_Crew = "Max Crew"
    Min_Crew = "Min Crew"
    Cargo_Capacity = "Cargo Capacity"
    REC_Cost = "REC Cost"
    Pledge_Cost = "Pledge Cost"
    Mass = "Mass"
    SCM_Speed = "SCM Speed"
    Afterburner_Speed = "Afterburner Speed"
    Length = "Length"
    Beam = "Beam"
    Height = "Height"
    Pitch_Max = "Pitch Max"
    Roll_Max = "Roll Max"
    Yaw_Max = "Yaw Max"
    X_Axis_Acceleration = "X-Axis Acceleration"
    Y_Axis_Acceleration = "Y-Axis Acceleration"
    Z_Axis_Acceleration = "Z-Axis Acceleration"


    Avionics = "avionics"
    Modular = "modular"
    Propulsion = "propulsion"
    Thrusters = "thrusters"
    Weaponry = "weapons"

    Manufacturer = "manufacturer"
    Name = "name"
    Type = "type"
    Details = "details"
    Size = "size"
    Quantity = "quantity"



    @staticmethod
    def get_system_file_connector():
        if platform.system() == "Windows":
            return "\\"
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            return "/"
