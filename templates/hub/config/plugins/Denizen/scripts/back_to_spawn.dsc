back_to_spawn:
    type: world
    events:
        on player exits spawn_region:
        - teleport <player> l@0.5,65,0.5,0,90,hub
        - playsound <player.location> <player> sound:entity_enderman_teleport