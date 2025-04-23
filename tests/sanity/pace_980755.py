import skywalker
from force.utils import ControllerNotReached
from force_vision import is_screen_in_light_mode
from ..test_common import create_audio, play_audio



TAG = 'PACE-980755'

@skywalker.dalek_id('PACE-980755')
@skywalker.description('TC - Audio Recording in dark mode')
def pace_980755(android_connection, record_on_teardown, with_dark_theme):
    android_connection.audio_recorder.main.navigate()
    try:
        android_connection.audio_recorder.main.wait_controller()
    except ControllerNotReached:
        assert False, 'Audio Recorder was not launched'

    assert not is_screen_in_light_mode(android_connection), 'Recorder main screen is not on Dark Mode'
    assert android_connection.audio_recorder.main.waitfor.bt_settings, 'Settings button is not present in Dark Mode'
    assert android_connection.audio_recorder.main.waitfor.bt_record, 'Play button is not present in Dark Mode'

    android_connection.audio_recorder.main.open_settings()

    try:
        android_connection.audio_recorder.settings.wait_controller()
    except ControllerNotReached:
        assert False, 'Audio Recorder settings was not launched'

    assert not is_screen_in_light_mode(android_connection), 'Recorder settings screen is not on Dark Mode'
    audio = create_audio(android_connection, 1, 'Settings - Default Quality')
    play_audio(android_connection, 1, audio)
