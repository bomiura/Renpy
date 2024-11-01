# 定義
define s = Character(_("Sylvie"), color="#adff2f")
# スタート
label start:
    play music "illurock.opus"
    scene bg uni
    with fade
    show sylvie blue smile
    with dissolve
    s "これがスタートです｡"

    menu:
        "右へ行きますか? 左へ行きますか?"
        "右へ!":
            jump rightside
        "左へ!":
            jump leftside

label rightside:
    return
label leftside:
    return
    
