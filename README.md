# My Top Ten Movies

This is a Flask-based web application that allows users to manage a collection of movies. Users can add movies, edit their ratings and reviews, and delete movies from the collection. The application integrates with The Movie Database (TMDb) API to retrieve movie details like title, release year, and poster images.

## Features

- **User Authentication**: Secure login and admin roles.
- **Responsive Design**: Built with Bootstrap for a seamless experience on any device.
- **Movie Management**: Add, edit, and delete movies in your collection.
- **Integration with TMDb API**: Automatically fetch movie details from The Movie Database.
- **Rating and Reviews**: Rate and review each movie.
- **Password Security**: Implemented password hashing for enhanced security.


## Usage

- **Home Page**: Displays a list of all movies in the collection, ranked by rating.
- **Add Movie**: Allows users to search for movies by title using the TMDb API.
- **Edit Movie**: Users can update the rating and review of a movie.
- **Delete Movie**: Users can remove a movie from the collection.

## Dependencies

- **Flask**: Micro web framework used to create the application.
- **Flask-Bootstrap**: For responsive design.
- **Flask-WTF**: For handling forms securely.
- **SQLAlchemy**: ORM used to manage the SQLite database.
- **WTForms**: For creating forms easily.
- **Requests**: For making API calls to TMDb.

## API

The application uses The Movie Database (TMDb) API to fetch movie details. You will need to set up an API key and include it in the configuration.


## Contributing

Feel free to fork this repository, create a new branch, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.
