# mud-parse2D

Toying with [python-parse-2d][parse2d].

[parse2d]: https://github.com/madman-bob/python-parse-2d

Note: a [fork][parse2d-fork] of this project exists to provide a packaging of that 2D parsing library. Please use this fork as it allows importing it into the current project as a python library.

[parse2d-fork]: https://github.com/gl-yziquel/python-parse-2d


## Context

[Current code](src/mud_parse2D/__main__.py) parses the content of a 2D text box.

There  is  a  dearth  of  well structured  parsing  toolkits  for  textual  data
or  textual   programming  languages  with   a  2D  layout.  One   exception  is
`python-parse-2d`, which seems to work but may be, perhaps, too simplistic for
[our needs][needs]. So we need to check it out in some details to evaluate it.

[needs]: https://github.com/madman-bob/python-parse-2d/issues/1#issue-2337951670

Ideally, we  would like to be  able to detect two  boxes randomly laid out  on a
page. The [toody][toody] comonadic parser  combinator haskell library is claimed
to handle that,  but it does not build  out of the box anymore.  It is cursorily
discussed on [reddit][toody-reddit].

If  you  know of  other  2D  text parsing  toolkits,  please  let me  know.  The
problematics relevant to  2D parsing notably include  various markdown parsings;
such as [markdeep][markdeep] for instance.  The comonadic structure also appears
in the [ascii art to  unicode parsing technology][ascii-art-parse]. One may also
mention the [2D language Befunge][befunge] which is indeed required to parse two
dimensional text.

[toody]: https://github.com/evincarofautumn/Toody
[toody-reddit]: https://www.reddit.com/r/haskell/comments/6hjsvf/requesting_feedback_on_2d_parser_combinator/
[markdeep]: https://github.com/morgan3d/markdeep.git
[ascii-art-parse]: https://github.com/fmthoma/ascii-art-to-unicode
[befunge]: https://codeberg.org/catseye/Befunge-93

The problematic  of subtler parsing technologies  able to handle 2D  layout does
matter  inasmuch as  modern artificial  intelligence workflows  (such as  in the
txtai software) seem to hit a  bottleneck: that of preprocessing the data coming
out of ugly things  such as pdf files into something  that can be satisfactorily
consumed by these modern artificial intelligence workflows.

Incidentally, it may  be interesting to develop 2D parsing  technology to create
more modern alternatives to things like the par formatting tool.


## Build system considerations

Caveat: the project builds out of the box, provided you have the same toolkit as
me: just, fd,  par, bat / batcat, hatch,  tomlq for python yq, sed.  If you have
that, you're good to go. If you don't, leave me a note, and I'll attempt to make
my setup as portable as possible.

Type `just` for the list of commands at your disposal to manage the project.


## Not yet surveyed litterature

* Masaru  Tomita. (1989). *Parsing  2-Dimensional Language*. Proceedings  of the
First International Workshop on Parsing Technologies, 414–424.
[link](https://aclanthology.org/W89-0243)
