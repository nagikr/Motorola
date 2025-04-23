import skywalker
import time
from force.utils import ControllerNotReached


@skywalker.dalek_id('PACE-980230')
@skywalker.description('Start a Recording')
def pace_980230(android_connection, record_on_teardown):
    android_connection.launcher3.app_tray.launch_app(android_connection.audio_recorder.APP_NAME)

    android_connection.audio_recorder.main.start_record()
    try:
        android_connection.audio_recorder.recording.wait_controller()
    except ControllerNotReached:
        assert False, 'Recorder was not able to start the recording'
    time.sleep(5)
