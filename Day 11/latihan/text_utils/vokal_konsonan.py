#latihan 2
def hitung_vokal_konsonan(teks):
    vokal= "aiueoAIUEO"
    jumlah_vokal = sum(1 for huruf in teks if huruf in vokal)
    jumlah_konsonan = len([huruf for huruf in teks if huruf.isalpha() and huruf not in vokal])
    return jumlah_vokal, jumlah_konsonan
