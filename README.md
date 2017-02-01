# lsdjwavmorph
LSDj Wavetable interpolation/morphing

A simple Python script to morph one wavetable into another by interpolation

Usage: python wavmorph.py [--normalize]

The script will prompt you for 2 strings of 32 hexadecimal numbers representing the wavetables you want to morph between, e.g. from 00000000000000000000000000000000 to FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

It will then prompt for how many wave frames to interpolate across, inclusive of the first and last waveforms-- minimum is 3, maximum is 16 (default).

If the --normalize flag is present, the script will normalize each waveform.

The output is printed in the console and also to a binary file called 'wavmorph.snt' which can be patched using the patcher included in [LSDj Wave Cruncher](https://github.com/iLambda/lsdj-wave-cruncher). If the number of waves is fewer than 16, remaining waves are filled with flat values to fill up to 16 frames.
