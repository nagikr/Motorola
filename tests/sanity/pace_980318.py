import pytest
import skywalker
from force.utils import ControllerNotReached


TAG = 'PACE-980318'


@skywalker.dalek_id('PACE-980318')
@skywalker.description('Share recordings by Share Icon')
@pytest.mark.parametrize('some_simple_audios', [[5, 10]], indirect=True)
def pace_980318(android_connection, some_simple_audios, audios_on_teardown):
    audio_names = some_simple_audios

    android_connection.audio_recorder.main.navigate()
    android_connection.force.log("[{}] Sharing a single audio".format(TAG))
    android_connection.audio_recorder.main.long_tap_an_audio(audio_names[0])
    android_connection.audio_recorder.main.multiple_audios.widget.bt_share.tap()
    try:
        android_connection.resolver_popup.wait_controller()
    except ControllerNotReached:
        assert False, 'Recorder was not able to open the Share Popup'

    android_connection.force.log("[{}] Sharing multiple audios".format(TAG))
    android_connection.resolver_popup.exit_screen()
    for audio_number in range(1, 5):
        android_connection.audio_recorder.main.multiple_audios.tap_audio(audio_names[audio_number])
    android_connection.audio_recorder.main.multiple_audios.widget.bt_share.tap()

    try:
        android_connection.resolver_popup.wait_controller()
    except ControllerNotReached:
        assert False, 'Recorder was not able to open the Share Popup'
