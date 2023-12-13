label change_bg(score, bg_name):
    python:
        renpy.scene()
        print("AAAAAA")
        if score <= 0:
            renpy.show(bg_name)
        else:
            renpy.show(bg_name + " empty")
