import time
import chlorian
import force
import skywalker
import pytest

TAG = 'TSHIELDTST_14823'
@skywalker.dalek_id('TSHIELDTST_14823')
@skywalker.description('- Device should be freshly flashed - Device Screen lock should be set as "PIN"')
@skywalker.tags('moto_secure')
@skywalker.refactored_for_bb8_data_extraction
def TSHIELDTST_14823(test_device):
    test_device.force.log(
       f'[{TAG}]  {(test_device.settings.MOTOSECURE_TEST_1)} times')
    # iDart Step 1:.force.log(f"[{TAG}] Go to "Settings" > Security > Device Security :Screen Lock :pin")

    test_device.moto_settings.security.device_unlock.navigate()
    time.sleep(2)

    # iDart Step 2:  Verify "PIN Scramble Layout" option below to " Screen Lock" option
    test_device. moto_settings.security.device_unlock.screen_lock_settings.navigate()
    time.sleep(2)

    # iDart Step 3:  Verify "PIN Scramble" Instruction page here "and" we are verifying text should be present or not
    assert test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble, "PIN pad Scramble was not displayed"

    time.sleep(5)

    # iDart Step 4:Lock the screen

    test_device.input.power()

    # Verify "PIN" lock digits order on Lock screen

    time.sleep(5)
    test_device.ui.unlock(1234)
    test_device.recents.clear_all_apps()




