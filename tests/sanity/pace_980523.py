import skywalker
import force
from ..test_common import widget_detail_popup

TAG = 'PACE-980523'

@skywalker.dalek_id('PACE-980523')
@skywalker.description('TC - Cancel by three dots menu')
def pace_980523(android_connection, three_simple_audios, delete_audios_teardown):

    android_connection.audio_recorder.main.navigate()
    android_connection.audio_recorder.main.open_three_dots_menu(three_simple_audios[0])
    widget_detail_popup(android_connection)
    android_connection.audio_recorder.main.waitfor.bt_cancel_three_dots.tap()

    try:
        android_connection.audio_recorder.main.noneof.gv_bottom_sheet_grid
    except force.WaitforTimeout:
        assert False, 'The three dots menu was not dismissed'

    assert android_connection.audio_recorder.main.widget.bt_three_dots_(text=three_simple_audios[0]), 'Audio is missing!'