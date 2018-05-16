import org.sikuli.script.*
import org.sikuli.basics.Debug

import sikuli

class Test:
    def test_capture(self):
        Debug.setDebugLevel(3)
        s = Screen
        s.find(s.userCapture().getFile()).highlight(2))
