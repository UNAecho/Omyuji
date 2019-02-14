

class Coordinate:
    # 探索灯笼
    explore_x_left = 589
    explore_x_right = 628
    explore_y_top = 146
    explore_y_bottom = 197

    # 刷狗粮参数
    # 战斗准备阶段，式神编号分别从左上角到右下角为3号、2号、1号位置
    # 这么编号是因为更换式神的时候，从左到右为1-3号

    # 收益号-3号式神判定满级范围区域
    experience_3_member_x_left = 181
    experience_3_member_x_right = 305
    experience_3_member_y_top = 178
    experience_3_member_y_bottom = 384

    # 收益号-2号式神判定满级范围区域
    experience_2_member_x_left = 345
    experience_2_member_x_right = 506
    experience_2_member_y_top = 249
    experience_2_member_y_bottom = 495

    # 收益号-1号式神判定满级范围区域
    experience_1_member_x_left = 573
    experience_1_member_x_right = 791
    experience_1_member_y_top = 321
    experience_1_member_y_bottom = 576

    # 战斗中更换式神选择稀有度的按钮
    experience_rare_button_x = 63
    experience_rare_button_y = 618

    # 探索主界面-突破卷数量截图区域
    explore_number_of_breakthrough_ticker_x_left = 665
    explore_number_of_breakthrough_ticker_x_right = 745
    explore_number_of_breakthrough_ticker_y_top = 40
    explore_number_of_breakthrough_ticker_y_bottom = 67

    # 组队界面-点击创建队伍之后，选择副本类型、层数、队员等级限制
    # 选择副本类型坐标位置
    create_team_choose_type_of_battle_x_left = 361
    create_team_choose_type_of_battle_y_top = 297

    # 选择层数
    create_team_choose_floor_of_battle_x_left = 569
    create_team_choose_floor_of_battle_y_top = 297

    # 限制队友等级-最低级
    create_team_minimum_lv_x_left = 734
    create_team_minimum_lv_y_top = 296

    # 限制队友等级-最高级
    create_team_max_lv_x_left = 820
    create_team_max_lv_y_top = 298

    # 不公开队伍单选按钮位置
    create_private_team_x_left = 670
    create_private_team_x_right = 689
    create_private_team_y_top = 474
    create_private_team_y_bottom = 492

    # 组队界面-协战界面
    # 2号位置点击邀请坐标
    team_ready_for_battle_invite_member_no2_x_left = 636
    team_ready_for_battle_invite_member_no2_y_top = 458

    # 探索主界面-菜单按钮按钮-御魂
    yuhun_x_left = 187
    yuhun_x_right = 204
    yuhun_y_top = 636
    yuhun_y_bottom = 648

    # 御魂主界面-点击御魂大图片选择打御魂
    choose_yuhun_not_yeyuanhuo_x_left = 264
    choose_yuhun_not_yeyuanhuo_x_right = 350
    choose_yuhun_not_yeyuanhuo_y_top = 413
    choose_yuhun_not_yeyuanhuo_y_bottom = 455

    # 探索主界面-菜单按钮按钮-御灵
    yuling_x_left = 352
    yuling_x_right = 406
    yuling_y_top = 596
    yuling_y_bottom = 645

    # 御灵主界面--暗·神龙
    dragon_x_left = 154
    dragon_x_right = 280
    dragon_y_top = 239
    dragon_y_bottom = 530
    # 御灵主界面--暗·白藏主
    baizangzhu_x_left = 392
    baizangzhu_x_right = 531
    baizangzhu_y_top = 237
    baizangzhu_y_bottom = 483
    # 御灵主界面--暗·黑豹
    panther_x_left = 627
    panther_x_right = 762
    panther_y_top = 240
    panther_y_bottom = 492
    # 御灵主界面--暗·孔雀
    peacock_x_left = 860
    peacock_x_right = 996
    peacock_y_top = 280
    peacock_y_bottom = 511

    # 御灵选择层数界面:3层
    yuling_floor_x_left = 248
    yuling_floor_x_right = 480
    yuling_floor_y_top = 302
    yuling_floor_y_bottom = 325

    # 御灵锁定阵容
    yuling_lock_customer_x_left = 248
    yuling_lock_customer_x_right = 480
    yuling_lock_customer_y_top = 302
    yuling_lock_customer_y_bottom = 325

    # 御灵开始战斗
    yuling_start_battle_x_left = 810
    yuling_start_battle_x_right = 902
    yuling_start_battle_y_top = 456
    yuling_start_battle_y_bottom = 488

    # 普通战斗坐标
    # 战斗结束红达摩奖励弹出后，点击屏幕上某一点退出战斗界面，这里选取屏幕左上角的一块位置，不会被各种邀请挡住
    explore_getoutofbattle_x_left = 205
    explore_getoutofbattle_x_right = 250
    explore_getoutofbattle_y_top = 57
    explore_getoutofbattle_y_bottom = 69

    # 战斗胜利红达摩奖励弹出过后，屏幕下的【点击屏幕继续】图标
    explore_click_to_continue_x_left = 494
    explore_click_to_continue_x_right = 666
    explore_click_to_continue_y_top = 633
    explore_click_to_continue_y_bottom = 666

    # 御魂、御灵等各种共同界面，选择层数之后的挑战（进入战斗）按钮
    explore_start_battle_x_left = 796
    explore_start_battle_x_right = 897
    explore_start_battle_y_top = 453
    explore_start_battle_y_bottom = 490

    # 悬赏封印--接受的错号坐标，用于定时任务判断是否有人邀请，如有，则拒绝
    reward_refuse_x_left = 749
    reward_refuse_x_right = 785
    reward_refuse_y_top = 474
    reward_refuse_y_bottom = 511

    # 战斗结束之后红达摩开出奖励，肚子上【魂】字坐标，用于判断战斗是否胜利
    remuneration_x_left = 545
    remuneration_x_right = 574
    remuneration_y_top = 502
    remuneration_y_bottom = 514

    # 探索主界面-菜单按钮-突破
    breakthrough_x_left = 249
    breakthrough_x_right = 302
    breakthrough_y_top = 599
    breakthrough_y_bottom = 648

    # 突破主界面-退出按钮
    breakthrough_logout_x_left = 1037
    breakthrough_logout_x_right = 1071
    breakthrough_logout_y_top = 78
    breakthrough_logout_y_bottom = 105

    # 突破主界面-个人按钮
    breakthrough_personal_x_left = 1075
    breakthrough_personal_x_right = 1113
    breakthrough_personal_y_top = 185
    breakthrough_personal_y_bottom = 263

    # 突破主界面-个人突破票剩余位置
    breakthrough_personal_ticket_x_left = 361
    breakthrough_personal_ticket_x_right = 424
    breakthrough_personal_ticket_y_top = 570
    breakthrough_personal_ticket_y_bottom = 594

    # 突破主界面-个人突破刷新按钮
    breakthrough_personal_refresh_x_left = 859
    breakthrough_personal_refresh_x_right = 1007
    breakthrough_personal_refresh_y_top = 491
    breakthrough_personal_refresh_y_bottom = 535

    # 个人突破 - 点击刷新按钮后提示的确认按钮坐标
    breakthrough_personal_refresh_confirm_x_left = 613
    breakthrough_personal_refresh_confirm_x_right = 741
    breakthrough_personal_refresh_confirm_y_top = 396
    breakthrough_personal_refresh_confirm_y_bottom = 430
    # 个人突破 - 每个人物坐标信息字典制作
    personal_1_info = {"x": 276,
                       "y": 163,
                       "attack_button_x": 335,
                       "attack_button_y": 329}

    personal_2_info = {"x": 598,
                       "y": 150,
                       "attack_button_x": 636,
                       "attack_button_y": 334}

    personal_3_info = {"x": 903,
                       "y": 169,
                       "attack_button_x": 949,
                       "attack_button_y": 328}
    personal_4_info = {"x": 270,
                       "y": 291,
                       "attack_button_x": 331,
                       "attack_button_y": 450}
    personal_5_info = {"x": 602,
                       "y": 312,
                       "attack_button_x": 643,
                       "attack_button_y": 447}
    personal_6_info = {"x": 903,
                       "y": 306,
                       "attack_button_x": 948,
                       "attack_button_y": 450}
    personal_7_info = {"x": 296,
                       "y": 435,
                       "attack_button_x": 334,
                       "attack_button_y": 573}
    personal_8_info = {"x": 597,
                       "y": 411,
                       "attack_button_x": 642,
                       "attack_button_y": 571}
    personal_9_info = {"x": 900,
                       "y": 390,
                       "attack_button_x": 941,
                       "attack_button_y": 553}
    # 个人突破 - 个人坐标信息
    breakthrough_personal_info = {1: personal_1_info,
                                  2: personal_2_info,
                                  3: personal_3_info,
                                  4: personal_4_info,
                                  5: personal_5_info,
                                  6: personal_6_info,
                                  7: personal_7_info,
                                  8: personal_8_info,
                                  9: personal_9_info,
                                  }

    # 个人突破 - 全部打完后点掉弹出奖励位置
    breakthrough_personal_reward_x_left = 778
    breakthrough_personal_reward_x_right = 892
    breakthrough_personal_reward_y_top = 557
    breakthrough_personal_reward_y_bottom = 602


    # 突破主界面-阴阳寮按钮
    breakthrough_union_x_left = 1073
    breakthrough_union_x_right = 1113
    breakthrough_union_y_top = 294
    breakthrough_union_y_bottom = 376

    # 突破-寮突破-判断是否选择阴阳寮-【会长或副会长暂】语句坐标
    breakthrough_union_check_start_x_left = 292
    breakthrough_union_check_start_x_right = 473
    breakthrough_union_check_start_y_top = 225
    breakthrough_union_check_start_y_bottom = 274

    # 突破-寮突破-剩余突破次数截图坐标
    breakthrough_union_attack_remaining_x_left = 243
    breakthrough_union_attack_remaining_x_right = 298
    breakthrough_union_attack_remaining_y_top = 505
    breakthrough_union_attack_remaining_y_bottom = 560

    # 通用 - 接受组队邀请固定坐标
    accept_invite_x_left = 125
    accept_invite_y_top= 256

    # 2018/12/19超鬼王临时坐标
    tuizhi_start_battle_x_left = 1010
    tuizhi_start_battle_x_right = 1067
    tuizhi_start_battle_y_top = 550
    tuizhi_start_battle_y_bottom = 592

    physical_power_value_x_left = 962
    physical_power_value_x_right = 1047
    physical_power_value_y_top = 42
    physical_power_value_y_bottom = 62
