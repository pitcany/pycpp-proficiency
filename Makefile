# pycpp-proficiency Makefile
# Development workflow targets

.PHONY: all bootstrap check fmt lint test test-python test-cpp build-cpp run-cpp-demo \
        sync-notion gen-from-manifest run-lesson clean help

# Default target
all: check

# =============================================================================
# Setup
# =============================================================================

## Bootstrap the development environment (macOS)
bootstrap:
	@bash scripts/bootstrap_macos.sh

## Verify environment is set up correctly
check:
	@bash scripts/check.sh

# =============================================================================
# Code Quality
# =============================================================================

## Format Python code with black and ruff
fmt:
	@echo "Formatting Python code..."
	@ruff check --fix src/ tests/python/ scripts/ || true
	@black src/ tests/python/ scripts/
	@echo "Done."

## Run linters (ruff, mypy)
lint:
	@echo "Running linters..."
	@ruff check src/ tests/python/ scripts/
	@mypy src/python_lib/
	@echo "Done."

# =============================================================================
# Testing
# =============================================================================

## Run all tests (Python and C++)
test: test-python test-cpp

## Run Python tests
test-python:
	@echo "Running Python tests..."
	@pytest tests/python/ -v --tb=short

## Run Python tests with coverage
test-python-cov:
	@echo "Running Python tests with coverage..."
	@pytest tests/python/ -v --cov=python_lib --cov-report=term-missing

## Run C++ tests
test-cpp:
	@echo "Running C++ tests..."
	@if [ -d build ] && [ -f build/tests/cpp/test_numerical ]; then \
		cd build && ctest --output-on-failure; \
	else \
		echo "C++ tests not built. Run 'make build-cpp' first."; \
	fi

# =============================================================================
# C++ Build
# =============================================================================

## Build C++ components
build-cpp:
	@echo "Building C++ components..."
	@mkdir -p build
	@cd build && cmake .. -DCMAKE_BUILD_TYPE=Release && cmake --build . --parallel
	@echo "Done."

## Build C++ in Debug mode with sanitizers
build-cpp-debug:
	@echo "Building C++ in Debug mode..."
	@mkdir -p build-debug
	@cd build-debug && cmake .. -DCMAKE_BUILD_TYPE=Debug && cmake --build . --parallel
	@echo "Done."

## Run C++ demo
run-cpp-demo: build-cpp
	@echo "Running C++ demo..."
	@./build/demo

# =============================================================================
# Content Management
# =============================================================================

## Sync content from Notion (requires NOTION_API_KEY)
sync-notion:
	@python scripts/sync_from_notion.py

## Regenerate lesson structure from manifest
gen-from-manifest:
	@python scripts/generate_from_manifest.py

## Force regenerate (overwrite existing files)
gen-from-manifest-force:
	@python scripts/generate_from_manifest.py --force

# =============================================================================
# Run Lessons
# =============================================================================

## Run a specific lesson (usage: make run-lesson WEEK=week1 LESSON=day-01)
run-lesson:
ifndef WEEK
	$(error WEEK is not set. Usage: make run-lesson WEEK=week1 LESSON=day-01)
endif
ifndef LESSON
	$(error LESSON is not set. Usage: make run-lesson WEEK=week1 LESSON=day-01)
endif
	@echo "Running lesson: $(WEEK)/$(LESSON)"
	@if [ -f "lessons/$(WEEK)/$(LESSON)/python/main.py" ]; then \
		python "lessons/$(WEEK)/$(LESSON)/python/main.py"; \
	else \
		echo "No main.py found for this lesson."; \
	fi

# =============================================================================
# Cleanup
# =============================================================================

## Clean build artifacts
clean:
	@echo "Cleaning..."
	@rm -rf build/ build-debug/
	@rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "Done."

## Deep clean (including venv)
clean-all: clean
	@rm -rf .venv/
	@echo "Virtual environment removed."

# =============================================================================
# Help
# =============================================================================

## Show this help message
help:
	@echo "pycpp-proficiency Makefile"
	@echo ""
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@grep -E '^## ' $(MAKEFILE_LIST) | sed 's/## /  /' | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'
