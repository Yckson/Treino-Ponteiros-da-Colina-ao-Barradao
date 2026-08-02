CXX := g++
CXXFLAGS := -std=c++17 -O2 -Wall -Wextra -Wshadow -Wconversion -pedantic

SRC_DIR := src
BUILD_DIR := build
TEMPLATE := templates/main.cpp

ifndef PROB
PROB_REQUIRED = @echo "Erro: informe o codigo do problema. Exemplo: make run PROB=CF_71A" && exit 1
else
PROB_REQUIRED =
endif

ifndef CONTEST
CONTEST_REQUIRED = @echo "Erro: informe o contest. Exemplo: make cf-contest CONTEST=2248" && exit 1
else
CONTEST_REQUIRED =
endif

PROB_DIR := $(SRC_DIR)/$(PROB)
SOURCE := $(PROB_DIR)/main.cpp
BINARY := $(BUILD_DIR)/$(PROB)
INPUT_DIR := $(PROB_DIR)/input
OUTPUT_DIR := $(PROB_DIR)/output

.PHONY: help new build run test exec list cf-tool cf-download cf-random cf-contest cf-contest-download cf-contest-problem cf-refresh-problems cf-refresh-problems-dry clean

help:
	@echo "Comandos disponiveis:"
	@echo "  make new PROB=CF_71A    cria src/CF_71A com template, input e output"
	@echo "  make build PROB=CF_71A  compila src/CF_71A/main.cpp"
	@echo "  make run PROB=CF_71A    compila e testa todos os casos"
	@echo "  make test PROB=CF_71A   testa todos os casos ja compilados"
	@echo "  make exec PROB=CF_71A   executa o binario lendo da entrada padrao"
	@echo "  make list               lista problemas em src/"
	@echo "  make cf-tool            abre menu para baixar problemas do Codeforces"
	@echo "  make cf-download PROB=CF_71A baixa statement/samples pelo codigo"
	@echo "  make cf-random          baixa problema aleatorio com filtros interativos"
	@echo "  make cf-contest CONTEST=2248 lista problemas de um contest"
	@echo "  make cf-contest-download CONTEST=2248 baixa todos os problemas do contest"
	@echo "  make cf-contest-problem CONTEST=2248 PROB=CF_2248A baixa um problema do contest"
	@echo "  make cf-refresh-problems atualiza metadata e reorganiza problemas baixados"
	@echo "  make cf-refresh-problems-dry mostra o que mudaria sem alterar arquivos"
	@echo "  make clean              remove build/"

new:
	$(PROB_REQUIRED)
	@mkdir -p "$(PROB_DIR)/input" "$(PROB_DIR)/output"
	@if [ ! -f "$(SOURCE)" ]; then cp "$(TEMPLATE)" "$(SOURCE)"; fi
	@echo "Criado/preparado: $(PROB_DIR)"

build:
	$(PROB_REQUIRED)
	@if [ ! -f "$(SOURCE)" ]; then echo "Erro: arquivo nao encontrado: $(SOURCE)"; exit 1; fi
	@mkdir -p "$(BUILD_DIR)"
	$(CXX) $(CXXFLAGS) "$(SOURCE)" -o "$(BINARY)"

run: build test

test:
	$(PROB_REQUIRED)
	@if [ ! -x "$(BINARY)" ]; then echo "Erro: binario nao encontrado. Rode: make build PROB=$(PROB)"; exit 1; fi
	@if [ ! -d "$(INPUT_DIR)" ]; then echo "Erro: pasta de entradas nao encontrada: $(INPUT_DIR)"; exit 1; fi
	@if [ -z "$$(find "$(INPUT_DIR)" -name '*.txt' -type f | sort)" ]; then echo "Nenhum caso .txt encontrado em $(INPUT_DIR)"; exit 0; fi
	@status=0; \
	for input in $$(find "$(INPUT_DIR)" -name '*.txt' -type f | sort); do \
		base=$$(basename "$$input" .txt); \
		expected="$(OUTPUT_DIR)/$$base.txt"; \
		got="$(BUILD_DIR)/$(PROB)_$$base.got"; \
		echo "==> $$base"; \
		"$(BINARY)" < "$$input" > "$$got"; \
		if [ -f "$$expected" ]; then \
			if diff -u --strip-trailing-cr "$$expected" "$$got"; then \
				echo "OK"; \
			else \
				echo "WA: saida diferente para $$base"; \
				status=1; \
			fi; \
		else \
			echo "Sem saida esperada: $$expected"; \
			echo "Saida obtida em: $$got"; \
		fi; \
	done; \
	exit $$status

exec: build
	"$(BINARY)"

list:
	@if [ ! -d "$(SRC_DIR)" ]; then echo "Nenhum problema cadastrado ainda."; exit 0; fi
	@find "$(SRC_DIR)" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort

cf-tool:
	python3 tools/cf_problem_tool.py

cf-download:
	$(PROB_REQUIRED)
	python3 tools/cf_problem_tool.py --code "$(PROB)"

cf-random:
	python3 tools/cf_problem_tool.py --random

cf-contest:
	$(CONTEST_REQUIRED)
	python3 tools/cf_problem_tool.py --contest "$(CONTEST)"

cf-contest-download:
	$(CONTEST_REQUIRED)
	python3 tools/cf_problem_tool.py --contest "$(CONTEST)" --download-all

cf-contest-problem:
	$(CONTEST_REQUIRED)
	$(PROB_REQUIRED)
	python3 tools/cf_problem_tool.py --contest "$(CONTEST)" --contest-problem "$(PROB)"

cf-refresh-problems:
	python3 tools/cf_problem_tool.py --refresh --refresh-problems

cf-refresh-problems-dry:
	python3 tools/cf_problem_tool.py --refresh --refresh-problems --dry-run

clean:
	@rm -rf "$(BUILD_DIR)"
	@echo "Removido: $(BUILD_DIR)"
