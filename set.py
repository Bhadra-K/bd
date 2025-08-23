# Set Project – Movie Recommendation System
# Problem:
# Create a simple movie recommendation system using sets.
# User A’s watched movies (set1)
# User B’s watched movies (set2)
# Program should show:
# Movies both have watched (intersection)
# Movies unique to User A (difference)
# Suggested movies for User A based on User B’s watched list (set2 – set1)

usera={'Inception','Matrix','Avatar','Titanic'} 
userb={'Inception','Matrix','Jurassic Park','Avengers'}
commonmovies=usera & userb
print("Movies both have watched:",commonmovies)
uniquemoviesofa=usera-userb
print("Movies user A have watched:",uniquemoviesofa)
suggestfora=userb-usera
print("Suggested movies for user A by user B:",suggestfora)
