import pytest
import skywalker


TAG = 'PACE-980521'


@skywalker.dalek_id('PACE-980521')
@skywalker.description('Delete by three dots menu')
@pytest.mark.parametrize('some_simple_audios', [[1, 30]], indirect=True)
def pace_980521(android_connection, some_simple_audios, audios_on_teardown):
    audio_name = some_simple_audios[0]

    android_connection.audio_recorder.main.navigate()
    number_of_records = android_connection.audio_recorder.main.number_of_records()
    android_connection.audio_recorder.main.delete_audio(audio_name, cancel_deletion=True)

    assert number_of_records == android_connection.audio_recorder.main.number_of_records(), \
        'The number of records is different from the previous one'

    android_connection.audio_recorder.main.delete_audio(audio_name)

    assert not number_of_records == android_connection.audio_recorder.main.number_of_records(), \
        'The number of records remains the same of the previous one'
