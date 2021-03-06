help:
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run-core"
	@echo "        Spin up the core server on the command line"
	@echo "    run-actions"
	@echo "        Spin up the action server"
	@echo "    run"
	@echo "        Spin up both core and the action server"
	@echo "    visualize"
	@echo "        Show your stories as a graph"


train-core:
	python -m rasa_core.train -s data/storiesfou.md -d domainfou.yml -o models/dialoguefou --debug

run-core:
	python -m rasa_core.run --enable_api --core models/dialoguefou --nlu models/nlu/currentfou --debug --endpoints endpoints.yml

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions.actions

run:
	make run-actions&
	make run-core

train-interactive:
	python -m rasa_core.train interactive -s data/storiesfou.md -d domainfou.yml -o models/dialoguefou --debug --endpoints endpoints.yml

visualize:
	python -m rasa_core.visualize -s data/stories.md -d domain.yml -o story_graph.html

train-nlu:
	python -m rasa_nlu.train -c nlu_tensorflow.yml --fixed_model_name currentfou --data data/nlufou.md -o models --project nlu --verbose
