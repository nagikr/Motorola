import time

import force
import pytest
import skywalker
import setup_utils
import quick_settings

TAG = "PACE-1385234"


@pytest.fixture(scope="session")
def pace_1385234_setup(test_device):
    products = ["motorola razr 50", "motorola razr 50 ultra", "motorola edge 50 ultra"]

    if test_device.device.product() in products:
        setup_utils.configure_wifi(test_device)
        if not quick_settings.get_account(test_device, "Moto Account"):
            test_device.moto_settings.accounts.open_add_account()
            test_device.moto_settings.accounts.add_account.tap_moto_account()
            test_device.moto_account.sign_in.signin(
                test_device.settings.GOOGLE_ACCOUNT, test_device.settings.GOOGLE_PASSWORD
            )
            if test_device.save_to_google.is_in_screen():
                test_device.save_to_google.exit_screen()
    else:
        pytest.skip("This TC is applicable for only Aura, Glory and Velar devices")


@skywalker.test_id("PACE-1385234")
@skywalker.test_description("Verify and transcription and Summarization functionality during stress")
@skywalker.test_tags("stress")
@pytest.mark.repeat(100)
def pace_1385234(pace_1385234_setup, android_connection, delete_audios_teardown):
    one_minute = 60
    # iDart Step 1: Open recorder
    # iDart Step 2: Give all permission for recorder app
    # iDart Step 3: Enable DND for recorder app
    android_connection.force.log(
        f"[{TAG}] Open recorder > Give all permission for recorder app > Enable DND for recorder app"
    )

    android_connection.audio_recorder.main.navigate()

    # iDart Step 4: Play an English podcast from Reference device and record the audio
    android_connection.force.log(f"[{TAG}] Play an English podcast from Reference device and record the audio")

    # iDart Step 5: Stop the recording after 5 mins and tap on transcribe button
    android_connection.force.log(f"[{TAG}] Stop the recording after 5 mins and tap on transcribe button")

    initial_audios = android_connection.audio_recorder.main.number_of_records()

    android_connection.audio_recorder.main.start_record()
    time.sleep(5 * one_minute)
    android_connection.audio_recorder.recording.stop_record()

    android_connection.audio_recorder.recording.save_popup.save()

    # iDart Step 6: Open Transcribed file and again tap on Summary tab
    android_connection.force.log(f"[{TAG}] Open Transcribed file and again tap on Summary tab")

    current_audios = android_connection.audio_recorder.main.number_of_records()

    assert initial_audios + 1 == current_audios, "The recording was not saved"

    android_connection.input.scroll_to_beginning(True)

    try:
        android_connection.audio_recorder.main.waitfor.tv_audios.tap()
    except force.WaitforTimeout:
        assert False, "Audio name was not reached"

    try:
        android_connection.audio_recorder.playback.wait_controller()
    except force.ControllerNotReached:
        assert "Not able to reach Playback Screen"

    android_connection.force.log(f"[{TAG}] Transcribing in progress")

    try:
        android_connection.force.noneof(text='Transcribing...', timeout=60)
    except force.WaitforTimeout:
        assert False, "Transcription took more than 60 seconds"

    android_connection.force.log(f"[{TAG}] Tap on Summary")

    try:
        android_connection.audio_recorder.playback.waitfor.tv_summary_tab_(timeout=30).tap()
    except force.WaitforTimeout:
        android_connection.force.log(f"[{TAG}] Summary tab was not displayed > Tap on transcription")

        try:
            android_connection.audio_recorder.playback.waitfor.tv_transcription_(timeout=30).tap()
        except force.WaitforTimeout:
            android_connection.force.log(f"[{TAG}] Transcription button was not displayed")

        try:
            android_connection.force.noneof(text='Transcribing...', timeout=60)
        except force.WaitforTimeout:
            assert False, "Transcription took more than 60 seconds"

        try:
            android_connection.audio_recorder.playback.waitfor.tv_summary_tab_(timeout=30).tap()
        except force.WaitforTimeout:
            assert False, "Summary tab was not displayed"

    # iDart Step 7: Tap on generate Summary
    android_connection.force.log(f"[{TAG}] Tap on generate Summary")

    try:
        android_connection.audio_recorder.playback.waitfor.bt_generate_(timeout=30).tap()
    except force.WaitforTimeout:
        assert False, "Generate button was not displayed"

    # iDart Step 8: Wait until summary is generated
    android_connection.force.log(f"[{TAG}] Wait until summary is generated")

    try:
        summary_content = android_connection.audio_recorder.playback.waitfor.tv_summarization_content_(timeout=30)
        assert summary_content and summary_content.text(), "Summary content was not generated"
    except force.WaitforTimeout:
        assert False, "Summary content was not displayed"
