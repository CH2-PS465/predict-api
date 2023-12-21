# recomendation.py

def ayam_petelur(fase, banyak):
    if fase == "1":  # fase starter
        return {
            "recommendation": f"Ternak anda berada pada fase starter, komposisi pakan yang sebaiknya anda berikan:\n"
                               f"Jagung: {72.4 / 100 * 40 * banyak:.2f} gram\n"
                               f"Tepung ikan: {18.4 / 100 * 40 * banyak:.2f} gram\n"
                               f"Kedelai/ampas tahu: {9.2 / 100 * 40 * banyak:.2f} gram"
        }
    elif fase == "2":  # fase grower
        return {
            "recommendation": f"Ternak anda berada pada fase grower, komposisi pakan yang sebaiknya anda berikan:\n"
                               f"Jagung: {76.9 / 100 * 80 * banyak:.2f} gram\n"
                               f"Tepung ikan: {15.4 / 100 * 80 * banyak:.2f} gram\n"
                               f"Kedelai/ampas tahu: {7.7 / 100 * 80 * banyak:.2f} gram"
        }
    elif fase == "3":  # fase layers
        return {
            "recommendation": f"Ternak anda berada pada fase layers, komposisi pakan yang sebaiknya anda berikan:\n"
                               f"Jagung: {81.5 / 100 * 120 * banyak:.2f} gram\n"
                               f"Tepung ikan: {12.3 / 100 * 120 * banyak:.2f} gram\n"
                               f"Kedelai/ampas tahu: {6.2 / 100 * 120 * banyak:.2f} gram"
        }
    else:
        return {"error": "Masukkan anda harus berupa angka 1, 2, atau 3 pada kolom 'Fase Ternak'."}


def ayam_pedaging(fase, banyak):
    if fase == "1":  # fase starter
        return {
            "recommendation": f"Ternak anda berada pada fase starter, komposisi pakan yang sebaiknya anda berikan:\n"
                               f"Jagung: {53.6 / 100 * 50 * banyak:.2f} gram\n"
                               f"Bungkil kedelai: {35.64 / 100 * 50 * banyak:.2f} gram\n"
                               f"Tepung tulang: {5 / 100 * 50 * banyak:.2f} gram\n"
                               f"Bubuk lemak: {3.1 / 100 * 50 * banyak:.2f} gram\n"
                               f"Fosfor dan kalsium: {0.44 / 100 * 50 * banyak:.2f} gram\n"
                               f"Asam amino: {1.6 / 100 * 50 * banyak:.2f} gram\n"
                               f"Tepung Batu: {0.62 / 100 * 50 * banyak:.2f} gram"
        }
    elif fase == "2":  # fase finisher
        return {
            "recommendation": f"Ternak anda berada pada fase finisher, komposisi pakan yang sebaiknya anda berikan:\n"
                               f"Jagung: {62.5 / 100 * 120 * banyak:.2f} gram\n"
                               f"Bungkil kedelai: {29.2 / 100 * 120 * banyak:.2f} gram\n"
                               f"Tepung tulang: {5 / 100 * 120 * banyak:.2f} gram\n"
                               f"Bubuk lemak: {1.2 / 100 * 120 * banyak:.2f} gram\n"
                               f"Fosfor dan kalsium: {0.5 / 100 * 120 * banyak:.2f} gram\n"
                               f"Asam amino: {1.3 / 100 * 120 * banyak:.2f} gram\n"
                               f"Tepung Batu: {0.4 / 100 * 120 * banyak:.2f} gram"
        }
    else:
        return {"error": "Masukkan anda harus berupa angka 1, 2, atau 3 pada kolom 'Fase Ternak'."}
