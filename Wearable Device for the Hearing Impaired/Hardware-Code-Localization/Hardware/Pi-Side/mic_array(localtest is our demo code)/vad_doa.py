#

import sys
import webrtcvad
import numpy as np
from mic_array import MicArray
from pixel_ring import pixel_ring
from time import sleep

RATE = 16000
CHANNELS = 4
VAD_FRAMES = 10     # ms
DOA_FRAMES = 200    # ms


def main():
    vad = webrtcvad.Vad(3)

    speech_count = 0
    chunks = []
    doa_chunks = int(DOA_FRAMES / VAD_FRAMES)

    try:
        with MicArray(RATE, CHANNELS, RATE * VAD_FRAMES / 1000)  as mic:
            for chunk in mic.read_chunks():
                # Use single channel audio to detect voice activity
                if vad.is_speech(chunk[0::CHANNELS].tobytes(), RATE):
                    speech_count += 1
                    sys.stdout.write('')
                else:
                    sys.stdout.write('')

                sys.stdout.flush()

                chunks.append(chunk)
                if len(chunks) == doa_chunks:
                    if speech_count > (doa_chunks / 2):
                        frames = np.concatenate(chunks)
                        direction = mic.get_direction(frames)
                        pixel_ring.set_direction(direction)
                        print('\n{}'.format(int(direction)))
			if ((int(direction) >= 45) &( int(direction) <= 135)):
			    print('right')
			    sleep(0.5)
			elif ((int(direction) > 135) &( int(direction) <= 225)):
			    print('top')
                            sleep(0.5)
			elif ((int(direction) > 225) &( int(direction) <= 315)):
			    print('left')
			    sleep(0.5)
			else:# ((int(direction) > 315) &( int(direction) < 45)):
			    print('bottom')
                    	    sleep(0.5)


		    speech_count = 0
                    chunks = []

    except KeyboardInterrupt:
        pass
        
    pixel_ring.off()


if __name__ == '__main__':
    main()
