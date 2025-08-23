usera={'Inception','Matrix','Avatar','Titanic'} 
userb={'Inception','Matrix','Jurassic Park','Avengers'}
commonmovies=usera & userb
print("Movies both have watched:",commonmovies)
uniquemoviesofa=usera-userb
print("Movies user A have watched:",uniquemoviesofa)
suggestfora=userb-usera
print("Suggested movies for user A by user B:",suggestfora)
