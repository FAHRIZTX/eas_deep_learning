def to_jenis(q):
    if q == '1':
      return 'Laki - Laki'
    else:
        return 'Perempuan'

def to_tingkat(q):
    if q == '1':
      return 'Normal'
    elif q == '2':
        return 'Di atas normal'
    else:
        return 'Jauh di atas normal'

def to_yatidak(q):
    if q == '1':
      return 'Ya'
    elif q == '0':
        return 'Tidak'
