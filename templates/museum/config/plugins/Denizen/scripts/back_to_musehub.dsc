musehub_command:
    type: command
    debug: false
    name: musehub
    aliases:
    - mhub
    description: Teleport the player back to the hub of the museum.
    usage: /musehub
    script:
    - flag <player> isnt_at_musehub:!
    - execute as_player "mv tp musehub"