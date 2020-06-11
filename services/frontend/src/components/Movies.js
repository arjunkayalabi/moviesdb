import React from "react";
import { List, Header, Rating } from "semantic-ui-react";

const Movies = ({ movies }) => {
	return (
		<div>
			<List>
				{movies.map((movie) => {
					return (
						<List.Item key={movie.title}>
							<Header>{movie.title}</Header>
							<Rating
								icon="heart"
								rating={movie.rating}
								maxRating={5}
								disabled
							/>
						</List.Item>
					);
				})}
			</List>
		</div>
	);
};

export default Movies;
