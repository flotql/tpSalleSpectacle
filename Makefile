run:
	docker-compose up -d --build
	echo "Waiting MariaDB to be up"
	sleep 10
	docker exec tpsallespectacle_web_1 python SalleSpectacle/manage.py migrate
	docker exec tpsallespectacle_web_1  bash -c "python SalleSpectacle/manage.py shell < script.py"
	docker exec tpsallespectacle_web_1  python SalleSpectacle/manage.py loaddata db.json
	docker exec -d tpsallespectacle_web_1  python SalleSpectacle/manage.py runserver 0.0.0.0:8000
