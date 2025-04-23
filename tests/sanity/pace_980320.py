import skywalker
import time

TAG = 'PACE-980320'


@skywalker.dalek_id('PACE-980320')
@skywalker.description('Delete recordings before saving')
def pace_980320(android_connection):
    android_connection.audio_recorder.main.navigate()

    number_of_recordings = android_connection.audio_recorder.main.number_of_records()

    android_connection.audio_recorder.main.start_record()
    time.sleep(5)
    android_connection.audio_recorder.recording.stop_record()
    widgets = bool(android_connection.audio_recorder.recording.save_popup.widget.tv_date_of_recording_value) \
              and bool(android_connection.audio_recorder.recording.save_popup.widget.tv_duration_value) \
              and bool(android_connection.audio_recorder.recording.save_popup.widget.tv_file_size_value)
    assert widgets, 'Widgets were not displayed correctly'
    android_connection.audio_recorder.recording.save_popup.delete()

    assert number_of_recordings == android_connection.audio_recorder.main.number_of_records(), 'The audio was not ' \
                                                                                               'deleted '
