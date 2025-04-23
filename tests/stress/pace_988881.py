import time

import force
import skywalker

from com_motorola_audiorecorder.playback import LoopState

TAG = "PACE-988881"


@skywalker.test_id("PACE-988881")
@skywalker.test_description("[Audio Recorder Stress] Playback recordings")
@skywalker.test_tags("stress")
def pace_988881(android_connection, set_storage_private, delete_audios_teardown):
    one_minute = 60
    # iDart Step 1: Open Audio Recorder app;
    android_connection.force.log(f"[{TAG}] Open Audio Recorder app")
    android_connection.audio_recorder.main.navigate()

    # iDart Step 2: Select a short recording (15 minutes) and play it;
    android_connection.force.log(f"[{TAG}] Starting a 15 minutes recording")
    android_connection.audio_recorder.main.start_record()

    try:
        android_connection.audio_recorder.recording.wait_controller()
    except force.ControllerNotReached:
        assert "Record did not start the recording"

    time.sleep(15 * one_minute)

    android_connection.force.log(f"[{TAG}] Stopping a 15 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] Saving a 15 minutes recording")

    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except force.ControllerNotReached:
        assert "Recorder save screen was not reached"

    short_audio = "Short Audio"
    android_connection.audio_recorder.recording.save_popup.save_recording(short_audio)

    android_connection.force.log(f"[{TAG}] Select a short recording (15 minutes) and play it")
    android_connection.audio_recorder.main.open_audio(short_audio)

    # iDart Step 3: Select a long recording (45 minutes) and play it;
    android_connection.force.log(f"[{TAG}] Starting a 45 minutes recording")
    android_connection.audio_recorder.main.start_record()

    try:
        android_connection.audio_recorder.recording.wait_controller()
    except force.ControllerNotReached:
        assert "Record did not start the recording"

    time.sleep(45 * one_minute)

    android_connection.force.log(f"[{TAG}] Stopping a 45 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] Saving a 45 minutes recording")

    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except force.ControllerNotReached:
        assert "Recorder save screen was not reached"

    long_audio = "Long Audio"
    android_connection.audio_recorder.recording.save_popup.save_recording(long_audio)

    android_connection.force.log(f"[{TAG}] Select a long recording (45 minutes) and play it;")
    android_connection.audio_recorder.main.open_audio(long_audio)

    # iDart Step 4: Select a short recording (15 minutes) and play it with the loop icon enabled one time. Let it play 3 times;
    android_connection.force.log(f"[{TAG}] Select a short recording (15 minutes) and play it with the loop icon enabled one time. Let it play 3 times;")

    android_connection.audio_recorder.main.open_audio(short_audio)
    android_connection.audio_recorder.playback.start_playback()
    android_connection.audio_recorder.playback.set_loop(LoopState.ON)

    duration = 3 * 15 * one_minute
    start_time = time.time()

    while time.time() - start_time < duration:
        ...

    # iDart Step 5: Select a medium recording (30 minutes) and play it with the loop icon enabled twice. Let it play twice;
    android_connection.force.log(f"[{TAG}] Starting a 30 minutes recording")
    android_connection.audio_recorder.main.start_record()

    try:
        android_connection.audio_recorder.recording.wait_controller()
    except force.ControllerNotReached:
        assert "Record did not start the recording"

    time.sleep(30 * one_minute)

    android_connection.force.log(f"[{TAG}] Stopping a 30 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] Saving a 30 minutes recording")

    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except force.ControllerNotReached:
        assert "Recorder save screen was not reached"

    medium_audio = "Medium Audio"
    android_connection.audio_recorder.recording.save_popup.save_recording(medium_audio)

    android_connection.force.log(f"[{TAG}] Select a medium recording (30 minutes) and play it with the loop icon enabled twice. Let it play twice")

    android_connection.audio_recorder.main.open_audio(medium_audio)
    android_connection.audio_recorder.playback.start_playback()
    android_connection.audio_recorder.playback.set_loop(LoopState.ON)

    duration = 2 * 30 * one_minute
    start_time = time.time()

    while time.time() - start_time < duration:
        ...

    # iDart Step 6: Select a super long recording (60 minutes) and play it in the speed 2X.
    android_connection.force.log(f"[{TAG}] Starting a 60 minutes recording")
    android_connection.audio_recorder.main.start_record()

    try:
        android_connection.audio_recorder.recording.wait_controller()
    except force.ControllerNotReached:
        assert "Record did not start the recording"

    time.sleep(60 * one_minute)

    android_connection.force.log(f"[{TAG}] Stopping a 30 minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    android_connection.force.log(f"[{TAG}] Saving a 30 minutes recording")

    try:
        android_connection.audio_recorder.recording.save_popup.wait_controller()
    except force.ControllerNotReached:
        assert "Recorder save screen was not reached"

    super_long_audio = "Super Long Audio"
    android_connection.audio_recorder.recording.save_popup.save_recording(super_long_audio)

    android_connection.force.log(f"[{TAG}] Select a super long recording (60 minutes) and play it in the speed 2X")
    android_connection.audio_recorder.main.open_audio(super_long_audio)

    android_connection.audio_recorder.playback.start_playback()
    android_connection.audio_recorder.playback.set_speed("2x")

    time.sleep(60 * one_minute)

    # iDart Step 7: Select a medium recording (30 minutes) and play it in the speed 0,75X.
    android_connection.audio_recorder.main.open_audio(medium_audio)

    android_connection.audio_recorder.playback.start_playback()
    android_connection.audio_recorder.playback.set_speed("0.75x")

    time.sleep(30 * one_minute)

    # iDart Step 8: Select a super long recording (60 minutes) and play it in the default speed.
    # After 5 minutes, fast foward the playback by the time range twice.
    # Wait 1 minute. Fast foward by the time range again.
    # Wait 2 minutes. Fast foward by time range 3 times.
    # Wait 5 minutes. Rewind the playback by the time range twice.
    # Wait 1 minute. Rewind by the time range again.
    # Wait 2 minutes. Rewind by time range 3 times.
    android_connection.audio_recorder.main.open_audio(super_long_audio)

    android_connection.audio_recorder.playback.start_playback()
    android_connection.audio_recorder.playback.set_speed("1x")

    for direction in ["forward", "backward"]:
        for sleep, amount_of_times in [(5 * one_minute, 2), (one_minute, 1), (2 * one_minute, 3)]:
            time.sleep(sleep)
            android_connection.audio_recorder.playback.move_by_the_time_range(
                direction=direction, amount_of_times=amount_of_times
            )
