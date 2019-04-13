def dto(dec):
  dec=int(dec)
  output=''
  const=28672
  for i,j in zip(range(5),reversed(range(5))):
      k=((const>>i*3)&dec)>>3*j
      output+=str(k)
  return output

print(dto(156))
