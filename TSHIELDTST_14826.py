import time
import skywalker
import force
import pytest

TAG = 'TSHIELDTST_14826'
@skywalker.dalek_id('TSHIELDTST_14826')
@skywalker.description('[PIN Scramble] To Verify "PIN Scramble Layout" option is enabled , after restarting the device , user entered correct pin and able to unlock the device')
@skywalker.tags('moto_secure')
@skywalker.refactored_for_bb8_data_extraction
def TSHIELDTST_14826(test_device):
    test_device.force.log(
    f'[{TAG}]  {(test_device.settings.MOTOSECURE_TEST_1)} times')
    test_device.ui.unlock(1234)
    # iDart Step 1:.force.log(f"[{TAG}] Go to "Settings" > Security > Device Security :Screen Lock :pin")

    test_device.moto_settings.security.device_unlock.navigate()
    time.sleep(2)

    # iDart Step 3:  Verify "PIN Scramble" Instruction page here and we are verifying text should be present or not
    test_device.moto_settings.security.device_unlock.screen_lock_settings.navigate()
    time.sleep(2)
    assert test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble, "PIN pad Scramble was not displayed"

    # iDart Step 3:Turn on the screen and Verify pin lock digits order in lock screen

    test_device.moto_settings.security.device_unlock.screen_lock_settings.enable_pin_pad_scramble()

    # iDart Step 4:Lock the screen

    test_device.input.power()
    time.sleep(5)

    # iDart Step 5: Enter correct pin lock number
    test_device.ui.unlock(1234)
    time.sleep(2)
    # iDart Step 6:Restart the device
    test_device.device.reboot()
    time.sleep(5)
    # iDart Step 7:Enter Incorrect PIN and verify the Device unlock
    test_device.ui.unlock(12345)

