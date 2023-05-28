###########################
##         ITEMS         ##
###########################

jump_checkpoint_disabled_item:
    type: item
    debug: false
    material: gunpowder
    display name: <&7><&o>Previous checkpoint (not working yet)
    lore:
    - <&8>Currently disabled

jump_checkpoint_item:
    type: item
    debug: false
    material: magma_cream
    display name: <&l>Previous checkpoint
    lore:
    - <&8>Right click to go back to the previous checkpoint

jump_quit_item:
    type: item
    debug: false
    material: spruce_door
    display name: <&c><&l>Quit
    lore:
    - <&8>Right click to quit the jump

###########################
##         WORLD         ##
###########################

jump:
    type: world
    events:
      # start
      after player enters jump_start:
      - run start_jump

      # items
      after player right clicks block with:jump_quit_item:
      - run quit_jump
      after player right clicks block with:jump_checkpoint_item:
      - ratelimit <player> 1s
      - run back_to_checkpoint

      on player drops jump_*:
      - determine cancelled
      on player clicks jump_* in inventory:
      - determine cancelled

      # Checkpoints
      on player enters jump_checkpoint_* flagged:jump:
      - run reach_checkpoint def:<context.area.flag[id]>

      # End

      # Fail

start_jump:
  type: task
  script:
  - if !<player.is_op>:
    - narrate <&7>Soon™
    # - stop
  - flag <player> jump:0
  - flag <player> jump_start_time:<util.time_now>
  - playsound <player> sound:ENTITY_ENDER_EYE_DEATH pitch:1
  - run set_items
  - adjust <player> item_slot:5
  - run timer

quit_jump:
  type: task
  script:
  - ratelimit <player> 1s
  - flag <player> jump:!
  - flag <player> jump_start_time:!
  - teleport <player> l@-24.5,59,23.5,0,90,hub
  - inventory set origin:air slot:5
  - inventory set origin:air slot:6
  - playsound <player> ENTITY_VILLAGER_HURT
  - actionbar ""

reach_checkpoint:
  type: task
  script:
  # Verifications
  - define checkpoint_reached <[1]>
  - if <player.flag[jump]> >= <[checkpoint_reached]>:
    - stop
  - if <proc[has_player_cheated].context[<[checkpoint_reached]>]>:
    - narrate "[task] You cheated!"
    - stop
  # The player has reached the checkpoint
  - narrate "You reached checkpoint <[checkpoint_reached]>"
  - flag <player> jump:++
  - playsound <player> sound:entity_experience_orb_pickup
  - run set_items


# Verify that the player didn't skip any previous checkpoint
has_player_cheated:
  type: procedure
  definitions: checkpoint_reached
  script:
  - define player_level <player.flag[jump]>
  - if <[checkpoint_reached]> > <[player_level].add[1]>:
    - determine true
  - determine false

set_items:
  type: task
  script:
  - inventory set origin:jump_quit_item slot:6
  - if <player.flag[jump]> > 0:
    - inventory set origin:jump_checkpoint_item slot:5
  - else:
    - inventory set origin:jump_checkpoint_disabled_item slot:5
  

back_to_checkpoint:
  type: task
  script:
  - playsound <player> sound:item_armor_equip_turtle
  - if <player.flag[jump]> == 1:
    - teleport <player> l@6.5,59,86.5,0,-90,hub
  - if <player.flag[jump]> == 2:
    - teleport <player> l@29.5,37,-26.5,0,180,hub
  - if <player.flag[jump]> == 3:
    - teleport <player> l@33.5,42,-30.5,0,0,hub
  - if <player.flag[jump]> == 4:
    - teleport <player> l@52.5,47,18.5,0,0,hub
  - if <player.flag[jump]> == 5:
    - teleport <player> l@-19.5,23,55.5,0,0,hub
  - if <player.flag[jump]> == 6:
    - teleport <player> l@50.5,65,33.5,0,180,hub
  - if <player.flag[jump]> == 7:
    - teleport <player> l@11.5,89,-23.5,0,180,hub
  - if <player.flag[jump]> == 8:
    - teleport <player> l@53.5,101,13.5,0,0,hub

timer:
  type: task
  script:
  - while <player.has_flag[jump]>:
    # - actionbar <time@2020/01/01_00:00:00:000_Z.add[<player.flag[jump_start_time].from_now>].format[mm:ss:SSS]>
    # - actionbar <player.flag[jump_start_time].format[hh:mm:ss:SSS]>
    - actionbar <time@2020/01/01_01:00:00:000_Z.format[hh:mm:ss]>
    
    # - actionbar <player.flag[jump_start_time]>
    - wait 0.05s
