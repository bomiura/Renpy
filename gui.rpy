﻿################################################################################
## 初期化
################################################################################

## このファイルは GUI をカスタマイズする基本的なオプションを記載しています。次の
## init offset ステートメントにより、このファイルの init 文は他のファイルの init
## 文よりも先に実行されます。
init offset = -2

## まず最初に gui.init を実行して、スタイルを扱いやすい初期値にリセットし、ゲー
## ムの横幅と縦幅を設定します。
init python:
    gui.init(1280, 720)

## スクリーンやトランスフォームのプロパティが無効または不安定であることをチェッ
## クできるようにする。
define config.check_conflicting_properties = True


################################################################################
## GUI 設定変数
################################################################################


## カラー #########################################################################
##
## インターフェースのテキストのカラー。

## アクセントカラー。タイトル・ラベル・ハイライトされたテキスト・ボタンの背景・
## スライダーのつまみ等、インターフェイスの様々な場所で使います。
define gui.accent_color = '#0099cc'

## selected（選択中）でも hover（フォーカス中）でもない状態のテキストボタンのカ
## ラー。
define gui.idle_color = '#888888'

## スモールカラー。クイックメニューなどの、明るさを調節する必要のある小さなテキ
## ストボタンに使います。
define gui.idle_small_color = '#aaaaaa'

## hover（フォーカス中）のテキストボタンのカラー。また、バーの充足部分（左側）や
## スライダーのつまみ等の画像を再生成するときにも使われます。
define gui.hover_color = '#66c1e0'

## selected（選択中）のテキストボタンのカラー。ボタンが現在のスクリーンであった
## り、環境設定の値と一致したりすると、ボタンは選択中になります。
define gui.selected_color = '#ffffff'

## insensitive (選択不可能）なテキストボタンのカラー。
define gui.insensitive_color = '#8888887f'

## バーの非充足部分（右側）やスライダーの背景部分のカラー。バーやスライダーのカ
## ラーは直接使われず、 GUI を変更・更新した場合の画像生成に使われます。
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## text_color は台詞や選択肢のテキストのカラーです。interface_text_color はヒス
## トリーやヘルプなどそれ以外のテキストのカラーです。
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## フォントとフォントサイズ ################################################################

## ゲーム内の台詞や選択肢に使われるフォント。
define gui.text_font = "SourceHanSansLite.ttf"

## キャラクターの名前に使われるフォント。
define gui.name_text_font = "SourceHanSansLite.ttf"

## ゲームメニューなどのインターフェースに使われるテキストのフォント。
define gui.interface_text_font = "SourceHanSansLite.ttf"

## 一般的な台詞のテキストサイズ。
define gui.text_size = 22

## キャラクターの名前のテキストサイズ。
define gui.name_text_size = 30

## インターフェースのテキストサイズ。
define gui.interface_text_size = 22

## インターフェースのラベル（見出し）のテキストサイズ。
define gui.label_text_size = 24

## notify（通知）スクリーンのテキストサイズ。
define gui.notify_text_size = 16

## ゲームタイトルのテキストサイズ。
define gui.title_text_size = 50


## メインメニューとゲームメニュー #############################################################

## メインメニューとゲームメニューの背景画像。メインメニューはゲーム起動時に最初
## に表示されるメニュー、ゲームメニューはゲーム中右クリックで呼び出せるメニュー
## です。画像を変えたい場合は gui ディレクトリーにある該当の画像を入れ替えてくだ
## さい。
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## ダイアローグ（台詞） ##################################################################
##
## 以下の変数は、一度に表示される台詞とキャラクターの名前を、どのようにスクリー
## ンに表示するか制御します。

## 台詞を表示するテキストボックスの高さ。テキストボックスの画像を変えたい場合は
## gui/textbox.png の画像を入れ替えます。
define gui.textbox_height = 185

## 画面に対する、テキストボックスの垂直方向の位置。 0.0 は上端、0.5 は中央、 1.0
## は下端になります。
define gui.textbox_yalign = 1.0


## テキストボックスに対する、キャラクター名の位置。左上からのピクセル数で指定す
## るか 0.0 から 1.0 までの小数で指定します。 0.5 は中央に表示。
define gui.name_xpos = 240
define gui.name_ypos = 0

## キャラクター名の文字揃え。 0.0 は左揃え、0.5 は中央揃え、 1.0 は右揃えになり
## ます。0.0 以外にした場合、キャラクター名の位置の調整も必要になります。
define gui.name_xalign = 0.0

## キャラクター名を表示するネームボックスのサイズ。None にすると、自動的に決定さ
## れます。画像を変えたい場合は gui/textbox.png の画像を入れ替えます（デフォルト
## 画像は透明なので表示されません）。
define gui.namebox_width = None
define gui.namebox_height = None

