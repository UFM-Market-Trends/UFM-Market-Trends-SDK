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

def application():
    quarter_values_test = [0,1,2,3,4,5,6,7]
    assert get_yearly_values(quarter_values_test) == [None, None, None, 6, 10, 14, 18, 22], "should be true"
    assert get_yearly_variation(quarter_values_test) == [None, None, None, None, None, None, None, (22-6)/6], "should be true"
    
    print(get_yearly_values(quarter_values_test))
    print(get_yearly_variation(quarter_values_test))


if __name__ == '__main__':
    application()