import unittest
import math

import ppb_vector

def epsilon(decimal):
    return round(decimal, 5)

def assertEpsilonEqual(self, a, b):
    return self.assertEqual(epsilon(a), epsilon(b))
    
class TestIterable(unittest.TestCase):

    def test_is_iterable(self):
        test_vector = ppb_vector.Vector2(3, 4)
        test_tuple = tuple(test_vector)
        self.assertEqual(test_tuple[0], 3)
        self.assertEqual(test_tuple[1], 4)

    def test_normalize(self):
        test_vector = ppb_vector.Vector2(3, 4)
        test_vector = test_vector.normalize()
        assertEpsilonEqual(self, test_vector.x, 3 / 5)
        assertEpsilonEqual(self, test_vector.y, 4 / 5)
        
        test_vector = ppb_vector.Vector2(5, 12)
        test_vector = test_vector.normalize()
        assertEpsilonEqual(self, test_vector.x, 5 / 13)
        assertEpsilonEqual(self, test_vector.y, 12 / 13)
        
        test_vector = ppb_vector.Vector2(8, 15)
        test_vector = test_vector.normalize()
        assertEpsilonEqual(self, test_vector.x, 8 / 17)
        assertEpsilonEqual(self, test_vector.y, 15 / 17)
        
        test_vector = ppb_vector.Vector2(7, 24)
        test_vector = test_vector.normalize()
        assertEpsilonEqual(self, test_vector.x, 7 / 25)
        assertEpsilonEqual(self, test_vector.y, 24 / 25)
        
    def test_length(self):
        test_vector = ppb_vector.Vector2(3, 4)
        test_length = test_vector.length
        assertEpsilonEqual(self, test_length, 5)
        
        test_vector = ppb_vector.Vector2(5, 12)
        test_length = test_vector.length
        assertEpsilonEqual(self, test_length, 13)
        
        test_vector = ppb_vector.Vector2(8, 15)
        test_length = test_vector.length
        assertEpsilonEqual(self, test_length, 17)
        
        test_vector = ppb_vector.Vector2(7, 24)
        test_length = test_vector.length
        assertEpsilonEqual(self, test_length, 25)
    
    def test_scale(self):
        test_vector = ppb_vector.Vector2(3, 4)
        test_vector = test_vector.scale(1)
        assertEpsilonEqual(self, test_vector.x, 3 / 5)
        assertEpsilonEqual(self, test_vector.y, 4 / 5)
        
        test_vector = test_vector.scale(2)
        assertEpsilonEqual(self, test_vector.x, 6 / 5)
        assertEpsilonEqual(self, test_vector.y, 8 / 5)
        
        test_vector = test_vector.scale(3)
        assertEpsilonEqual(self, test_vector.x, 9 / 5)
        assertEpsilonEqual(self, test_vector.y, 12 / 5)
        
        test_vector = test_vector.scale(4)
        assertEpsilonEqual(self, test_vector.x, 12 / 5)
        assertEpsilonEqual(self, test_vector.y, 16 / 5)
        
    def test_rotate(self):
        orig_vector = ppb_vector.Vector2(3, 4)
        test_vector = orig_vector.rotate(45)
        assertEpsilonEqual(self, test_vector.x, -0.70711)
        assertEpsilonEqual(self, test_vector.y, 4.94975)
        
        test_vector = orig_vector.rotate(90)
        assertEpsilonEqual(self, test_vector.x, -4)
        assertEpsilonEqual(self, test_vector.y, 3)
        
        test_vector = orig_vector.rotate(135)
        assertEpsilonEqual(self, test_vector.x, -4.94975)
        assertEpsilonEqual(self, test_vector.y, -0.70711)
        
        test_vector = orig_vector.rotate(180)
        assertEpsilonEqual(self, test_vector.x, -3)
        assertEpsilonEqual(self, test_vector.y, -4)
        
    def test_index(self):
        test_vector = ppb_vector.Vector2(3, 4)
        assertEpsilonEqual(self, test_vector.x, 3)
        assertEpsilonEqual(self, test_vector.y, 4)
        
        assertEpsilonEqual(self, test_vector[0], 3)
        assertEpsilonEqual(self, test_vector[1], 4)
        
        assertEpsilonEqual(self, test_vector["x"], 3)
        assertEpsilonEqual(self, test_vector["y"], 4)
        
    def test_truncate(self):
        orig_vector = ppb_vector.Vector2(3, 4)
        test_vector = orig_vector.truncate(1)
        assertEpsilonEqual(self, test_vector.x, 3 / 5)
        assertEpsilonEqual(self, test_vector.y, 4 / 5)
        
        test_vector = orig_vector.truncate(2)
        assertEpsilonEqual(self, test_vector.x, 6 / 5)
        assertEpsilonEqual(self, test_vector.y, 8 / 5)
        
        test_vector = orig_vector.truncate(5)
        assertEpsilonEqual(self, test_vector.x, 3)
        assertEpsilonEqual(self, test_vector.y, 4)
        
        test_vector = orig_vector.truncate(10)
        assertEpsilonEqual(self, test_vector.x, 3)
        assertEpsilonEqual(self, test_vector.y, 4)
        
    def test_equality(self):
        test_vector = ppb_vector.Vector2(3, 4)
        other_vector = ppb_vector.Vector2(3, 4)
        
        assertEpsilonEqual(self, test_vector == other_vector, True)
        assertEpsilonEqual(self, test_vector != other_vector, False)
        
        other_vector = ppb_vector.Vector2(6, 8)
        
        assertEpsilonEqual(self, test_vector == other_vector, False)
        assertEpsilonEqual(self, test_vector != other_vector, True)
        
    def test_dot(self):
        test_vector = ppb_vector.Vector2(3, 4)
        other_vector = ppb_vector.Vector2(5, 6)
        
        assertEpsilonEqual(self, test_vector * other_vector, 39)
        
        test_vector = ppb_vector.Vector2(1, -4)
        other_vector = ppb_vector.Vector2(21, 8)
        
        assertEpsilonEqual(self, test_vector * other_vector, -11)
        
        test_vector = ppb_vector.Vector2(0, 44)
        other_vector = ppb_vector.Vector2(182, 16)
        
        assertEpsilonEqual(self, test_vector * other_vector, 704)
        
    def test_scalar_mul(self):
        test_vector = ppb_vector.Vector2(3, 4)
        
        assertEpsilonEqual(self, (test_vector * 3).x, 9)
        assertEpsilonEqual(self, (test_vector * 3).y, 12)
        
        test_vector = ppb_vector.Vector2(-13, 42)
        
        assertEpsilonEqual(self, (test_vector * 5).x, -65)
        assertEpsilonEqual(self, (test_vector * 5).y, 210)
        
        test_vector = ppb_vector.Vector2(2, -4)
        
        assertEpsilonEqual(self, (test_vector * -2).x, -4)
        assertEpsilonEqual(self, (test_vector * -2).y, 8)
        
    def test_add(self):
        test_vector = ppb_vector.Vector2(3, 4)
        other_vector = ppb_vector.Vector2(5, 6)
        
        assertEpsilonEqual(self, (test_vector + other_vector).x, 8)
        assertEpsilonEqual(self, (test_vector + other_vector).y, 10)
        
        test_vector = ppb_vector.Vector2(1, -4)
        other_vector = ppb_vector.Vector2(21, 8)
        
        assertEpsilonEqual(self, (test_vector + other_vector).x, 22)
        assertEpsilonEqual(self, (test_vector + other_vector).y, 4)
        
        test_vector = ppb_vector.Vector2(0, 44)
        other_vector = ppb_vector.Vector2(182, 16)
        
        assertEpsilonEqual(self, (test_vector + other_vector).x, 182)
        assertEpsilonEqual(self, (test_vector + other_vector).y, 60)
        
    def test_sub(self):
        test_vector = ppb_vector.Vector2(3, 4)
        other_vector = ppb_vector.Vector2(5, 6)
        
        assertEpsilonEqual(self, (test_vector - other_vector).x, -2)
        assertEpsilonEqual(self, (test_vector - other_vector).y, -2)
        
        test_vector = ppb_vector.Vector2(1, -4)
        other_vector = ppb_vector.Vector2(21, 8)
        
        assertEpsilonEqual(self, (test_vector - other_vector).x, -20)
        assertEpsilonEqual(self, (test_vector - other_vector).y, -12)
        
        test_vector = ppb_vector.Vector2(0, 44)
        other_vector = ppb_vector.Vector2(182, 16)
        
        assertEpsilonEqual(self, (test_vector - other_vector).x, -182)
        assertEpsilonEqual(self, (test_vector - other_vector).y, 28)
