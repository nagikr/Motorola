import pytest
import skywalker
from force.utils import ControllerNotReached
from ..test_common import play_audio, widget_detail_popup


TAG = 'PACE-980748'

@skywalker.dalek_id('PACE-980748')
@skywalker.description('TC - Three dots menu in the recording playback - Delete')
@pytest.mark.parametrize('some_simple_audios', [[TAG, 3, 5]], indirect=True)
def pace_980748(android_connection, some_simple_audios):
    audio = some_simple_audios[0]

    play_audio(android_connection, 0.5, audio, default_widget_validation=True)
    android_connection.audio_recorder.playback.open_three_dots_menu()
    widget_detail_popup(android_connection)
    android_connection.audio_recorder.playback.waitfor.bt_delete.tap()
    android_connection.audio_recorder.playback.waitfor.bt_cancel.tap()
    android_connection.audio_recorder.playback.delete_audio()

    try:
        android_connection.audio_recorder.main.wait_controller()
    except ControllerNotReached:
        assert False, 'After delete the main page did not display'
