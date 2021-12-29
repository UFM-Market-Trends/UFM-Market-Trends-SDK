def test():
    print("It works!!!")

def get_yearly_values(quarterly_values):
  '''
  Entrada:
    quarterly_values (list) Valores trimestrales.

  Salida:
    Return (list) Valores anuales (acum. 4 trimestres).
  '''

  yearly_values = [sum(quarterly_values[
                                        current-3 :
                                        # (list) type is upper-exclusive
                                        # slicing 
                                        current + 1 # (we need inclusive)
                                        ])
                   if current >= 3 else None
                   for current in range(len(quarterly_values))]

  return yearly_values


def get_yearly_variation(quarterly_values):
  '''
  Entrada:
    quarterly_values (list) Valores trimestrales

  Salida:
    Return (list) Variaciones interanuales.
  '''
  # Reutiliza la función anterior
  yearly_values = get_yearly_values(quarterly_values)

  yearly_variation = [None if (yearly_values[current] == None
                             or yearly_values[current-4] == None
                             or current-4 < 0)
                    else 
                    (yearly_values[current] - yearly_values[current-4]) 
                    / (yearly_values[current-4])
                    for current in range(len(yearly_values))]

  return yearly_variation

def application_test1():
    quarter_values_test = [0,1,2,3,4,5,6,7]
    assert get_yearly_values(quarter_values_test) == [None, None, None, 6, 10, 14, 18, 22], "should be true"
    assert get_yearly_variation(quarter_values_test) == [None, None, None, None, None, None, None, (22-6)/6], "should be true"
    
    print(get_yearly_values(quarter_values_test))
    print(get_yearly_variation(quarter_values_test))


def get_yearonyear_variation(values, inter_values_size):
  '''
  Entrada:
    values (list) Valores.

    lot_size (int) Cuantos anteriores valores anteriores a referir para
      calcular la variación.

  Salida:
    Return (list) Variaciones inter-<extensión de la inter_values_size>.
  '''
  variation = [None if (values[current] == None
                             or values[current-inter_values_size] == None
                             or current-inter_values_size < 0)
                    else 
                    (values[current] - values[current-inter_values_size]) 
                    / (values[current-inter_values_size])
                    for current in range(len(values))]

  return variation


def get_accumulated_values(values, lot_size):
  '''
  Entrada:
    values (list) Valores.

    lot_size (int) Cuantos anteriores valores a acumular.

  Salida:
    Return (list) Valores acumulados (acum. <lot_size> valores)
  '''
  accumulated_values = [sum(values[current- (lot_size-1):
                                         current], 
                          values[current])
                   if current >= lot_size-1 else None
                   for current in range(len(values))]

  return accumulated_values

def application_test2():
  values_test = [1] * 12
  
  assert get_accumulated_values(values_test, lot_size=3) == [None, None, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
  assert get_accumulated_values(values_test, lot_size=12) == [None, None, None, None, None, None, None, None, None, None, None, 12]
  print(get_accumulated_values(values_test, lot_size=3))
  print(get_accumulated_values(values_test, lot_size=12))
  
  
def get_accumulated_variation(values, lot_size):
  '''
  Entrada:
    values (list) Valores.

    lot_size (int) Cuantos anteriores valores a acumular y calcular la variación.

  Salida:
    Return (list) Variaciones inter-<extensión de la acumulación>.
  '''
  # Reutiliza la función anterior
  accumulated_values = get_accumulated_values(values, lot_size)
  
  accumulated_variation = [None if (accumulated_values[current] == None
                             or accumulated_values[current-lot_size] == None
                             or current-lot_size < 0)
                    else 
                    (accumulated_values[current] - accumulated_values[current-lot_size]) 
                    / (accumulated_values[current-lot_size])
                    for current in range(len(accumulated_values))]

  return accumulated_variation

def application_test3():
  values_test = [1] * 24
  
  assert get_accumulated_variation(values_test, lot_size=3) == [None, None, None, None, None, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  assert get_accumulated_variation(values_test, lot_size=12) == [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 0.0]
  print(get_accumulated_variation(values_test, lot_size=3))
  print(get_accumulated_variation(values_test, lot_size=12))
  
if __name__ == '__main__':
    application_test1()
    application_test2()
    application_test3()