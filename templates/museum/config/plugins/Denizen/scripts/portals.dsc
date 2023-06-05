portals:
    type: world
    events:
        after entity enters portal_kh_semi_rp:
        - execute as_player "mv tp "KingdomHills Semi-RP""
        - run show_musehub_action

        after entity enters portal_kh_hardcore:
        - execute as_player "mv tp "KingdomHills Hardcore""
        - run show_musehub_action

        after entity enters portal_topred_redstone_plot:
        - execute as_player "mv tp "TopRed Plot""
        - run show_musehub_action

        after entity enters portal_topred_new_irs:
        - execute as_player "mv tp "TopRed IRS new""
        - run show_musehub_action

        after entity enters portal_topred_old_irs:
        - execute as_player "mv tp "TopRed IRS old""
        - run show_musehub_action

        after entity enters portal_kh_crea_plot:
        - execute as_player "mv tp "KingdomHills Plot""
        - run show_musehub_action

        after entity enters portal_kh_freebuild:
        - execute as_player "mv tp "KingdomHills Freebuild""
        - run show_musehub_action

show_musehub_action:
    type: task
    script:
    - flag <player> isnt_at_musehub:true
    - while <player.has_flag[isnt_at_musehub]>:
        - actionbar "<&6><&l>Use /musehub to quit"
        - wait 1s