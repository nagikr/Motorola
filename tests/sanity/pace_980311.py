import skywalker
from force.utils import ControllerNotReached


@skywalker.dalek_id('PACE-980311')
@skywalker.description('Pause a Recording')
def pace_980311(android_connection, record_on_teardown):
    android_connection.launcher3.app_tray.launch_app(android_connection.audio_recorder.APP_NAME)
    try:
        android_connection.audio_recorder.main.wait_controller()
    except ControllerNotReached:
        assert False, 'Audio Recorder was not launched'

    android_connection.audio_recorder.main.start_record()
    try:
        android_connection.audio_recorder.recording.wait_controller()
    except ControllerNotReached:
        assert False, 'Recorder was not able to start the recording'

    android_connection.audio_recorder.recording.pause_or_resume_record()
    assert android_connection.audio_recorder.recording.is_paused(), 'Recorder was not able to pause the recording'

    android_connection.audio_recorder.recording.pause_or_resume_record()
    assert not android_connection.audio_recorder.recording.is_paused(), 'Recorder was not able to resume the recording'
