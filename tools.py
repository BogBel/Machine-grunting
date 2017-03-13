from datetime import timedelta
import logging

from pydub import AudioSegment


def slice_by_timestamp(song, timestamp):
    return song[timestamp: timestamp+500]  # milliseconds


def get_timestamps(time_list):
    """

    :param time_list: [
    '0:07:56',
    '0:31:17',
    '0:31:36',
    '0:48:06',
    '0:48:30',
    '0:49:34',
    '0:51:53',
    '0:52:31'
    ]
    :return: generator with timestamps
    """
    for unformatted_time in time_list:
        h, m, s = map(int, unformatted_time.split(':'))
        yield timedelta(hours=h, minutes=m, seconds=s).total_seconds() * 1000  # milliseconds


def proceed_files(source, timestamps):
    song = AudioSegment.from_mp3(source)
    for ind, timestamp in enumerate(timestamps):
        grunt = slice_by_timestamp(song, timestamp)
        logging.info('grunt{}.mp3 was saved'.format(ind))
        grunt.export('sources/prepared_grunts/grunt{}.mp3'.format(ind), format="mp3")

if __name__ == '__main__':
    proceed_files(timestamps=get_timestamps([]),
                  source="sources/e1s1auto.mp3")

