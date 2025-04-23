import time
import chlorian
import force
import skywalker
import pytest

TAG = 'TSHIELDTST_14824'
@skywalker.dalek_id('TSHIELDTST_14824')
@skywalker.description('[PIN Scramble] To Verify "PIN Scramble Layout" option is enabled , PIN lock digits appears in random order on lock screen and user is able to enter correct PIN and unlock the device')
@skywalker.tags('moto_secure')
@skywalker.refactored_for_bb8_data_extraction
def TSHIELDTST_14824(test_device):
    test_device.force.log(
    f'[{TAG}]  {(test_device.settings.MOTOSECURE_TEST_1)} times')
    # iDart Step 1:.force.log(f"[{TAG}] Go to "Settings" > Security > Device Security :Screen Lock :pin")

    test_device.moto_settings.security.device_unlock.navigate()
    time.sleep(2)

    # iDart Step 2:  Verify "PIN Scramble Layout" option below to " Screen Lock" option

    test_device. moto_settings.security.device_unlock.screen_lock_settings.navigate()
    time.sleep(2)
    assert test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble, "PIN pad Scramble was not displayed"

    # iDart Step 3:Turn on the screen and Verify pin lock digits order on lock screen

    test_device.moto_settings.security.device_unlock.screen_lock_settings.enable_pin_pad_scramble()

    # iDart Step 4:Lock the screen

    test_device.input.power()
    time.sleep(5)

    # iDart Step 5: Enter Correct pin lock number

    test_device.ui.unlock(1234)
    test_device.recents.clear_all_apps()

