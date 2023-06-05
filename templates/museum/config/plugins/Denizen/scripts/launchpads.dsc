launchpads:
    type: world
    events:
        after entity enters launchpad_to_kh_hardcore_crea_plot:
        - adjust <player> velocity:l@-3,0.7,3,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        
        after entity enters launchpad_to_kh_freebuild_semi_rp:
        - adjust <player> velocity:l@-3,0.7,-3,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        
        after entity enters launchpad_to_topred_old_irs:
        - adjust <player> velocity:l@3,0.7,3,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        
        after entity enters launchpad_to_topred_redstone_plot_new_irs:
        - adjust <player> velocity:l@3,0.7,-3,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
