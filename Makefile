SHELL := /bin/bash

parse-xlsx:
	source config.sh && python parse_xlsx.py
