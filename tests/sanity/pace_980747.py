import pytest
import skywalker
from force.utils import ControllerNotReached
from ..test_common import play_audio, widget_detail_popup


TAG = 'PACE-980747'

@skywalker.dalek_id('PACE-980747')
@skywalker.description('TC - Three dots menu in the recording playback - Share')
@pytest.mark.parametrize('some_simple_audios', [[TAG, 3, 5]], indirect=True)
def pace_980747(android_connection, some_simple_audios):
    audio = some_simple_audios[0]

    play_audio(android_connection, 0.5, audio, default_widget_validation=True)
    widget_detail_popup(android_connection)

    android_connection.audio_recorder.playback.open_share()
    try:
        android_connection.resolver_popup.wait_controller()
    except ControllerNotReached:
        assert False, 'After tap on the share button the popup did not appear'
