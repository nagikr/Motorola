import pytest
import skywalker
from force import WaitforTimeout


TAG = 'PACE-980322'


@skywalker.dalek_id('PACE-980322')
@skywalker.description('Rename recordings by three dots menu')
@pytest.mark.parametrize('some_simple_audios', [[1, 30]], indirect=True)
def pace_980322(android_connection, some_simple_audios, audios_on_teardown):
    audio_name = some_simple_audios[0]

    android_connection.audio_recorder.main.navigate()
    android_connection.audio_recorder.main.open_rename(audio_name)
    renamed_audio = 'PaCe-980322 %%%$$$###@@@&&&'
    android_connection.audio_recorder.details_screen.rename(renamed_audio)

    try:
        android_connection.audio_recorder.main.open_audio(renamed_audio)
    except WaitforTimeout:
        assert False, 'Recorder was not able to find the renamed audio'
