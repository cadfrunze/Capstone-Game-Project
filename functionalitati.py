import pandas as pd
import random

data = pd.read_csv('./data/Frequency list-en-ro.csv')
data_coloana_en = data.en
data_coloana = data_coloana_en.to_list()


def afisare_raspuns():
    """Alegerea random unei valori din data"""
    aleg_elem: str = random.choice(data_coloana)
    #data_coloana.remove(aleg_elem)
    raspuns = data[data.en == aleg_elem]
    en_word = ''.join(raspuns.en)
    ro_word = ''.join(raspuns.ro)
    return [en_word, ro_word]


def random_ro(word_en: str, word_ro: str):
    random_raspuns = random.choice([True, False])
    data1_en = data.en
    data1_en = data1_en.to_list()
    data_word_en = random.choice(data1_en)
    if random_raspuns:
        return [word_en, word_ro]
    else:
        while True:
            if word_en == data_word_en:
                data_word_en = random.choice(data1_en)
                continue
            else:
                raspuns = data[data.en == data_word_en]
                word_ro = "".join(raspuns.ro)
                break
    data_coloana.remove(data_word_en)
    return [word_en, word_ro]





