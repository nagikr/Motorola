import pytest
import skywalker
from force.utils import ControllerNotReached


TAG = 'PACE-980520'


@skywalker.dalek_id('PACE-980520')
@skywalker.description('Share by three dots menu')
@pytest.mark.parametrize('some_simple_audios', [[1, 30]], indirect=True)
def pace_980520(android_connection, some_simple_audios, audios_on_teardown):
    audio_name = some_simple_audios[0]

    android_connection.audio_recorder.main.navigate()
    android_connection.audio_recorder.main.open_share(audio_name)
    try:
        android_connection.resolver_popup.wait_controller()
    except ControllerNotReached:
        assert False, 'The share button was not able to open the share screen'
