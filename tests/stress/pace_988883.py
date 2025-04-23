import time

from datetime import datetime

import force
import skywalker

TAG = "PACE-988883"


@skywalker.test_id("PACE-988883")
@skywalker.test_description("TC - [Audio Recorder Stress] Super long recording")
@skywalker.test_tags("stress")
def pace_988883(android_connection, enable_am_pm, set_storage_private, delete_audios_teardown):
    one_minute = 60
    number_of_time_changes = 10
    audio_name_date_format = android_connection.audio_recorder.main.audio_name_date_format

    # iDart Step 1: Open Audio Recorder app;
    android_connection.force.log(f"[{TAG}] Open Audio Recorder app")
    android_connection.audio_recorder.main.navigate()

    # iDart Step 2: Go to Settings > Quality and select the option High;
    android_connection.force.log(f"[{TAG}] Go to Settings > Quality and select the option High")

    android_connection.audio_recorder.main.open_settings()
    android_connection.audio_recorder.settings.set_high_quality()

    assert "High" in android_connection.audio_recorder.settings.get_quality(), "Could not set high quality"

    # iDart Step 3: Come back to Audio Recorder home screen;
    android_connection.force.log(f"[{TAG}] Come back to Audio Recorder home screen")
    android_connection.audio_recorder.main.navigate()

    # iDart Step 4: Do a recording for 60 minutes. Stop and save it with the default name;
    android_connection.force.log(f"[{TAG}] Do a recording for 60 minutes. Stop and save it with the default name")
    android_connection.audio_recorder.main.start_record()

    assert android_connection.audio_recorder.recording.is_in_screen(), "Could not start the recording"

    time.sleep(60 * one_minute)

    android_connection.force.log(f"[{TAG}] Stopping a 60 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] Saving a 60 minutes recording")
    android_connection.audio_recorder.recording.save_popup.save()

    try:
        android_connection.audio_recorder.main.wait_controller()
    except force.ControllerNotReached:
        assert False, "Recorder main screen not reached"

    android_connection.input.scroll_to_beginning(True)

    try:
        android_connection.audio_recorder.main.waitfor.tv_audios.tap()
    except force.WaitforTimeout:
        assert False, "Audio name was not reached"

    try:
        android_connection.audio_recorder.playback.wait_controller()
    except force.ControllerNotReached:
        assert "Not able to reach Playback Screen"

    default_name = android_connection.audio_recorder.playback.get_audio_name()

    try:
        datetime.strptime(default_name, audio_name_date_format)
    except ValueError:
        assert False, f"{default_name} is not following the format '%A, %Ih%Mm %p'"

    # iDart Step 5: Select the recording that was made in the step 4 and play it.
    android_connection.force.log(f"[{TAG}] Select the recording that was made in the step 4 and play it")
    android_connection.audio_recorder.playback.start_playback()

    # iDart Step 6: After 10 minutes of playback, do 10 fast fowards by the time range.
    android_connection.force.log(f"[{TAG}] After 10 minutes of playback, do 10 fast fowards by the time range")

    time.sleep(10 * one_minute)

    for tap in range(number_of_time_changes):
        android_connection.audio_recorder.playback.tap_forward()

    # iDart Step 7: Wait more 10 minutes and do 10 rewinds by the time range.
    android_connection.force.log(f"[{TAG}] Wait more 10 minutes and do 10 rewinds by the time range")

    time.sleep(10 * one_minute)

    for tap in range(number_of_time_changes):
        android_connection.audio_recorder.playback.tap_backward()
