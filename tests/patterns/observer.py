# -*- coding: utf-8 -*-

from puremvc.patterns.observer import Observer, Notification, Notifier
import unittest


class NotificationTest(unittest.TestCase):
    """NotificationTest: Test Notification Class"""

    def testEqual(self):
        """NotificationTest: test __eq__()"""
        n1 = Notification("test", body="body", type="type")
        n2 = Notification("test", body="body", type="type")

        self.assertNotEqual(id(n1), id(n2))
        self.assertEqual(n1, n2)

    def testReprAttribute(self):
        """NotificationTest: test __repr__()"""
        obj1 = object()
        obj2 = object()

        self.assertEqual(
            repr(Notification('NotificationTestNote', None)),
            "Notification Name: NotificationTestNote"
                + "\nBody:None"
                + "\nType:None"
        )
        self.assertEqual(
            repr(Notification('NotificationTestNote', 1, 2)),
            "Notification Name: NotificationTestNote"
                + "\nBody:1"
                + "\nType:2"
        )
        self.assertEqual(
            repr(Notification('NotificationTestNote', "aaa", "bbb")),
            "Notification Name: NotificationTestNote"
                + "\nBody:" + repr("aaa")
                + "\nType:" + repr("bbb")
        )
        self.assertEqual(
            repr(Notification('NotificationTestNote', obj1, obj2)),
            "Notification Name: NotificationTestNote"
                + "\nBody:" + repr(obj1)
                + "\nType:" + repr(obj2)
        )

    def testNameAccessors(self):
        """NotificationTest: Test Name Accessors"""

        note = Notification('TestNote')

        self.assertEqual(True, note.getName() == 'TestNote')

    def testBodyAccessors(self):
        """NotificationTest: Test Body Accessors"""

        note = Notification(None)
        note.setBody(5)

        self.assertEqual(True, note.getBody() == 5)

    def testConstructor(self):
        """NotificationTest: Test Constructor"""
        note = Notification('TestNote', 5, 'TestNoteType')

        self.assertEqual(True, note.getName() == 'TestNote')
        self.assertEqual(True, note.getBody() == 5)
        self.assertEqual(True, note.getType() == 'TestNoteType')


class ObserverTest(unittest.TestCase):
    """ObserverTest: Test Observer Pattern"""

    __observerTestVar = None

    def __observerTestMethod(self, note):
        self.__observerTestVar = note.getBody()

    def testObserverAccessors(self):
        """ObserverTest: Test Observer Accessors"""

        obsrvr = Observer(None, None)
        obsrvr.setNotifyContext(self)

        obsrvr.setNotifyMethod(self.__observerTestMethod)

        note = Notification('ObserverTestNote', 10)
        obsrvr.notifyObserver(note)

        self.assertEqual(True, self.__observerTestVar == 10)

    def testObserverConstructor(self):
        """ObserverTest: Test Observer Constructor"""

        obsrvr = Observer(self.__observerTestMethod, self)

        note = Notification('ObserverTestNote', 5)
        obsrvr.notifyObserver(note)

        self.assertEqual(True, self.__observerTestVar == 5)

    def testCompareNotifyContext(self):
        """ObserverTest: Test compareNotifyContext()"""

        obsrvr = Observer(self.__observerTestMethod, self)

        negTestObj = object()

        self.assertEqual(False, obsrvr.compareNotifyContext(negTestObj))
        self.assertEqual(True, obsrvr.compareNotifyContext(self))


class NotifierTest(unittest.TestCase):
    """ObserverTest: Test Observer Pattern"""

    def setUp(self):
        self.notifier = Notifier()
        self.notifier.multitonKey = "key"

    def testSendNotificationNoBodyAndType(self):
        """NotifierTest: send notification without body and type"""
        try:
            self.notifier.sendNotification("TestNotification")
        except Exception, e:  # Old-style 'except' for Python 2.5 compatibility
            self.fail(e)

    def testSendNotificationNoType(self):
        """NotifierTest: send notification without type"""
        try:
            self.notifier.sendNotification("TestNotification", 1)
        except Exception, e:  # Old-style 'except' for Python 2.5 compatibility
            self.fail(e)
