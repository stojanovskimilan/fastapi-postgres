run-db:
	docker run --name fastapi-postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgrespw -e POSTGRES_DB=fastapi-db -d postgres