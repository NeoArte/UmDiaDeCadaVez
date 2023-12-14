define config.log = "log_txt"
define config.default_language = "portuguese"
define config.language = "portuguese"
define config.main_menu_music = "main_menu.mp3"
define config.main_menu_music_fadein = 2.0

define score = 0

python early:
    from random import randint
    import json
    def parse_choice(lexer):
        print("Start parse")
        lexer.expect_block("choice")
        lexer.require(':')
        lexer.expect_eol()
        subblock_lexer = lexer.subblock_lexer()
        choices = []
        while subblock_lexer.advance():
            with subblock_lexer.catch_error():
                # subblock_lexer.expect_block("label option")
                option = subblock_lexer.subblock_lexer().renpy_block()
                choices.append(option)
        return choices

    def execute_choice(parsed_object):
        renpy.say("DEBUG", "1")
        renpy.say("DEBUG", "2")
        renpy.say("DEBUG", "3")
        renpy.log(len(parsed_object))
        renpy.log(parsed_object[0].__repr__)
        return parsed_object[0]

    def lint_choice(parsed_object):
        print("Started Lint")
        renpy.write_log(parsed_object)
        for obj in parsed_object:
            tte = renpy.check_text_tags(parsed_object)
            if tte:
                renpy.error(tte)
    renpy.register_statement(
        "choice",
        block="script",
        parse=parse_choice,
        execute=execute_choice,
        lint=lint_choice
        )

init 1 python:
    from enum import IntEnum
    class WeekDay(IntEnum):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
    week_colors = ["#999999", "#008B8B", "#FFFF00", "", "#333388"]


default day_color = week_colors[WeekDay.ONE]
label setup:
    queue music main_menu loop fadein 1.0
    define diego = Character("Diego",
                             image="diego",
                             who_prefix='{color=[day_color]}',
                             who_suffix='{/color}',
                             what_prefix='{color=[day_color]}',
                             what_suffix='{/color}')
    define rat_think = Character("Ratinho", what_prefix='(', what_suffix=')')
    define rat_speak = Character("Ratinho", what_prefix='*', what_suffix='*')
    transform rat_right:
        xzoom -1.0
        yalign 1.5
        xalign 1.0
    transform rat_stand_right:
        xzoom 1.0
        yalign 2.5
        xalign 1.0
    return
