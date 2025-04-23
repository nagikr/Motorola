import time
import chlorian
import force
import skywalker
import pytest

TAG = 'TSHIELDTST_14820'
@skywalker.dalek_id('TSHIELDTST_14820')
@skywalker.description('[PIN Scramble] To Verify "PIN Scramble Layout" instruction page with Animation "OFF" in Portrait and Landscape Mode')
@skywalker.tags('moto_secure')
@skywalker.refactored_for_bb8_data_extraction
def TSHIELDTST_14820(test_device):
    test_device.force.log(
    f'[{TAG}]  {(test_device.settings.MOTOSECURE_TEST_1)} times')
    # iDart Step 1:.force.log(f"[{TAG}] Go to "Settings" > Security > Device Security :Screen Lock :pin")
    test_device.moto_settings.security.device_unlock.navigate()
    time.sleep(2)
    test_device. moto_settings.security.device_unlock.screen_lock_settings.navigate()
    time.sleep(2)

    # iDart Step 2:  Tap on "PIN Scramble" 'Title' and 'Icon'
    assert test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble, "PIN pad Scramble was not displayed"

    test_device.moto_settings.security.device_unlock.screen_lock_settings.disable_pin_pad_scramble()

    # iDart Step 3:  Verify "PIN Scramble" Instruction page here "and" we are verifying text should be present or not

    test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble.tap()
    time.sleep(2)

    # iDart Step 4:  Verify the same in "Landscape Mode"
    test_device.ui.change_orientation_landscape()
    #iDart step : here we are checking auto rotate turn on or off
    test_device.ui.turn_on_auto_rotation()
    assert test_device.moto_settings.display.is_auto_rotate_enabled(), \
        'Auto Rotate option is not back to on'
    test_device.recents.clear_all_apps()









