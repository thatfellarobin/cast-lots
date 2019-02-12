# cast-lots
This module allows you to cast lots, where the lots are ASCII sticks.
Interpretation, however, is up for interpretation.

## Usage
`from lots import Lots`

Initialize the Lots class with a certain number of lots (default 10, positive integers only)

`my_cast = Lots(20)`

Cast the lots with `Lots.cast()`. You may optionally specify a countdown in seconds, with the argument `countdown`. Default is no countdown.

`my_cast.cast(countdown=3)`

Uncast the lots (show them nice and orderly again) with `Lots.uncast()`

## Authors 
- Jacob Deery
- Robin Liu
