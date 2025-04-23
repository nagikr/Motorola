import skywalker
import time
import datetime
from force.utils import ControllerNotReached


@skywalker.dalek_id('PACE-980315')
@skywalker.description('Saving a recording without a name')
def pace_980315(android_connection, record_on_teardown):
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

    time.sleep(5)
    android_connection.audio_recorder.recording.stop_record()
    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except ControllerNotReached:
        assert False, 'Recorder was not able to stop the recording'

    date_of_recording = android_connection.audio_recorder.recording.save_popup.get_date_of_recording().split(" ")
    hour_of_recording = date_of_recording[4:6]
    day_of_recording = datetime.datetime.today().strftime("%A")
    android_connection.audio_recorder.recording.save_popup.save()

    android_connection.audio_recorder.main.widget.tv_audios.tap()
    audio_name = android_connection.audio_recorder.playback.get_audio_name()

    hour = (hour_of_recording[0].replace(":", ".") in audio_name) and (hour_of_recording[1] in audio_name)
    assert hour, 'Default name do not match with the correct hour of recording: "{}"'.format(hour_of_recording)

    day = day_of_recording in audio_name
    assert day, 'Default name do not match with the correct day of recording: "{}"'.format(day_of_recording)

    audio_name_date_format = '%A, %H.%M %p'
    try:
        audio_name = datetime.datetime.strptime(audio_name, audio_name_date_format)
    except ValueError:
        assert False, 'Default name is not following the expected format: "{}"'.format(audio_name_date_format)
