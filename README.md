# LSDj WAV morph
A Python script for LSDj Wavetable morphing via interpolation

![bgb.gif](bgb.gif)

Usage: python wavmorph.py [--normalize]

The script will prompt you for 2 strings of 32 hexadecimal numbers representing the wavetables you want to morph between, e.g. as shown from 7ACFEB630148999888BDC96433467767 to CCCCCCCCCCCCCCCC3333333333333333

It will then prompt for how many wave frames to interpolate across, inclusive of the first and last waveforms-- minimum is 3, maximum is 16 (default).

If the --normalize flag is present, the script will normalize each waveform.

The output is printed in the console and also to a binary file called 'wavmorph.snt' which can be patched using the wavetable import tool included in [libLSDj](https://github.com/stijnfrishert/liblsdj). If the number of waves is fewer than 16, remaining waves are filled with flat values to fill up to 16 frames.

TODO: add ability to phase and vshift waveforms
