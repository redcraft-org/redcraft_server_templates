launchpads:
    type: world
    events:
        after entity enters launchpad_to_crea_build:
        - adjust <player> velocity:l@-4.5,0.9,-3.1,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        - wait 0.75s
        - adjust <player> velocity:l@-4.275,0.9,-1.03,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:1

        after entity enters launchpad_to_crea_redstone:
        - adjust <player> velocity:l@-4.5,0.9,2.7,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        - wait 0.75s
        - adjust <player> velocity:l@-3.6,0.9,0.9,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:1

        after entity enters launchpad_to_survival:
        - adjust <player> velocity:l@-4,1,0,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        - wait 0.75s
        - adjust <player> velocity:l@-3,1,0,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:1
        - wait 0.75s
        - adjust <player> velocity:l@-2,0.2,0,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:0.1

        after entity enters launchpad_crea_redstone_to_spawn:
        - adjust <player> velocity:l@4.5,0.9,-2.7,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        - wait 0.75s
        - adjust <player> velocity:l@4.5,0.9,-0.9,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:1

        after entity enters launchpad_crea_build_to_spawn:
        - adjust <player> velocity:l@7.2,0.9,1.8,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        - wait 0.75s
        - adjust <player> velocity:l@3.6,0.9,0.9,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:1
        - wait 0.75s
        - adjust <player> velocity:l@1.8,0.18,0,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:0.1

        after entity enters launchpad_survival_to_spawn:
        - adjust <player> velocity:l@4,1,0,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:2
        - wait 0.75s
        - adjust <player> velocity:l@3,1,0,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:1
        - wait 0.75s
        - adjust <player> velocity:l@2,0.2,0,0,0,spawn
        - playsound <player.location> <player> sound:ENTITY_WITHER_SHOOT pitch:0.1
