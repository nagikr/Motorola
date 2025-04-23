import pytest
import skywalker
from ..test_common import play_audio, widget_detail_popup


TAG = 'PACE-980746'

@skywalker.dalek_id('PACE-980746')
@skywalker.description('TC - Three dots menu in the recording playback')
@pytest.mark.parametrize('some_simple_audios', [[TAG, 3, 5]], indirect=True)
def pace_980746(android_connection, some_simple_audios):
    audio = some_simple_audios[0]

    play_audio(android_connection, 0.5, audio, default_widget_validation=True)
    widget_detail_popup(android_connection)
