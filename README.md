# mud-parse2D

Toying with [python-parse-2d][parse2d].

[parse2d]: https://github.com/madman-bob/python-parse-2d

Current code parses the content of a 2D text box.

There is  a dearth of parsing  toolkits for textual data  or textual programming
languages with  a 2D layout. One  exception is `python-parse-2d`, which  seems to
work but may be,  perhaps, too simplistic for [our needs][needs].  So we need to
check it out in some details to evaluate it.

[needs]: https://github.com/madman-bob/python-parse-2d/issues/1#issue-2337951670

Ideally, we would like to be able to detect two boxes randomly laid out on a page.

If you know of other 2D text parsing toolkits, please let me know.

Caveat: the project builds out of the box, provided you have the same toolkit as
me: just, fd,  par, bat / batcat, hatch,  tomlq for python yq, sed.  If you have
that, you're good to go. If you don't, leave me a note, and I'll attempt to make
my setup as portable as possible.

Type `just` for the list of commands at your disposal to manage the project.
