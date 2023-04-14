for i in range(0,3,2):
  for k in range(1,10):
    for j in range(i*2+2,i*2+6):
      print(f'{j} x {k} = {j*k:2d}',end='\t')
    print()
  print()

