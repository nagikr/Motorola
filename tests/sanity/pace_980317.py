import pytest
import skywalker
from force.utils import ControllerNotReached


TAG = 'PACE-980317'


@skywalker.dalek_id('PACE-980317')
@skywalker.description('TC - Selecting recordings')
@pytest.mark.parametrize('some_simple_audios', [[2, 10]], indirect=True)
def pace_980317(android_connection, some_simple_audios, audios_on_teardown):
    audio_names = some_simple_audios

    android_connection.audio_recorder.main.navigate()
    android_connection.force.log("[{}] Testing the audio named {}".format(TAG, audio_names[0]))
    android_connection.audio_recorder.main.long_tap_an_audio(audio_names[0])
    try:
        android_connection.audio_recorder.main.multiple_audios.wait_controller()
    except ControllerNotReached:
        assert False, 'Not Recorder was not able to long tap the audio'
    assert android_connection.audio_recorder.main.multiple_audios.number_of_selected_audios() == '1 selected'

    android_connection.force.log("[{}] Marking the audio named {} checkbox".format(TAG, audio_names[1]))
    android_connection.audio_recorder.main.multiple_audios.tap_audio(audio_names[1])
    assert android_connection.audio_recorder.main.multiple_audios.is_checkbox_marked(
        audio_names[1]), 'The checkbox was not marked'
    assert android_connection.audio_recorder.main.multiple_audios.number_of_selected_audios() == '2 selected'

    android_connection.force.log("[{}] Unmarking the audio named {} checkbox".format(TAG, audio_names[1]))
    android_connection.audio_recorder.main.multiple_audios.tap_audio(audio_names[1])
    assert not android_connection.audio_recorder.main.multiple_audios.is_checkbox_marked(
        audio_names[1]), 'The checkbox remain marked'
    assert android_connection.audio_recorder.main.multiple_audios.number_of_selected_audios() == '1 selected'
