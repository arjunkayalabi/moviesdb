import React, { useState, useEffect } from "react";
import "./App.css";
import Movies from "./components/Movies";
import { MovieForm } from "./components/MovieForm";
import { Container } from "semantic-ui-react";
import { hot } from "react-hot-loader/root";

// "http://localhost:5000/movies"

function App() {
	const [movies, setMovies] = useState([]);

	useEffect(() => {
		fetch(`${process.env.REACT_APP_USERS_SERVICE_URL}/movies`).then(
			(response) =>
				response.json().then((data) => {
					setMovies(data.movies);
				})
		);
	}, []);

	// console.log(movies); `${process.env.REACT_APP_USERS_SERVICE_URL}/users`

	return (
		<div className="App">
			<Container style={{ marginTop: 45 }}>
				<MovieForm
					onNewMovie={(movie) =>
						setMovies((currentMovie) => [movie, ...currentMovie])
					}
				/>

				<Movies movies={movies} />
			</Container>
		</div>
	);
}

export default hot(App);
