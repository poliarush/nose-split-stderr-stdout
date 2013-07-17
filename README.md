= Problem = 
Nose take all output\errors and print in one defined stream.
You can't split printing if you need to split success messages to stdout and failure\errors to stderr.

= Solution = 
Implement custom TextTestRunner and TextTestResult to not give nosetest intercepts real stream.
Just need to replace it with fake one for example StringIO.

= Similar solutions =
- to capture stderr https://github.com/thkoch2001/nose/commit/c3d3dbf796eeed933b130644b259004ceae04f80 anyway, it writes all to one stream due to nature of nosetests
