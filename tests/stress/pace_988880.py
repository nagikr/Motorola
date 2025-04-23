import time

from datetime import datetime

import force
import skywalker


TAG = "PACE-988880"


@skywalker.test_id("PACE-988880")
@skywalker.test_description("[Audio Recorder Stress] Do several recordings")
@skywalker.test_tags("stress")
def pace_988880(android_connection, set_storage_private, delete_audios_teardown):
    one_minute = 60
    audio_name_date_format = android_connection.audio_recorder.main.audio_name_date_format

    # iDart Step 1: Open Audio Recorder app;
    android_connection.force.log(f"[{TAG}] Open Audio Recorder app")
    android_connection.audio_recorder.main.navigate()

    # iDart Step 2. Go to Settings > Quality and select the option High;
    android_connection.force.log(f"[{TAG}] Go to Settings > Quality and select the option High")
    android_connection.audio_recorder.settings.set_high_quality()

    # iDart Step 3. Come back to Audio Recorder home screen;
    android_connection.force.log(f"[{TAG}] Come back to Audio Recorder home screen")
    android_connection.audio_recorder.main.navigate()

    # iDart Step 4. Do a recording for 5 minutes. Stop and save it with the default name;
    android_connection.force.log(f"[{TAG}] [High] Starting a 5 minutes recording")

    android_connection.audio_recorder.main.start_record()

    assert android_connection.audio_recorder.recording.is_in_screen(), "Could not start the recording"

    time.sleep(5 * one_minute)

    android_connection.force.log(f"[{TAG}] [High] Stopping a 5 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] [High] Saving a 5 minutes recording")
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

    high_audio_name = android_connection.audio_recorder.playback.get_audio_name()

    try:
        datetime.strptime(high_audio_name, audio_name_date_format)
    except ValueError:
        assert False, f"{high_audio_name} is not following the format '%A, %Ih%Mm %p'"

    # iDart Step 5. Do another recording for 5 minutes. Stop and save it. Name this recording;
    android_connection.force.log(f"[{TAG}] [High] Starting a 5 minutes recording")
    android_connection.audio_recorder.main.start_record()

    try:
        android_connection.audio_recorder.recording.wait_controller()
    except force.ControllerNotReached:
        assert "Record did not start the recording"

    time.sleep(5 * one_minute)

    android_connection.force.log(f"[{TAG}] [High] Stopping a 5 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] [High] Saving a 5 minutes recording")

    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except force.ControllerNotReached:
        assert "Recorder save screen was not reached"

    android_connection.audio_recorder.recording.save_popup.save_recording("High Short Audio")

    assert "High Short Audio" in android_connection.audio_recorder.main.get_available_audios(), \
        "Should be saved a 5 minutes recording"

    # iDart Step 8. Go to Settings > Quality and select the option Low;
    android_connection.audio_recorder.settings.set_low_quality()

    # iDart Step 9. Come back to Audio Recorder home screen;
    android_connection.audio_recorder.main.navigate()

    # iDart Step 10. Do a recording for 5 minutes. Stop and save it with the default name;
    android_connection.force.log(f"[{TAG}] [Low] Starting a 5 minutes recording")

    android_connection.audio_recorder.main.start_record()

    assert android_connection.audio_recorder.recording.is_in_screen(), "Could not start the recording"

    time.sleep(5 * one_minute)

    android_connection.force.log(f"[{TAG}] [Low] Stopping a 5 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] [Low] Saving a 5 minutes recording")
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

    low_audio_name = android_connection.audio_recorder.playback.get_audio_name()

    try:
        datetime.strptime(low_audio_name, audio_name_date_format)
    except ValueError:
        assert False, f"{low_audio_name} is not following the format '%A, %Ih%Mm %p'"

    # iDart Step 11. Do another recording for 5 minutes. Stop and save it. Name this recording;
    android_connection.force.log(f"[{TAG}] [Low] Starting a 5 minutes recording")
    android_connection.audio_recorder.main.start_record()

    try:
        android_connection.audio_recorder.recording.wait_controller()
    except force.ControllerNotReached:
        assert "Record did not start the recording"

    time.sleep(5 * one_minute)

    android_connection.force.log(f"[{TAG}] [Low] Stopping a 5 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] [Low] Saving a 5 minutes recording")

    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except force.ControllerNotReached:
        assert "Recorder save screen was not reached"

    android_connection.audio_recorder.recording.save_popup.save_recording("Low Short Audio")

    assert "Low Short Audio" in android_connection.audio_recorder.main.get_available_audios(), \
        "Should be saved a 5 minutes recording"

    # iDart Step 14. Go to Settings > Quality and select the option Default;
    android_connection.audio_recorder.settings.set_default_quality()

    # iDart Step 15. Come back to Audio Recorder home screen;
    android_connection.audio_recorder.main.navigate()

    # iDart Step 16. Do a recording for 5 minutes. Stop and save it with the default name;
    android_connection.force.log(f"[{TAG}] [Default] Starting a 5 minutes recording")

    android_connection.audio_recorder.main.start_record()

    assert android_connection.audio_recorder.recording.is_in_screen(), "Could not start the recording"

    time.sleep(5 * one_minute)

    android_connection.force.log(f"[{TAG}] [Default] Stopping a 5 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] [Default] Saving a 5 minutes recording")
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

    default_audio_name = android_connection.audio_recorder.playback.get_audio_name()

    try:
        datetime.strptime(default_audio_name, audio_name_date_format)
    except ValueError:
        assert False, f"{default_audio_name} is not following the format '%A, %Ih%Mm %p'"

    # iDart Step 17. Do another recording for 5 minutes. Stop and save it. Name this recording;
    android_connection.force.log(f"[{TAG}] [Default] Starting a 5 minutes recording")
    android_connection.audio_recorder.main.start_record()

    try:
        android_connection.audio_recorder.recording.wait_controller()
    except force.ControllerNotReached:
        assert "Record did not start the recording"

    time.sleep(5 * one_minute)

    android_connection.force.log(f"[{TAG}] [Default] Stopping a 5 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] [Default] Saving a 5 minutes recording")

    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except force.ControllerNotReached:
        assert "Recorder save screen was not reached"

    android_connection.audio_recorder.recording.save_popup.save_recording("Default Short Audio")

    assert "Default Short Audio" in android_connection.audio_recorder.main.get_available_audios(), \
        "Should be saved a 5 minutes recording"
