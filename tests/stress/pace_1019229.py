import time

import force
import pytest
import skywalker

TAG = "PACE-1019229"


@skywalker.test_id("PACE-1019229")
@skywalker.test_description("TC - [Audio Recorder Stress] Edit function")
@skywalker.test_tags("stress")
@pytest.mark.parametrize("some_simple_audios", [[TAG, 3, 42]], indirect=True)
def pace_1019229(android_connection, some_simple_audios, set_storage_private, delete_audios_teardown):
    initial_audios = android_connection.audio_recorder.main.number_of_records()

    # iDart Step 1: Open Recorder app;
    android_connection.force.log(f"[{TAG}] Open Audio Recorder app")
    android_connection.audio_recorder.main.navigate()

    try:
        android_connection.audio_recorder.main.wait_controller()
    except force.ControllerNotReached:
        assert False, "Recorder main screen not reached"

    # iDart Step 2: Select a recording and play it;
    android_connection.force.log(f"[{TAG}] Select a recording and play it")

    android_connection.input.scroll_to_beginning(True)

    try:
        android_connection.audio_recorder.main.waitfor.tv_audios.tap()
    except force.WaitforTimeout:
        assert False, "Audio name was not reached"

    try:
        android_connection.audio_recorder.playback.wait_controller()
    except force.ControllerNotReached:
        assert "Not able to reach Playback Screen"

    android_connection.audio_recorder.playback.start_playback()

    assert (
        android_connection.audio_recorder.playback.widget.bt_play.is_selected()
    ), "Playback button is not playing"

    # iDart Step 3: Select edit option;
    android_connection.force.log(f"[{TAG}] Select edit option")
    android_connection.audio_recorder.playback.open_edit()

    try:
        android_connection.audio_recorder.edit.wait_controller()
    except force.ControllerNotReached:
        assert False, "Recorder edit screen was not reached"

    # iDart Step 4: In the graphic, shorten the recording from the left and right ends of the file;
    android_connection.force.log(f"[{TAG}] In the graphic, shorten the recording from the left and right ends of the file")
    initial_audio_length = android_connection.audio_recorder.edit.get_duration()

    android_connection.audio_recorder.edit.trim_playback_on_bottom("left", porcetage_cut=5)
    android_connection.audio_recorder.edit.trim_playback_on_bottom("right", porcetage_cut=5)

    # iDart Step 5: Select Trim;
    android_connection.force.log(f"[{TAG}] Select Trim")

    try:
        android_connection.audio_recorder.edit.waitfor.bt_trim.tap()
    except force.WaitforTimeout:
        assert False, "Trim button should be available"

    current_audio_length = android_connection.audio_recorder.edit.get_duration()

    assert (
        initial_audio_length > current_audio_length or initial_audio_length == "00:00"
    ), "Trim did not work as expected"

    # iDart Step 6: Select Save and Save again;
    if not android_connection.audio_recorder.edit.waitfor.bt_save.is_enabled():
        android_connection.force.log(f"[{TAG}] Loading still in progress")
        time.sleep(15)

    android_connection.audio_recorder.edit.save_edit()

    try:
        android_connection.audio_recorder.edit.save_popup.wait_controller(timeout=30)
    except force.ControllerNotReached:
        assert False, "The save popup did not appear after press the save button"

    try:
        android_connection.audio_recorder.edit.save_popup.waitfor.bt_save.tap()
    except force.WaitforTimeout:
        assert False, "Save button was not found on save popup"

    current_audios = android_connection.audio_recorder.main.number_of_records()
    assert initial_audios == current_audios, "After save a editing the audios was being removed or added"

    # iDart Step 7: Select a recording and play it;
    android_connection.force.log(f"[{TAG}] Select a recording and play it")

    android_connection.audio_recorder.main.open_audio(some_simple_audios[1])

    try:
        android_connection.audio_recorder.playback.wait_controller()
    except force.ControllerNotReached:
        assert "Not able to reach Playback Screen"

    android_connection.audio_recorder.playback.start_playback()

    assert (
        android_connection.audio_recorder.playback.widget.bt_play.is_selected()
    ), "Playback button is not playing"

    # iDart Step 8: Select edit option;
    android_connection.force.log(f"[{TAG}] Select edit option")
    android_connection.audio_recorder.playback.open_edit()

    try:
        android_connection.audio_recorder.edit.wait_controller()
    except force.ControllerNotReached:
        assert False, "Recorder edit screen was not reached"

    # iDart Step 9: In the graphic, shorten the recording only from the left side of the file;
    android_connection.force.log(f"[{TAG}] In the graphic, shorten the recording from the left and right ends of the file")
    initial_audio_length = android_connection.audio_recorder.edit.get_duration()

    android_connection.audio_recorder.edit.trim_playback_on_bottom("left", porcetage_cut=5)
    android_connection.audio_recorder.edit.trim_playback_on_bottom("right", porcetage_cut=5)

    # iDart Step 10: Select Trim;
    android_connection.force.log(f"[{TAG}] Select Trim")

    try:
        android_connection.audio_recorder.edit.waitfor.bt_trim.tap()
    except force.WaitforTimeout:
        assert False, "Trim button should be available"

    current_audio_length = android_connection.audio_recorder.edit.get_duration()

    assert (
        initial_audio_length > current_audio_length or initial_audio_length == "00:00"
    ), "Trim did not work as expected"

    # iDart Step 11: Select Save and Save as copy;
    if not android_connection.audio_recorder.edit.waitfor.bt_save.is_enabled():
        android_connection.force.log(f"[{TAG}] Loading still in progress")
        time.sleep(15)

    android_connection.audio_recorder.edit.save_edit()

    try:
        android_connection.audio_recorder.edit.save_popup.wait_controller(timeout=30)
    except force.ControllerNotReached:
        assert False, "The save popup did not appear after press the save button"

    try:
        android_connection.audio_recorder.edit.save_popup.waitfor.bt_copy.tap()
    except force.WaitforTimeout:
        assert False, "Save as copy button was not found on save popup"

    current_audios = android_connection.audio_recorder.main.number_of_records()
    assert initial_audios + 1 == current_audios, "After save a editing the audios was being removed or added"
