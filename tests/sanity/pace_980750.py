import pytest
import skywalker
from force.utils import ControllerNotReached
from ..test_common import play_audio


TAG = 'PACE-980750'

@skywalker.dalek_id('PACE-980750')
@skywalker.description('TC - Three dots menu in the recording playback - Rename')
@pytest.mark.parametrize('some_simple_audios', [[TAG, 3, 5]], indirect=True)
def pace_980750(android_connection, some_simple_audios):
    audio = some_simple_audios[0]
    play_audio(android_connection, 0.5, audio, default_widget_validation=True)

    android_connection.audio_recorder.playback.open_details()
    date = android_connection.audio_recorder.details_screen.get_date_of_recording()
    duration = android_connection.audio_recorder.details_screen.get_duration_of_recording()
    size = android_connection.audio_recorder.details_screen.get_size_of_recording()

    assert date, 'Date did not display on detail screen'
    assert duration, 'Duration did not display on detail screen'
    assert size, 'Size did not display on detail screen'
    try:
        android_connection.audio_recorder.details_screen.waitfor.bt_delete
    except ControllerNotReached:
        assert False, 'Delete button did not display on detail screen'
