import skywalker
from force.utils import ControllerNotReached


@skywalker.dalek_id('PACE-980313')
@skywalker.description('Stop after pause a Recording')
def pace_980313(android_connection, record_on_teardown):
    android_connection.launcher3.app_tray.launch_app(android_connection.audio_recorder.APP_NAME)

    android_connection.audio_recorder.main.start_record()
    try:
        android_connection.audio_recorder.recording.wait_controller()
    except ControllerNotReached:
        assert False, 'Recorder was not able to start the recording'

    android_connection.audio_recorder.recording.pause_or_resume_record()
    assert android_connection.audio_recorder.recording.is_paused(), 'Recorder was not able to pause the recording'

    android_connection.audio_recorder.recording.stop_record()
    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except ControllerNotReached:
        assert False, 'Recorder was not able to stop the recording'
