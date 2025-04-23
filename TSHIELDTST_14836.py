import time
import skywalker
import force
import pytest

TAG = 'TSHIELDTST_14836'
@skywalker.dalek_id('TSHIELDTST_14836')
@skywalker.description('[PIN Scramble] To Verify "PIN Scramble Layout" option is enabled , after restarting the device , user entered correct pin and able to unlock the device')
@skywalker.tags('moto_secure')
@skywalker.refactored_for_bb8_data_extraction
def TSHIELDTST_14836(test_device):
    test_device.force.log(
     f'[{TAG}]  {(test_device.settings.MOTOSECURE_TEST_1)} times')
    test_device.ui.unlock(1234)

    # iDart Step 1:Go to "Settings" > Security > Device Security :Screen Lock :pin
    test_device.moto_settings.security.device_unlock.navigate()
    time.sleep(2)

    #iDart Step 2:Tap on "PIN Scramble" 'Title' and 'Icon'
    test_device.moto_settings.security.device_unlock.screen_lock_settings.enable_pin_pad_scramble()

    # iDart Step 2.1 : we are enable the Dark Theme
    test_device.moto_settings.display.enable_dark_theme()

    # iDart Step 3 : Verify "PIN Scramble" Instruction page in dark theme with animation ON
    test_device.moto_settings.security.device_unlock.screen_lock_settings.navigate()
    assert test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble, "PIN pad Scramble was not displayed"
    test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble.tap()

    # iDart Step 4 :Verify the "PIN Scramble" Instruction page in light theme with animation ON
    test_device.moto_settings.display.disable_dark_theme()

    # iDart Step: Verify the "PIN Scramble" instruction page in light theme with animation ON
    test_device.moto_settings.security.device_unlock.screen_lock_settings.navigate()
    assert test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble, "PIN pad Scramble was not displayed"
    test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble.tap()

    # iDart Step 5 :Verify the same in different font size
    test_device.moto_settings.display.font_size.change_font_size(size='Small')
    test_device.moto_settings.security.device_unlock.screen_lock_settings.navigate()
    test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble.tap()

    # iDart Step 6 : Verify the same with animation OFF
    test_device.moto_settings.security.device_unlock.screen_lock_settings.disable_pin_pad_scramble()
    test_device.moto_settings.security.device_unlock.screen_lock_settings.widget.tv_pin_pad_scramble.tap()






