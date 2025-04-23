import time
import skywalker
import force
import pytest

TAG = 'TSHIELDTST_14872'
@skywalker.dalek_id('TSHIELDTST_14872')
@skywalker.description('[Lock Network and Security]: Verify Lock Network Security toggle is ON by Default')
@skywalker.tags('moto_secure')
@skywalker.refactored_for_bb8_data_extraction
def TSHIELDTST_14872(test_device):
    test_device.force.log(
     f'[{TAG}]  {(test_device.settings.MOTOSECURE_TEST_1)} times')
    # precondition
    test_device.moto_settings.security.security_pin.set_security_pin('1234')

    # # iDart Step 1:.Go to Setting > Security > Screen Lock.Click on Settings icon beside Screen Lock.
    test_device.moto_settings.security.device_unlock.screen_lock_settings.navigate()

    # iDart Step 2:Verify " Lock Network and Security " is displayed and toggle is ON
    test_device.moto_settings.security.device_unlock.screen_lock_settings.navigate()

    #iDart Step 3:Verify subtext for "Lock Network and Security"
    assert test_device.moto_settings.security.device_unlock.screen_lock_settings.tv_lock_network_security, "Lock_network_and_security was not displayed"

    # iDart Step 4:Lock the screen
    test_device.input.power()

    #iDart Step 5:Pull the curtain from the Lockscreen and try to make any connection optimization or shut down or restart
    test_device.system.power.restart()





