portals:
    type: world
    events:
        after entity enters portal_to_museum:
        - teleport <player> l@0.5,65,0.5,0,90,hub
        - execute as_player "server museum"
        - playsound <player.location> <player> sound:entity_enderman_teleport