import time

import force
from force.utils import ControllerNotReached

TAG = "audio_recorder_common"


def create_audio(android_connection, length, name=None):
    android_connection.force.log(f"[{TAG}] Starting a {length} minutes recording")
    android_connection.audio_recorder.main.start_record()

    assert (
        android_connection.audio_recorder.recording.is_in_screen()
    ), "Could not start the recording"
    time.sleep(60 * length)

    android_connection.force.log(f"[{TAG}] Stopping a {length} minutes recording")
    android_connection.audio_recorder.recording.stop_record()

    if name:
        android_connection.force.log(f"[{TAG}] Saving a {length} minutes recording")
        android_connection.audio_recorder.recording.save_popup.save_recording(name)
        android_connection.force.log(f"Saved as: {name}")
        return name
    else:
        android_connection.force.log(f"[{TAG}] Saving a {length} minutes recording")
        android_connection.audio_recorder.recording.save_popup.save()
        try:
            android_connection.audio_recorder.main.wait_controller()
            android_connection.audio_recorder.main.waitfor.tv_audios.tap()
        except ControllerNotReached:
            assert "Recorder main screen not reached"

        try:
            android_connection.audio_recorder.playback.wait_controller()
        except ControllerNotReached:
            assert "Not able to reach Playback Screen"
        return android_connection.audio_recorder.playback.get_audio_name()


def play_audio(android_connection, length, audio_name, default_widget_validation=False):
    android_connection.force.log(f"[{TAG}] Playing {audio_name} recording")

    android_connection.audio_recorder.main.navigate()
    android_connection.audio_recorder.main.open_audio(audio_name)

    time.sleep(5)
    assert android_connection.audio_recorder.playback.is_audio_open(
        audio_name
    ), "The selected audio could not be opened"
    if default_widget_validation:
        assert (
            android_connection.audio_recorder.playback.widget.bt_play
        ), "Play button should be on display"
        assert (
            android_connection.audio_recorder.playback.widget.bt_forward
        ), "Forward button should be on display"
        assert (
            android_connection.audio_recorder.playback.widget.bt_backward
        ), "Backward button should be on display"
        assert (
            android_connection.audio_recorder.playback.widget.tv_audio_speed.text
            == "1x"
        ), "Audio speed button is not on default value"

    android_connection.audio_recorder.playback.start_playback()
    android_connection.force.log(f"Starting a {length} minutes playback")
    time.sleep(60 * length + 5)
    return True


def play_with_specs(android_connection, audio_name, length, loop, repetitions, speed):
    android_connection.audio_recorder.main.navigate()
    android_connection.audio_recorder.main.open_audio(audio_name)

    time.sleep(5)
    assert android_connection.audio_recorder.playback.is_audio_open(
        audio_name
    ), "The selected audio could not be opened"
    android_connection.audio_recorder.playback.set_loop(loop)
    android_connection.audio_recorder.playback.set_speed(speed)

    numerical_speed = speed[:-1]
    length = length / float(numerical_speed)

    android_connection.force.log(
        f"Starting a {length} playback, at {speed} speed, {repetitions} time(s)"
    )
    android_connection.audio_recorder.playback.start_playback()
    for i in range(repetitions):
        android_connection.force.log(f"{i + 1} of {repetitions}")
        time.sleep(60 * length + 10)

    android_connection.audio_recorder.playback.set_speed("1x")
    android_connection.input.back()


def default_without_duplicated_flag(android_connection):
    android_connection.audio_recorder.main.widget.tv_audios.tap()
    audio_name = android_connection.audio_recorder.playback.get_audio_name()
    audio_name = audio_name.replace(" (1)", "")

    return audio_name


def create_short_audio(android_connection, create_new=False):
    short_audio_name = android_connection.settings.SHORT_AUDIO_NAME
    short_audio_length = android_connection.settings.SHORT_AUDIO_LENGTH
    audio_exists = android_connection.audio_recorder.main.is_audio_in_audio_list(
        short_audio_name
    )

    if audio_exists:
        android_connection.force.log(f"{short_audio_name} already exists")
        if create_new:
            android_connection.force.log("Deleting audio to create a new one")
            android_connection.audio_recorder.main.delete_audio(short_audio_name)

            android_connection.force.log("Creating the new audio")
            return create_audio(android_connection, short_audio_length, short_audio_name)
    else:
        android_connection.force.log(
            f"{short_audio_name} does not exists, creating the audio"
        )
        return create_audio(android_connection, short_audio_length, short_audio_name)


def create_medium_audio(android_connection, create_new=False):
    medium_audio_name = android_connection.settings.MEDIUM_AUDIO_NAME
    medium_audio_length = android_connection.settings.MEDIUM_AUDIO_LENGTH
    audio_exists = android_connection.audio_recorder.main.is_audio_in_audio_list(
        medium_audio_name
    )

    if audio_exists:
        android_connection.force.log(f"{medium_audio_name} already exists")
        if create_new:
            android_connection.force.log("Deleting audio to create a new one")
            android_connection.audio_recorder.main.delete_audio(medium_audio_name)

            android_connection.force.log("Creating the new audio")
            return create_audio(android_connection, medium_audio_length, medium_audio_name)
    else:
        android_connection.force.log(
            f"{medium_audio_name} does not exists, creating the audio"
        )
        return create_audio(android_connection, medium_audio_length, medium_audio_name)


def create_long_audio(android_connection, create_new=False):
    long_audio_name = android_connection.settings.LONG_AUDIO_NAME
    long_audio_length = android_connection.settings.LONG_AUDIO_LENGTH
    audio_exists = android_connection.audio_recorder.main.is_audio_in_audio_list(
        long_audio_name
    )

    if audio_exists:
        android_connection.force.log(f"{long_audio_name} already exists")
        if create_new:
            android_connection.force.log("Deleting audio to create a new one")
            android_connection.audio_recorder.main.delete_audio(long_audio_name)

            android_connection.force.log("Creating the new audio")
            return create_audio(android_connection, long_audio_length, long_audio_name)
    else:
        android_connection.force.log(
            f"{long_audio_name} does not exists, creating the audio"
        )
        return create_audio(android_connection, long_audio_length, long_audio_name)


def create_super_long_audio(android_connection, create_new=False):
    super_long_audio_name = android_connection.settings.SUPER_LONG_AUDIO_NAME
    super_long_audio_length = android_connection.settings.SUPER_LONG_AUDIO_LENGTH
    audio_exists = android_connection.audio_recorder.main.is_audio_in_audio_list(
        super_long_audio_name
    )

    if audio_exists:
        android_connection.force.log(f"{super_long_audio_name} already exists")
        if create_new:
            android_connection.force.log("Deleting audio to create a new one")
            android_connection.audio_recorder.main.delete_audio(super_long_audio_name)

            android_connection.force.log("Creating the new audio")
            return create_audio(android_connection, super_long_audio_length, super_long_audio_name)
    else:
        android_connection.force.log(
            f"{super_long_audio_name} does not exists, creating the audio"
        )
        return create_audio(android_connection, super_long_audio_length, super_long_audio_name)


def widget_detail_popup(android_connection):
    try:
        android_connection.audio_recorder.playback.waitfor.bt_share_()
        android_connection.audio_recorder.playback.waitfor.bt_delete_()
        android_connection.audio_recorder.playback.waitfor.bt_rename_()
        android_connection.audio_recorder.playback.waitfor.bt_details_()
        android_connection.audio_recorder.playback.waitfor.bt_cancel_()
    except force.WaitforTimeout:
        assert False, "Detail Popup buttons did not appeared on the screen correctly"
