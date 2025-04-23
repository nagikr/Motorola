import skywalker
from ..test_common import create_audio, play_audio
from force.utils import ControllerNotReached


TAG = 'PACE-980789'

@skywalker.dalek_id('PACE-980789')
@skywalker.description('TC - Settings - Low Quality')
def pace_980789(android_connection, record_on_teardown):
    android_connection.audio_recorder.settings.set_low_quality()

    android_connection.audio_recorder.settings.waitfor.bt_back_arrow.tap()
    try:
        android_connection.audio_recorder.main.wait_controller()
    except ControllerNotReached:
        assert False, 'After exit from settings the main screen fo audio recorder did not show up'

    audio = create_audio(android_connection, 5, 'Settings - Low Quality')

    play_audio(android_connection, 5, audio, default_widget_validation=True)
