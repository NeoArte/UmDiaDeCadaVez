init 1 python:
    from enum import IntEnum
    class WeekDay(IntEnum):
        ONE = 0
        TWO = 1
        THREE = 2
    week_colors = ["#008B8B", "#FFFF00"]


default day_color = week_colors[WeekDay.ONE]
label setup:
    define diego = Character("Diego",
                             image="rodrigo",
                             what_prefix='{color=[day_color]}',
                             what_suffix='{/color}')
    define rat_think = Character("", what_prefix='(', what_suffix=')')
    define rat_speak = Character("Ratinho", what_prefix='*', what_suffix='*')
    return
