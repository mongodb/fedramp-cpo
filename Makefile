VENV := .venv
PY := $(VENV)/bin/python

.PHONY: build check check-schema clean

# Regenerate cpo/cpo.json from cpo/cpo.md (validates first)
build: $(VENV)/.installed
	$(PY) scripts/build_cpo.py

# Validate cpo.md and the template; write nothing
check: $(VENV)/.installed
	$(PY) scripts/build_cpo.py --check
	$(PY) scripts/build_cpo.py --src cpo/template.md --check

# Compare vendored schemas to what fedramp.gov publishes
check-schema:
	python3 scripts/check_schema.py

$(VENV)/.installed: scripts/requirements.txt
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -q -r scripts/requirements.txt
	touch $@

clean:
	rm -rf $(VENV)
