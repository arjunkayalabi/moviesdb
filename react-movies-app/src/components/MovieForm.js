import React, { useState } from "react";
import { Form, Input, Rating, Button } from "semantic-ui-react";

// "http:localhost:5000/add_movie",

export const MovieForm = ({ onNewMovie }) => {
	const [title, setTitle] = useState("");
	const [rating, setRating] = useState(1);

	return (
		<div>
			<Form>
				<Form.Field>
					<Input
						placeholder="movie title"
						value={title}
						onChange={(e) => setTitle(e.target.value)}
					></Input>
				</Form.Field>
				<Form.Field>
					<Rating
						icon="heart"
						rating={rating}
						maxRating={5}
						onRate={(_, data) => setRating(data.rating)}
					/>

					<Button
						onClick={async () => {
							const movie = { title, rating };
							const response = await fetch(
								`${process.env.REACT_APP_USERS_SERVICE_URL}/add_movie`,
								{
									method: "POST",
									headers: {
										"Content-Type": "application/json",
									},
									body: JSON.stringify(movie),
								}
							);

							if (response.ok) {
								console.log("response worked");
								onNewMovie(movie);
								setTitle("");
								setRating(1);
							}
						}}
					>
						Add Movie
					</Button>
				</Form.Field>
			</Form>
		</div>
	);
};
