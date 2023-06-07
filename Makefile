up:
	@docker-compose up --build

clean:
	docker-compose down
	docker system prune -f
	docker volume prune -fa
	rm -fv api_server/db.sqlite3
	rm -rf web_client/node_modules