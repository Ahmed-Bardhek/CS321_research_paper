prepare:
	python scripts/01_prepare_dataset.py

prompts:
	python scripts/02_generate_prompts.py

run:
	python scripts/03_run_models.py

evaluate:
	python scripts/04_evaluate_outputs.py

stats:
	python scripts/05_statistical_tests.py

figures:
	python scripts/06_generate_figures.py

all: prepare prompts run evaluate stats figures