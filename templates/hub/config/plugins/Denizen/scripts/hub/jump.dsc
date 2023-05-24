jump_checkpoint_item:
    type: item
    debug: false
    material: gunpowder
    display name: <&7><&l>Previous checkpoint
    lore:
    - <&8>Right click to go back to the previous checkpoint

jump_quit_item:
    type: item
    debug: false
    material: redstone
    display name: <&c><&l>Quit
    lore:
    - <&8>Right click to quit the jump


jump:
    type: world
    events:
      # start
      after player enters jump_start:
      - if !<player.is_op>
        - determine cancelled
      - flag <player> jump:0
      - narrate "wip"
      - inventory set origin:jump_checkpoint_item slot:5
      - inventory set origin:jump_quit_item slot:6
      - adjust <player> item_slot:5

      # items
      after player right clicks block with:jump_quit_item:
      - ratelimit <player> 1s
      - flag <player> jump:!
      - teleport <player> l@-24.5,59,23.5,0,90,hub
      - inventory set origin:air slot:5
      - inventory set origin:air slot:6
      after player right clicks block with:jump_checkpoint_item:
      - ratelimit <player> 1s
      - narrate "Checkpoint!"
      on player drops jump_*:
      - determine cancelled
      on player clicks jump_* in inventory:
      - determine cancelled

      # Checkpoints
      after player enters jump_checkpoint_*:
      - narrate "checkpoint *!"
      after player enters jump_checkpoint_1:
      - if <player.flag[jump]> != 0:
        - narrate "You forgot a checkpoint!"
      - narrate "Checkpoint 1!"
      - flag <player> jump:1
      after player enters jump_checkpoint_2:
      - if <player.flag[jump]> != 1:
        - narrate "You forgot a checkpoint!"
      - narrate "Checkpoint 2!"
      - flag <player> jump:2
