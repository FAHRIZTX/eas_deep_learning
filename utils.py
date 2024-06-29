def switch(quest):
    if quest == '1':
      return 1, 'Sangat Tidak Setuju'
    elif quest == '2':
        return 2, 'Tidak Setuju'
    elif quest == '3':
        return 3, 'Agak Setuju'
    elif quest == '4':
        return 4, 'Netral'
    elif quest == '5':
        return 5, 'Agak Setuju' 
    elif quest == '6':
        return 6, 'Setuju'  
    elif quest == '7':
        return 7, 'Sangat Setuju'                 
    else:
        return 0, 'Tidak Dipilih'