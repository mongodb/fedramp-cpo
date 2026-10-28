VENV := .venv
PY := $(VENV)/bin/python

.PHONY: build check clean

# Regenerate cpo/cpo.json from cpo/cpo.md (validates first)
build: $(VENV)/.installed
	$(PY) scripts/build_cpo.py

# Validate only; write nothing
check: $(VENV)/.installed
	$(PY) scripts/build_cpo.py --check

$(VENV)/.installed: scripts/requirements.txt
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -q -r scripts/requirements.txt
	touch $@

clean:
	rm -rf $(VENV)
