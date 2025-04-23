import skywalker
from com_motorola_audiorecorder.playback import LoopState

TAG = 'PACE-980743'

@skywalker.dalek_id('PACE-980743')
@skywalker.description('TC - Pause Recordings playback')
def pace_980743(android_connection, three_simple_audios, delete_audios_teardown):

    speeds = ['1x', '1.25x', '1.5x', '2x', '0.5x', '0.75x']
    android_connection.audio_recorder.main.navigate()
    android_connection.audio_recorder.main.open_audio(three_simple_audios[0])
    current_loop_state = LoopState.OFF
    android_connection.force.log(f'[{TAG}] Current Loop State: {current_loop_state}')
    for i in range(2):

        for index, speed in enumerate(speeds):
            android_connection.audio_recorder.playback.slide_the_progress_bar(0)
            android_connection.force.log(f'[{TAG}] Changing progress bar to: 0')
            assert android_connection.audio_recorder.playback.widget.tv_audio_speed.text() == speed, 'unexpected speed value'
            android_connection.audio_recorder.playback.start_playback()
            android_connection.force.log(f'[{TAG}] Starting playback...')
            assert android_connection.audio_recorder.playback.widget.bt_play.is_selected(), 'playback button is not on playing'
            android_connection.audio_recorder.playback.pause_playback()
            android_connection.force.log(f'[{TAG}] Pausing playback...')
            assert not android_connection.audio_recorder.playback.widget.bt_play.is_selected(), 'playback button is not on paused'
            android_connection.audio_recorder.playback.start_playback()
            android_connection.force.log(f'[{TAG}] Starting playback...')
            assert android_connection.audio_recorder.playback.widget.bt_play.is_selected(), 'playback button is not on playing'
            android_connection.audio_recorder.playback.pause_playback()
            android_connection.force.log(f'[{TAG}] Pausing playback...')

            if speed != speeds[-1]:
                android_connection.audio_recorder.playback.set_speed(speeds[index + 1])
                android_connection.force.log(f'[{TAG}] Changing speed to: {speeds[index + 1]}')
            else:
                android_connection.audio_recorder.playback.set_speed(speeds[0])
                android_connection.force.log(f'[{TAG}] Reseting speed to {speeds[0]}...')

        current_loop_state = LoopState.ON
        android_connection.audio_recorder.playback.set_loop(current_loop_state)
        android_connection.force.log(f'[{TAG}] Current Loop State: {current_loop_state}')
