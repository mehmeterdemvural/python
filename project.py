def flatten(lst):
  """
  Verilen listeyi düzleştirir.

  Args:
    lst: Düzleştirilecek liste.

  Returns:
    Düzleştirilmiş liste.
  """

  result = []
  for item in lst:
    if isinstance(item, list):
      result.extend(flatten(item))
    else:
      result.append(item)
  return result

# Örnek kullanım
input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output_list = flatten(input_list)
print(output_list)  # Çıktı: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]


def reverse_list(lst):
  """
  Verilen listenin ve alt listelerinin elemanlarını tersine çevirir.

  Args:
    lst: Tersine çevrilecek liste.

  Returns:
    Ters çevrilmiş liste.
  """

  result = []
  for item in reversed(lst):
    if isinstance(item, list):
      result.append(reverse_list(item))
    else:
      result.append(item)
  return result

# Örnek kullanım
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_list(input_list)
print(output_list)  # Çıktı: [[7, 6, 5], [4, 3], [2, 1]]
