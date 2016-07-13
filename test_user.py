from unittest import TestCase
from user import User


class TestSolver(TestCase):

    def test_adds_opponents_both_ways(self):
        a = User()
        b = User()

        self.assertEqual(0, a.opponents.__len__(), "done")
        self.assertEqual(0, b.opponents.__len__(), "done")

        a.add_opponent(b)

        self.assertEqual(1, a.opponents.__len__(), "done")
        self.assertEqual(1, b.opponents.__len__(), "done")

    def test_can_add_opponent(self):
        a = User()

        for number in range(0,7):
            b = User()

            self.assertTrue(a.can_add_opponent(), 'Cannot add at sume number opponents')

            a.add_opponent(b)

        self.assertTrue(a.can_add_opponent(), 'Cannot add at 7 opponents')
        self.assertEqual(7, a.opponents.__len__(), 'Does not have 7 opponents')

        c = User()
        a.add_opponent(c)

        self.assertFalse(a.can_add_opponent(), 'Can add at 8 opponents')

    def test_can_add_opponent_exceeded(self):
        a = User()

        for number in range(0,8):
            b = User()
            a.add_opponent(b)

        self.assertEqual(8, a.opponents.__len__(), 'It does not have 8 oponents')
        c = User()

        a.add_opponent(c)

        self.assertEqual(8, a.opponents.__len__(), 'It does not have 8 oponents')
        self.assertEqual(0, c.opponents.__len__(), 'It does not have 8 oponents')

        self.assertFalse(a.add_opponent(c), 'Does not return false on fail')

    def test_count_idle_opponents(self):
        a = User()

        for number in range(0, 8):
            b = User()
            a.add_opponent(b)

        self.assertEqual(0, a.count_idle_opponents(), 'Has idle opponents' )

        a.opponents[2].idle = True

        self.assertEqual(1, a.count_idle_opponents(), 'Has no idle opponents')

        for opponent in a.opponents:
            opponent.idle = True

        self.assertEqual(8, a.count_idle_opponents(), 'Has no idle opponents')

    def test_is_ready_to_leave(self):
        a = User()

        for number in range(0, 8):
            b = User()
            a.add_opponent(b)

        self.assertFalse(a.is_ready_to_leave(), 'Should stay and did not')

        for opponent in a.opponents:
            opponent.idle = True

        self.assertTrue(a.is_ready_to_leave(), 'Should be ready to leave')

    def test_cant_add_opponent_twice(self):
        a = User()
        b = User()

        a.add_opponent(b)
        self.assertEqual(1, a.opponents.__len__(), 'It should have only 1 opponent')

        a.add_opponent(b)
        self.assertEqual(1, a.opponents.__len__(), 'It should have only 1 opponent')

    def test_cant_add_opponent_itself(self):
        a = User()
        a.add_opponent(a)
        self.assertEqual(0, a.opponents.__len__(), 'It should not have any opponents')