## ネームボックスのボーダーのサイズ。左、上、右、下の順で指定します。ボックスの
## サイズは、その中に表示されるキャラクター名のサイズから更にボーダー分拡張した
## サイズになります。
define gui.namebox_borders = Borders(5, 5, 5, 5)

## True に設定すると、ネームボックスの背景画像をスケーリングではなくタイリングで
## 表示します。
define gui.namebox_tile = False


## テキストボックスに対する、台詞の位置。左上からのピクセル数で指定するか 0.0 か
## ら 1.0 までの小数で指定します。 0.5 だと中央に表示。
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

## 台詞の最大ピクセル幅。このピクセル幅以上の台詞は折り返して表示されます。
define gui.dialogue_width = 744

## 台詞の文字揃え。 0.0 は左揃え、0.5 は中央揃え、 1.0 は右揃えになります。0.0
## 以外にした場合、台詞の位置の調整も必要になります。
define gui.dialogue_text_xalign = 0.0


## ボタン #########################################################################
##
## 以下の変数は、ボタンをどのように表示するか制御します。画像を変えたい場合は
## gui/button ディレクトリーにある各 background.png の画像を入れ替えます（デフォ
## ルト画像は透明なので表示されません）。ボタンの状態に合わせて画像を変えたい場
## 合は、ファイル名に idle_、hover_、selected_、selected_hover_ の接頭辞を付けま
## す。

## ボタンの縦幅と横幅。None にすると自動的に計算されます。
define gui.button_width = None
define gui.button_height = None

## ボタンのボーダーのサイズ。左、上、右、下の順で指定します。ボタンのサイズは、
## その中のテキストやオブジェクトのサイズから更にボーダー分拡張したサイズになり
## ます。
define gui.button_borders = Borders(4, 4, 4, 4)

## True に設定すると、ボタンの背景画像をスケーリングではなくタイリングで表示しま
## す。
define gui.button_tile = False

## ボタンのテキストに使用するフォント。
define gui.button_text_font = gui.interface_text_font

## ボタンのテキストのサイズ。
define gui.button_text_size = gui.interface_text_size

## 状態別のボタンのテキストのカラー。idle は選択可能、hover はフォーカス中、
## selected は選択中、insensitive は選択不可能な状態です。
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## ボタンのフレームに対する、テキストの文字揃え。 0.0 は左揃え、0.5 は中央揃え、
## 1.0 は右揃えになります。
define gui.button_text_xalign = 0.0


## 以下の変数は、様々なボタンの種類ごとにボタンの基本設定を上書きします。詳細は
## gui ドキュメンテーションを参考にしてください。
##
## デフォルトのインターフェースには、radio、check、confirm、page、quick、
## navigation、choice、slot、test、help、nvl のボタンが用意されています。radio
## と check は環境設定の各項目のボタン（デフォルトでは同じ画像）。confirm は確認
## 画面の選択肢、page は セーブ・ロード画面のページ切り替え、quick はクイックメ
## ニュー、 navigation はゲームメニューのメニュー切り替えに使うボタンです。

define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## 上記以外にも、接頭辞と接尾辞を適切に組み合わせた変数名を追加すれば、様々なカ
## スタマイズが可能になります。例えば、次の行をアンコメントすると navigation（メ
## ニュー切り替え）ボタンの横幅を指定することができます。

# define gui.navigation_button_width = 250


## Choice（選択）ボタン ###############################################################
##
## Choice ボタンは、ゲーム内の選択肢に使うボタンです。

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## File Slot（ファイルスロット）ボタン ######################################################
##
## File slot は特別なボタンで、セーブデータのサムネイル画像と詳細情報を含んでい
## ます。他のボタンと同じように gui/button ディレクトリーにある slot_ の接頭辞が
## 付いた背景画像を使います。

## File slot ボタンの設定。
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## File slot に使われるサムネイル画像の横幅と縦幅。
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## １ページあたりの File slot の列数（cols）と行数（rows）。
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## 配置と間隔 #######################################################################
##
## 以下の変数は、インターフェースの様々な要素の位置と間隔を制御します。

## 画面左端からの navigation（メニュー切り替え）ボタンの位置。
define gui.navigation_xpos = 40

## 画面上端からの skip indicator（スキップ表示）スクリーンの位置。
define gui.skip_ypos = 10

## 画面上端からの notify（通知）スクリーンの位置。
define gui.notify_ypos = 45

## ゲーム中の choice（選択）ボタンの間隔。
define gui.choice_spacing = 22

## メインメニューやゲームメニューの navigation（メニュー切り替え）ボタンの間隔。
define gui.navigation_spacing = 4

## 環境設定の各項目の間隔。
define gui.pref_spacing = 10

