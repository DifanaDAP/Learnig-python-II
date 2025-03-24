# Latihan
# 1. Buat fungsi baru bernama "kurang" dan "kali", lalu buat unit test untuk fungsi tersebut.
import unittest

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

# 2. Tambahkan lebih banyak test case untuk memastikan fungsi berjalan dengan baik.
class Test(unittest.TestCase):
    def test_kurang(self):
        self.assertEqual(kurang(5, 3), 2)
        self.assertEqual(kurang(10, 3), 7)
        self.assertEqual(kurang(8, 5), 3)

    def test_kali(self):
        self.assertEqual(kali(2, 3), 6)
        self.assertEqual(kali(10, 5), 50)

# 3. Jalankan unit test dan perbaiki jika ada kesalahan atau bug.
if __name__ == "__main__":
    unittest.main()