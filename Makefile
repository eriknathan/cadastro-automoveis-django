APP = trabalho-ia-vinhos

run:
	@python3 /home/eriknathan/Estudos/faculdade/trabalho-ia-vinhos/app/scripts/create_model.py
	@echo -------------------
	@echo  RODANDO O PROJETO
	@echo -------------------
	@python3 manage.py runserver 8081