dic_bool = {
    'yes': True,
    'no': False,
    'do_not_use': False,
}
dic_emotion_limit = {
    'keep_high_emotion': 120,
    'avoid_green_face': 40,
    'avoid_yellow_face': 30,
    'avoid_red_face': 2,
}
dic_emotion_recover = {
    'not_in_dormitory': 20,
    'dormitory_floor_1': 40,
    'dormitory_floor_2': 50,
}
dic_daily = {
    'daily_air': 1,
    'daily_gun': 2,
    'daily_torpedo': 3,
    'index_1': 1,
    'index_2': 2,
    'index_3': 3,
}
dic_chi_to_eng = {
    # Function
    '出击设置': 'setting',
    '收菜设置': 'reward',
    '设备设置': 'emulator',
    '每日任务困难演习': 'daily',
    '每日活动图三倍PT': 'event_daily_ab',
    '主线图': 'main',
    '活动图': 'event',
    '半自动辅助点击': 'semi_auto',
    '7-2三战拣垃圾': 'c72_mystery_farming',
    '12-2打中型练级': 'c122_leveling',
    '12-4打大型练级': 'c124_leveling',

    # Argument
    '启用停止条件': 'enable_stop_condition',
    '使用周回模式': 'enable_fast_forward',
    '如果出击次数大于': 'if_count_greater_than',
    '如果时间超过': 'if_time_reach',
    '如果石油低于': 'if_oil_lower_than',
    '如果触发心情控制': 'if_trigger_emotion_control',
    '如果船舱已满': 'if_dock_full',
    '启用舰队控制': 'enable_fleet_control',
    '启用阵容锁定': 'enable_map_fleet_lock',
    '舰队编号1': 'fleet_index_1',
    '舰队阵型1': 'fleet_formation_1',
    '舰队步长1': 'fleet_step_1',
    '舰队编号2': 'fleet_index_2',
    '舰队阵型2': 'fleet_formation_2',
    '舰队步长2': 'fleet_step_2',
    '舰队编号3': 'fleet_index_3',
    '舰队阵型3': 'fleet_formation_3',
    '舰队步长3': 'fleet_step_3',
    '战斗自律模式': 'combat_auto_mode',
    '舰队编号4': 'fleet_index_4',
    '潜艇出击方案': 'submarine_mode',
    '启用心情消耗': 'enable_emotion_reduce',
    '无视红脸出击警告': 'ignore_low_emotion_warn',
    '心情回复1': 'emotion_recover_1',
    '心情控制1': 'emotion_control_1',
    '全员已婚1': 'hole_fleet_married_1',
    '心情回复2': 'emotion_recover_2',
    '心情控制2': 'emotion_control_2',
    '全员已婚2': 'hole_fleet_married_2',
    '心情回复3': 'emotion_recover_3',
    '心情控制3': 'emotion_control_3',
    '全员已婚3': 'hole_fleet_married_3',
    '启用血量平衡': 'enable_hp_balance',
    '启用低血量撤退': 'enable_low_hp_withdraw',
    '先锋血量平衡阈值': 'scout_hp_difference_threshold',
    '低血量撤退阈值': 'low_hp_withdraw_threshold',
    '启用退役': 'enable_retirement',
    '使用一键退役': 'use_one_click_retirement',
    '退役方案': 'retire_mode',
    '退役白皮': 'retire_n',
    '退役蓝皮': 'retire_r',
    '退役紫皮': 'retire_sr',
    '退役金皮': 'retire_ssr',
    '启用掉落记录': 'enable_drop_screenshot',
    '掉落保存目录': 'drop_screenshot_folder',
    '启用开荒': 'enable_map_clear_mode',
    '开荒停止条件': 'clear_mode_stop_condition',
    '地图全清星星': 'map_star_clear_all',
    '启用收获': 'enable_reward',
    '收菜间隔': 'reward_interval',
    '启用石油收获': 'enable_oil_reward',
    '启用物资收获': 'enable_coin_reward',
    '启用任务收获': 'enable_mission_reward',
    '启用委托收获': 'enable_commission_reward',
    '启用战术学院收获': 'enable_tactical_reward',
    '委托时间限制': 'commission_time_limit',
    '委托耗时小于2h': 'duration_shorter_than_2',
    '委托耗时超过6h': 'duration_longer_than_6',
    '委托过期小于2h': 'expire_shorter_than_2',
    '委托过期大于6h': 'expire_longer_than_6',
    '日常委托': 'daily_comm',
    '主要委托': 'major_comm',
    '钻头类额外委托': 'extra_drill',
    '部件类额外委托': 'extra_part',
    '魔方类额外委托': 'extra_cube',
    '石油类额外委托': 'extra_oil',
    '教材类额外委托': 'extra_book',
    '钻头类紧急委托': 'urgent_drill',
    '部件类紧急委托': 'urgent_part',
    '魔方类紧急委托': 'urgent_cube',
    '教材类紧急委托': 'urgent_book',
    '装备类紧急委托': 'urgent_box',
    '钻石类紧急委托': 'urgent_gem',
    '观舰类紧急委托': 'urgent_ship',
    '战术学院夜间时段': 'tactical_night_range',
    '技能书稀有度': 'tactical_book_tier',
    '技能书优先使用同类型': 'tactical_exp_first',
    '技能书夜间稀有度': 'tactical_book_tier_night',
    '技能书夜间优先使用同类型': 'tactical_exp_first_night',
    '设备': 'serial',
    '包名': 'package_name',
    '出错时保存log和截图': 'enable_error_log_and_screenshot_save',
    '保存透视识别出错的图像': 'enable_perspective_error_image_save',
    '使用ADB截图': 'use_adb_screenshot',
    '使用ADB点击': 'use_adb_control',
    '战斗中截图间隔': 'combat_screenshot_interval',
    '打每日': 'enable_daily_mission',
    '打困难': 'enable_hard_campaign',
    '打演习': 'enable_exercise',
    '战术研修': 'daily_mission_1',
    '斩首行动': 'daily_mission_2',
    '商船护航': 'daily_mission_4',
    '海域突进': 'daily_mission_5',
    '每日舰队': 'daily_fleet',
    '每日舰队快速换装': 'daily_equipment',
    '困难地图': 'hard_campaign',
    '困难舰队': 'hard_fleet',
    '困难舰队快速换装': 'hard_equipment',
    '演习对手选择': 'exercise_choose_mode',
    '演习次数保留': 'exercise_preserve',
    '演习尝试次数': 'exercise_try',
    '演习SL阈值': 'exercise_hp_threshold',
    '演习低血量确认时长': 'exercise_low_hp_confirm',
    '演习快速换装': 'exercise_equipment',
    '主线地图出击': 'main_stage',
    '活动地图': 'event_stage',
    'sp地图': 'sp_stage',
    '活动名称': 'event_name',
    '活动名称ab': 'event_name_ab',
    '进图准备': 'enable_semi_map_preparation',
    '跳过剧情': 'enable_semi_story_skip',
    'BOSS队踩A3': 'boss_fleet_step_on_a3',
    '大型敌人忍耐': 's3_enemy_tolerance',
    '非大型敌人进图忍耐': 'non_s3_enemy_enter_tolerance',
    '非大型敌人撤退忍耐': 'non_s3_enemy_withdraw_tolerance',
    '拣弹药124': 'ammo_pick_up_124',

    # Option
    '是': 'yes',
    '否': 'no',
    '单纵阵': 'formation_1',
    '复纵阵': 'formation_2',
    '轮形阵': 'formation_3',
    '自律': 'combat_auto',
    '手操': 'combat_manual',
    '中路站桩': 'stand_still_in_the_middle',
    '不使用': 'do_not_use',
    '仅狩猎': 'hunt_only',
    '每战出击': 'every_combat',
    '空弹出击': 'when_no_ammo',
    'BOSS战出击': 'when_boss_combat',
    'BOSS战BOSS出现后召唤': 'when_boss_combat_boss_appear',
    '未放置于后宅': 'not_in_dormitory',
    '后宅一楼': 'dormitory_floor_1',
    '后宅二楼': 'dormitory_floor_2',
    '保持经验加成': 'keep_high_emotion',
    '防止绿脸': 'avoid_green_face',
    '防止黄脸': 'avoid_yellow_face',
    '防止红脸': 'avoid_red_face',
    '退役全部': 'retire_all',
    '退役10个': 'retire_10',
    '地图通关': 'map_100',
    '地图三星': 'map_3_star',
    '地图绿海': 'map_green',
    '航空': 'daily_air',
    '炮击': 'daily_gun',
    '雷击': 'daily_torpedo',
    '第一个': 'index_1',
    '第二个': 'index_2',
    '第三个': 'index_3',
    '经验最多': 'max_exp',
    '排名最前': 'max_ranking',
    '福利队': 'good_opponent',

    # Event
    '北境序曲': 'event_20200227_cn',
    '复刻斯图尔特的硝烟': 'event_20200312_cn',
    '微层混合': 'event_20200326_cn',
    '复刻苍红的回响': 'event_20200423_cn',
    '夜幕下的归途': 'event_20200507_cn',
}
dic_eng_to_chi = {v: k for k, v in dic_chi_to_eng.items()}


def to_bool(string):
    return dic_bool.get(string, string)


def to_list(string):
    if string.isdigit():
        return None
    out = [int(letter.strip()) for letter in string.split(',')]
    return out
