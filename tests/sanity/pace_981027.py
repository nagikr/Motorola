import time
import pytest
import skywalker
from force import WaitforTimeout

TAG = 'PACE-981027'


@skywalker.dalek_id('PACE-981027')
@skywalker.description('Search recordings')
@pytest.mark.parametrize('some_simple_audios', [[6, 3]], indirect=True)
def pace_981027(android_connection, some_simple_audios, record_on_teardown):
    android_connection.audio_recorder.main.navigate()
    android_connection.force.log("[{}] Recording a 5 seconds audio".format(TAG))
    android_connection.audio_recorder.main.start_record()
    time.sleep(5)
    android_connection.audio_recorder.recording.stop_record()

    audio_name = "Find This Recording"
    android_connection.force.log("[{}] Saving the recording that will be search as {}".format(TAG, audio_name))
    android_connection.audio_recorder.recording.save_popup.save_recording(audio_name)

    android_connection.audio_recorder.main.search_record(audio_name, tap_audio=False)
    assert len(android_connection.audio_recorder.main.widgets.tv_audios) == 1, 'No audio found with this name'
    time.sleep(3)
    android_connection.utils.keyboard.close()

    android_connection.force.log("[{}] Searching for No Audio With This Name".format(TAG))
    try:
        android_connection.audio_recorder.main.search_record("No Audio With This Name")
        android_connection.audio_recorder.playback.exit_screen()
        assert False, 'No audio should be found with this name'
    except WaitforTimeout:
        assert True
    time.sleep(3)
    android_connection.utils.keyboard.close()
