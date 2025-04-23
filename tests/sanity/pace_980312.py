import skywalker
import datetime
from force.utils import ControllerNotReached
from ..test_common import default_without_duplicated_flag



@skywalker.dalek_id('PACE-980312')
@skywalker.description('Stop a Recording')
def pace_980312(android_connection, record_on_teardown):
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
    android_connection.audio_recorder.recording.stop_record()
    android_connection.audio_recorder.recording.save_popup.save()

    audio_name = default_without_duplicated_flag(android_connection)
    audio_name_date_format = '%A, %H.%M %p'
    try:
        audio_name = datetime.datetime.strptime(audio_name, audio_name_date_format)
    except ValueError:
        assert False, 'Default name is not following the expected format: "{}"'.format(audio_name_date_format)