import os
import time
import traceback
from pathlib import Path

import pytest
import quick_settings
from force.utils import ControllerNotReached

from .test_common import (create_long_audio, create_medium_audio,
                          create_short_audio, create_super_long_audio)

TAG = "audio_recorder_fixture"


@pytest.fixture(scope="session")
def android_connection(test_device):
    test_device.input.home()
    test_device.device.root()

    quick_settings.set_display_timeout(
        test_device.device.id(), 60000 * 30
    )  # 30 minutes

    quick_settings.grant_all_permissions(
        test_device, test_device.audio_recorder.package
    )

    test_device.device.sh(
        f"cmd notification allow_dnd {test_device.audio_recorder.package}"
    )

    test_device.system.bubble_hint.dismiss()
    test_device.recents.clear_all_apps()
    return test_device


@pytest.fixture()
def five_twenty_forty_minutes_audio(test_device):
    audio_durations = [5, 20, 40]
    audio_names = []

    for audio in audio_durations:
        test_device.audio_recorder.main.start_record()
        test_device.force.log(f"Starting a {audio} minutes recording")
        time.sleep(60 * audio)
        test_device.audio_recorder.recording.stop_record()
        test_device.audio_recorder.recording.save_popup.save_recording(
            str(audio) + " minutes audio"
        )
        test_device.force.log(f"Saved as: {audio} minutes audio")
        audio_names.append(str(audio) + " minutes audio")

    return audio_names


@pytest.fixture(scope="session")
def resources_folder():
    main_path = Path(__file__).parents[1]
    return os.path.join(main_path, "resources")


@pytest.fixture(scope="session")
def audio_folder(resources_folder):
    return os.path.join(resources_folder, "audio")


@pytest.fixture(scope="session")
def push_audio_to_device(test_device, audio_folder):
    all_audios = os.listdir(audio_folder)
    print(f"All audio files: {all_audios}")
    test_device.utils.media.push_music(
        [os.path.join(audio_folder, audio) for audio in all_audios]
    )


@pytest.fixture()
def with_secondary_user(test_device):
    test_device.force.log(f"[{TAG}] Create and setup new user")
    test_device.moto_settings.system.users.switch_to_admin()
    test_device.moto_settings.system.users.create_new_user()
    try:
        # Sometimes second user cannot connect to internet in Android Setup, let's set up Google Account later
        test_device.moto_settings.system.users.setup_new_user()
        time.sleep(30)
        test_device.input.power()
        test_device.ui.unlock()
        test_device.force.log(f"[{TAG}] Rename the new user")
        test_device.moto_settings.system.users.rename_current_user(new_name="Secondary")
        test_device.moto_settings.accounts.add_google_account(
            username=test_device.settings.GOOGLE_ACCOUNT,
            password=test_device.settings.GOOGLE_PASSWORD,
        )
    except Exception:
        traceback.print_exc()
        test_device.force.log(
            f"[{TAG}] Cannot perform secondary user setup, backing to user ..."
        )
        test_device.moto_settings.launch_settings()
        test_device.moto_settings.system.users.delete_current_user()
        raise Exception("Cannot perform secondary user setup")
    yield
    test_device.moto_settings.system.users.switch_to_admin()


@pytest.fixture()
def with_guest_user(test_device):
    test_device.moto_settings.system.users.switch_to_admin()
    test_device.moto_settings.system.users.switch_to_guest_user()
    yield
    test_device.moto_settings.system.users.switch_to_admin()


@pytest.fixture()
def set_storage_private(test_device):
    test_device.audio_recorder.settings.set_storage_private()


@pytest.fixture()
def with_dark_theme(test_device):
    test_device.moto_settings.display.enable_dark_theme()
    yield
    test_device.moto_settings.display.disable_dark_theme()


@pytest.fixture()
def some_simple_audios(test_device, request):
    """
    :param request: The request must receive a list of strings, where the first element is a differentiator for the name,
    the second is the number of audios to be created and the third is the duration of this audios
    :return: The fixture returns a list with the name of the audios created
    """
    audio_prefix, number_of_audios, audio_length = (
        request.param[0],
        request.param[1],
        request.param[2],
    )
    test_device.force.log(
        f"Creating {number_of_audios} audios with {audio_length} seconds with {audio_prefix} tag"
    )

    audio_names = []
    for _ in range(number_of_audios):
        test_device.audio_recorder.main.start_record()
        test_device.force.log(f"Starting a {audio_length} seconds recording")
        time.sleep(audio_length)
        test_device.audio_recorder.recording.stop_record()
        name = f"{audio_prefix}_{int(time.monotonic())}_{audio_length}s"

        try:
            test_device.audio_recorder.recording.save_popup.wait_controller()
            test_device.audio_recorder.recording.save_popup.save_recording(name)

        except ControllerNotReached:
            assert "Recorder save screen not reached"

        audio_names.append(name)
    return audio_names


@pytest.fixture()
def with_short_audio(android_connection):
    create_short_audio(android_connection)


@pytest.fixture()
def with_medium_audio(android_connection):
    create_medium_audio(android_connection)


@pytest.fixture()
def with_long_audio(android_connection):
    create_long_audio(android_connection)


@pytest.fixture()
def with_super_long_audio(android_connection):
    create_super_long_audio(android_connection)


@pytest.fixture()
def audios_on_teardown(test_device):
    yield
    test_device.audio_recorder.main.delete_all_audios()


@pytest.fixture()
def delete_audios_teardown(test_device):
    yield
    test_device.audio_recorder.main.navigate()
    test_device.audio_recorder.main.delete_all_audios()


@pytest.fixture()
def record_on_teardown(test_device):
    yield
    if test_device.audio_recorder.recording.is_in_screen():
        test_device.audio_recorder.recording.stop_record()
        test_device.audio_recorder.recording.save_popup.delete()
    elif test_device.audio_recorder.recording.save_popup.is_in_screen():
        test_device.audio_recorder.recording.save_popup.delete()


@pytest.fixture()
def reset_keyboard(android_connection):
    yield
    android_connection.utils.keyboard.reset_keyboard()


@pytest.fixture()
def enable_am_pm(android_connection):
    android_connection.moto_settings.system.date_time.set_24h_format_off()
    android_connection.moto_settings.system.date_time.set_locale_default_on()
