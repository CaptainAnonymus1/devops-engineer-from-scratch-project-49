install: # установка пакета
	uv sync

brain-games: # shortcut для старта игры
	uv run brain-games

build: # сборка проекта
	uv build

package-install: # установка пакета в ос
	uv tool install dist/*.whl
