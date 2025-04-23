import skywalker
from ..test_common import create_audio, play_audio
from force.utils import ControllerNotReached


TAG = 'PACE-980790'

@skywalker.dalek_id('PACE-980790')
@skywalker.description('TC - Settings - Default Quality')
def pace_980790(android_connection, record_on_teardown):
    android_connection.audio_recorder.settings.set_default_quality()

    android_connection.audio_recorder.settings.waitfor.bt_back_arrow.tap()
    try:
        android_connection.audio_recorder.main.wait_controller()
    except ControllerNotReached:
        assert False, 'After exit from settings the main screen fo audio recorder did not show up'

    audio = create_audio(android_connection, 5, 'Settings - Default Quality')

    play_audio(android_connection, 5, audio, default_widget_validation=True)
