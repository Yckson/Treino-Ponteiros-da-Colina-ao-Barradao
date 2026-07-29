CXX := g++
CXXFLAGS := -std=c++17 -O3 -Wall -Wextra -Wshadow -Wconversion -pedantic

SRC_DIR := src
BUILD_DIR := build
TEMPLATE := templates/main.cpp

ifndef PROB
PROB_REQUIRED = @echo "Erro: informe o codigo do problema. Exemplo: make run PROB=CF_71A" && exit 1
else
PROB_REQUIRED =
endif

PROB_DIR := $(SRC_DIR)/$(PROB)
SOURCE := $(PROB_DIR)/main.cpp
BINARY := $(BUILD_DIR)/$(PROB)
INPUT_DIR := $(PROB_DIR)/input
OUTPUT_DIR := $(PROB_DIR)/output

.PHONY: help new build run test exec list clean

help:
	@echo "Comandos disponiveis:"
	@echo "  make new PROB=CF_71A    cria src/CF_71A com template, input e output"
	@echo "  make build PROB=CF_71A  compila src/CF_71A/main.cpp"
	@echo "  make run PROB=CF_71A    compila e testa todos os casos"
	@echo "  make test PROB=CF_71A   testa todos os casos ja compilados"
	@echo "  make exec PROB=CF_71A   executa o binario lendo da entrada padrao"
	@echo "  make list               lista problemas em src/"
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
	@if [ -z "$$(find "$(INPUT_DIR)" -name '*.in' -type f | sort)" ]; then echo "Nenhum caso .in encontrado em $(INPUT_DIR)"; exit 0; fi
	@status=0; \
	for input in $$(find "$(INPUT_DIR)" -name '*.in' -type f | sort); do \
		base=$$(basename "$$input" .in); \
		expected="$(OUTPUT_DIR)/$$base.out"; \
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

clean:
	@rm -rf "$(BUILD_DIR)"
	@echo "Removido: $(BUILD_DIR)"
