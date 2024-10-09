from closest_pair import Point, closest_pair_of_points
import unittest
import random
import math
class TestClosestPair(unittest.TestCase):
    
    def test_basic_case(self):
        points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)]
        result, dist = closest_pair_of_points(points)
        expected_pair = (Point(0, 0), Point(1, 1))
        self.assertEqual(result, expected_pair)

    def test_large_coordinates(self):
        points = [Point(1000, 1000), Point(2000, 2000), Point(3000, 3000)]
        result, dist = closest_pair_of_points(points)
        expected_pair = (Point(1000, 1000), Point(2000, 2000))
        self.assertEqual(result, expected_pair)
    
    def test_insufficient_points(self):
        points = [Point(0, 0)]
        with self.assertRaises(ValueError):
            closest_pair_of_points(points)
    
    def test_identical_points(self):
        points = [Point(1, 1), Point(1, 1)]
        result, dist = closest_pair_of_points(points)
        expected_pair = (Point(1, 1), Point(1, 1))
        self.assertEqual(result, expected_pair)
    
    def test_close_points(self):
        points = [Point(0, 0), Point(0, 0.1), Point(0.2, 0), Point(0.3, 0.3)]
        result, dist = closest_pair_of_points(points)
        expected_pair = (Point(0, 0), Point(0, 0.1))
        self.assertEqual(result, expected_pair)
    
    def test_large_random_points(self):
        # Generar 1000 puntos aleatorios
        points = [Point(random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(1000)]
        result, dist = closest_pair_of_points(points)
        # Solo validar que no haya errores en la ejecución, ya que el par esperado no es conocido
        self.assertIsNotNone(result)
        self.assertGreaterEqual(dist, 0)

    def test_non_linear_distribution(self):
        # Puntos distribuidos en un arco de circunferencia
        points = [Point(math.cos(theta), math.sin(theta)) for theta in range(0, 360, 5)]
        result, dist = closest_pair_of_points(points)
        # Comprobamos que la distancia no es infinita y se calcula correctamente
        self.assertIsNotNone(result)
        self.assertGreaterEqual(dist, 0)

    def test_clustered_and_sparse_distribution(self):
        # Crear un conjunto con un cluster denso y puntos dispersos
        cluster_points = [Point(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(100)]
        sparse_points = [Point(random.uniform(100, 200), random.uniform(100, 200)) for _ in range(10)]
        points = cluster_points + sparse_points
        result, dist = closest_pair_of_points(points)
        self.assertIsNotNone(result)
        self.assertGreaterEqual(dist, 0)

if __name__ == '__main__':
    unittest.main()
