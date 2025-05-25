from typing import Dict, List, Iterator

class Film:
    def __init__(self, title: str, genre: str, year: int, company: str) -> None:

        self.title: str = title
        self.genre: str = genre
        self.year: int = year
        self.company: str = company

    def __repr__(self) -> str:
        return f"Film(title={self.title}, genre={self.genre}, year={self.year}, company={self.company})"


class FilmCollection:
    def __init__(self) -> None:

        self.films: Dict[str, Film] = {}

    def AddFilm(self, film: Film) -> None:
        if film.title in self.films:
            existing = self.films[film.title]
            if existing.year == film.year and existing.company == film.company:
                print("This exact film already exists in the collection")
                return
            else:
                new_key = f"{film.title} ({film.year}, {film.company})"
                self.films[new_key] = film
                print("Added film with same title but different year/company")
                return
        else:
            self.films[film.title] = film


    def removeFilm(self, title: str, year: int, company: str) -> None:
        key_to_remove = None
        for key, film in self.films.items():
            if film.title == title and film.year == year and film.company == company:
                key_to_remove = key
                break
        if key_to_remove:
            del self.films[key_to_remove]
        else:
            print("Film not found in the collection.")


    def findFilmByDate(self, year: int) -> None:

        sortbyYear: List[Film] = [
            film for film in self.films.values() if film.year == year
        ]
        if sortbyYear:
            print("Films in that year:")
            for film in sortbyYear:
                print(film)

    def findFilmByGenre(self, genre: str) -> None:

        sortbyGenre: List[Film] = [
            film for film in self.films.values() if film.genre == genre
        ]
        if sortbyGenre:
            print("Films in that genre:")
            for film in sortbyGenre:
                print(film)

    def findFilmByCompany(self, company: str) -> None:

        sortbyCompany: List[Film] = [
            film for film in self.films.values() if film.company == company
        ]
        if sortbyCompany:
            print("Films from that company:")
            for film in sortbyCompany:
                print(film)

    def __iter__(self) -> Iterator[Film]:

        return FilmIterator(self.films)


class FilmIterator:
    def __init__(self, films: Dict[str, Film]) -> None:

        self.films: List[Film] = list(films.values())
        self.index: int = 0

    def __iter__(self) -> Iterator[Film]:
        return self

    def __next__(self) -> Film:
        if self.index < len(self.films):
            film = self.films[self.index]
            self.index += 1
            return film
        else:
            raise StopIteration


    


def main():
   collection = FilmCollection()
    
   while True:
    print("\n===== Film Collection Management Menu =====")
    print("1. Add a film")
    print("2. Remove a film")
    print("3. Find films by year")
    print("4. Find films by genre")
    print("5. Find films by production company")
    print("6. Show all films")
    print("7. Exit the program")
    
    choice = input("Select an option (1-7): ")
    
    if choice == '1':
        title = input("Enter film title: ")
        genre = input("Enter genre: ")
        try:
            year = int(input("Enter release year: "))
        except ValueError:
            print("Error: Year must be a number.")
            continue
        company = input("Enter production company: ")
        film = Film(title, genre, year, company)
        collection.AddFilm(film)
    
    elif choice == '2':
        title = input("Enter film title to remove: ")
        year = input("Enter film year to remove: ")
        company = input("Enter film company to remove: ")
        collection.removeFilm(title,int(year),company)
        
    
    elif choice == '3':
        try:
            year = int(input("Enter release year: "))
            collection.findFilmByDate(year)
        except ValueError:
            print("Error: Year must be a number.")
    
    elif choice == '4':
        genre = input("Enter genre: ")
        collection.findFilmByGenre(genre)
    
    elif choice == '5':
        company = input("Enter production company: ")
        collection.findFilmByCompany(company)
    
    elif choice == '6':
        print("All films in the collection:")
        for film in collection:
            print(film)
    
    elif choice == '7':
        print("Exiting the program")
        break
    
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    
