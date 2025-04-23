import force
import pytest
import skywalker

TAG = "PACE-988882"


@skywalker.test_id("PACE-988882")
@skywalker.test_description("TC - [Audio Recorder Stress] File management")
@skywalker.test_tags("stress")
@pytest.mark.parametrize("some_simple_audios", [[TAG, 5, 5]], indirect=True)
def pace_988882(android_connection, some_simple_audios, set_storage_private, reset_keyboard, delete_audios_teardown):
    audios = android_connection.audio_recorder.main.get_available_audios()
    # iDart Step 1: Open Audio Recorder app;
    android_connection.force.log(f"[{TAG}] Open Audio Recorder app")
    android_connection.audio_recorder.main.navigate()

    # iDart Step 2: Select a recording and open it;
    android_connection.force.log(f"[{TAG}] Select a recording and open it")
    android_connection.audio_recorder.main.open_audio(audios[0])

    # iDart Step 3: Go to three dots menu and select Delete and Delete again;
    android_connection.force.log(f"[{TAG}] Go to three dots menu and select Delete and Delete again")
    android_connection.audio_recorder.playback.delete_audio()

    try:
        android_connection.audio_recorder.main.delete_audio(audios[0])
        assert False, "Audio should be deleted before"
    except force.WaitforTimeout:
        pass

    # iDart Step 4: Select another recording and open it;
    android_connection.force.log(f"[{TAG}] Select another recording and open it")
    android_connection.audio_recorder.main.open_audio(audios[1])

    # iDart Step 5: Go to three dots menu and select Rename.
    # Type a name with letters, numbers, special characters and emojis. Select Save;
    android_connection.force.log(f"[{TAG}] Go to three dots menu and select Rename."
                                  "Type a name with letters, numbers, special characters and emojis. Select Save")

    android_connection.utils.keyboard.enable_adb_keyboard()
    android_connection.audio_recorder.playback.open_rename()

    try:
        android_connection.audio_recorder.details_screen.wait_controller()
    except force.ControllerNotReached:
        assert False, "Not able to launch details screen"

    new_audio = audios[1] + " Renamed"
    android_connection.audio_recorder.details_screen.rename(new_audio)

    new_audios = android_connection.audio_recorder.main.get_available_audios()

    assert new_audio in new_audios, \
        "Should be renamed the audio"

    # iDart Step 6: Select a recording and open it;
    android_connection.force.log(f"[{TAG}] Select a recording and open it")
    android_connection.audio_recorder.main.open_audio(new_audios[0])

    # iDart Step 7: Go to three dots menu and select Details;
    android_connection.force.log(f"[{TAG}] Go to three dots menu and select Details")
    android_connection.audio_recorder.playback.open_details()

    try:
        android_connection.audio_recorder.details_screen.wait_controller()
    except force.ControllerNotReached:
        assert False, "Not able to launch details screen"

    # iDart Step 8: Come back to Audio Recorder home screen;
    android_connection.force.log(f"[{TAG}] Come back to Audio Recorder home screen")
    android_connection.audio_recorder.main.navigate()

    try:
        android_connection.audio_recorder.main.waitfor.bt_record
    except force.WaitforTimeout:
        assert False, "Record button was not displayed"
