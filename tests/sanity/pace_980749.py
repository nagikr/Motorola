import pytest
import skywalker
from force import WaitforTimeout
from ..test_common import play_audio, widget_detail_popup


TAG = 'PACE-980749'

@skywalker.dalek_id('PACE-980749')
@skywalker.description('TC - Three dots menu in the recording playback - Rename')
@pytest.mark.parametrize('some_simple_audios', [[TAG, 3, 5]], indirect=True)
def pace_980749(android_connection, some_simple_audios):
    audio = some_simple_audios[0]
    rename = 'New 1 edited 2 name! 3'
    play_audio(android_connection, 0.5, audio, default_widget_validation=True)
    widget_detail_popup(android_connection)
    android_connection.audio_recorder.playback.open_rename()
    android_connection.audio_recorder.details_screen.rename(rename)

    try:
        android_connection.audio_recorder.main.scrollto.tv_audios_(text=rename)
    except WaitforTimeout:
        assert False, 'The rename was not saved'