## 環境設定の各項目にある、各ボタンの間隔。
define gui.pref_button_spacing = 0

## セーブ・ロード画面の file page（ページ切り替え）ボタンの間隔。
define gui.page_spacing = 0

## セーブ・ロード画面の file slot（ファイルスロット）ボタン間隔。
define gui.slot_spacing = 10

## メインメニューのテキストの文字揃え。
define gui.main_menu_text_xalign = 1.0


## フレーム ########################################################################
##
## 以下の変数は、インターフェースのコンポーネントを収納するフレームを制御しま
## す。フレームは、ウィンドウやオーバーレイが用意されていない場面で使われます。

## 一般的なフレーム。デフォルトのインターフェースでは未使用です。画像は gui/
## frame.png。
define gui.frame_borders = Borders(4, 4, 4, 4)

## confirm（確認）スクリーンに使用するフレーム。画像は gui/overlay/confirm.png。
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## skip indicator（スキップ表示）スクリーンに使用するフレーム。画像は gui/
## skip.png。
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## notify（通知）スクリーンに使用するフレーム。画像は gui/notify.png。
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## True に設定すると、フレームの背景画像をスケーリングではなくタイリングで表示し
## ます。
define gui.frame_tile = False


## バー・スクロールバー・スライダー ############################################################
##
## 以下の変数は、バー・スライダー・スクロールバーの外見を制御します。
##
## デフォルトの GUI はスライダーと垂直スクロールバーだけを使用します。他のバーは
## 開発者が追加したスクリーンでのみ使われます。

## バー・スクロールバー・スライダーの各々の太さ（水平バーでは縦幅、垂直バーでは
## 横幅）。
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## True に設定すると、バーの背景をスケーリングではなくタイリングで表示します。
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## 水平バーのボーダー。画像はそれぞれ、 gui/bar/left.png 及び right.png、gui/
## slider/horizontal_**.png、gui/scrollbar/horizontal_**.png。
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## 垂直バーのボーダー。画像はそれぞれ、gui/bar/bottom.png 及び top.png、gui/
## slider/vertical_**.png、gui/scrollbar/vartical_**.png。
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## スクロール不可能なスクロールバーをどう扱うか。 "hide" なら非表示、None なら表
## 示します。
define gui.unscrollable = "hide"


## ヒストリー #######################################################################
##
## History（履歴）スクリーンは、プレイヤーが見終わった台詞を表示します。

## ヒストリーのエントリー（１台詞）を最大いくつまで保持するか。
define config.history_length = 250

## History スクリーンにおける、エントリーの高さ。None にすると可変になりますが、
## パフォーマンスが低下します。
define gui.history_height = 140

## キャラクター名の縦座標・横座標・横幅・文字揃え。
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## 台詞の縦座標・横座標・横幅・文字揃え。
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0


## NVL モード #####################################################################
##
## NVL（ノベル）スクリーンは、 NVL モード（全画面方式）のキャラクターの台詞を表
## 示するスクリーンです。

## NVL モードに使用する背景のボーダー。画像は gui/nvl.png。
define gui.nvl_borders = Borders(0, 10, 0, 20)

## NVL モードにおける、一度に表示されるエントリー（１台詞）の最大数。この値以上
## のエントリーを表示しようとすると、一番古いエントリーが取り除かれます。
define gui.nvl_list_length = 6

## NVL モードにおける、エントリー（１台詞）の高さ。None にすると可変になります。
define gui.nvl_height = 115

## NVL モードにおいて、gui.nvl_height を None に設定した場合の各エントリーの間
## 隔。また、台詞と選択肢との間隔にも使われます。
define gui.nvl_spacing = 10

## キャラクター名の縦座標・横座標・横幅・文字揃え。
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## 台詞の縦座標・横座標・横幅・文字揃え。
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## nvl_thought（モノローグ）の縦座標・横座標・横幅・文字揃え。
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## NVL モードにおける、選択肢の横座標と文字揃え。
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0


## 多言語対応 #######################################################################

## 次の変数は改行・禁則処理を制御します。デフォルトの値が推奨です。他の値は
## https://www.renpy.org/doc/html/style_properties.html#style-property-language
## を参照してください。

define gui.language = 'japanese-normal'


################################################################################
## モバイルデバイス
################################################################################

init python:

    ## タブレットやスマートフォンでタッチしやすいように、 quick ボタンのサイズを
    ## 大きくします。
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## スマートフォンで見やすいように、GUI の各要素のサイズと間隔を変更します。
    @gui.variant
    def small():

        ## フォントサイズ。
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## テキストボックスの位置を調整。
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        ## 様々なサイズとスペーシングを変更。
        gui.slider_size = 36

        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## ファイルスロットの配置。
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL モード。
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
