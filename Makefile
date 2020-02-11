.PHONY: clean

clean:
	@find . \( -name "__pycache__" -o -name "*.pyc" -o -name "dist" -o -name "build" -o -name "*.egg-info" \) -exec rm -rf {} +
