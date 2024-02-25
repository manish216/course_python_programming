print('''
                             . .
                              .
                              |
                      .  ~ ~ ~ ~ ~ ~ .
                    `  `$'`$'`$'`$'`S  '
                  '                     '
                 '                       '
                '                         '
               '                           '
              '                             '
             '                               '
            '                                 '
           '                                   '
          '                                     '
         '                                       '
        '                                         '
   . . '`$'                                     `S''. .
   `.       `$'  `$'   `$`   `$'    `$'    `$'       .'
      `    ,    ,    ,   ,   ,   ,   ,   ,   ,  ,   '
                             ( )          )
                            ) * (         (
                           (  *  )        )
                            ) * (         *
                           (  *  )
                            ) * (
                           (  *  )
                            ) * (
                          (   *   )
                          (   *   )
                           )  *  (
                          (   *   )
                        `@~@~@~@~@~@'
                         `@.@.@.@.@'  ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
action = ""
door = ""
direction = input("You're at a cross road. where do you want to go? Type \"left\" or \"right\" \n")
if direction == 'Left':
    action = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if action != '' and action == 'Wait':
        door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one Yellow and One blue. Which colour do you choose?\n")
        if door != '' and door == 'Yellow':
            print("You win.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")

else:
    print("Game Over.")