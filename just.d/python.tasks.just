# Builds the python project.
build:
	python -m build --wheel

# Runs the python project.
run:
	hatch run "`tomlq -r .project.name pyproject.toml`"

# Cleans up the project.
clean:
	rm -rf dist/
	fd --no-ignore --type directory --hidden __pycache__ --exec rm -r {}
