# Day 13 Unit Testing dalam python

# apa itu unit testing?
# unit testing adalah metode pengujian yang digunakan untuk menguji bagian kecil(unit) dari kode,
# seperti fingsi atau metode, untuk memastikan mereka bekerja dengan benar.

# mengunakan modul unit testing
import unittest

# contoh fungsi yang akan diuji
def tambah(a, b):
    return a + b

def bagi(a, b):
    if b == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan")
    return a / b

# Membuat test case
class TestMathOperations(unittest.TestCase):
    def test_tambah(self):
        self.assertEqual(tambah(2, 3),5)
        self.assertEqual(tambah(-1, 1), 0)
        self.assertEqual(tambah(0, 0), 0)

    def test_bagi(self): 
        self.assertEqual(bagi(10, 2), 5)
        self.assertEqual(bagi(9, 3), 3)

        with self.assertRaises(ValueError):
            bagi(10, 0)  # harus mengembalikan error

# Menjalankan unit test
if __name__ == "__main__":
    unittest.main()