SHELL := /bin/bash

parse-xlsx:
	source config.sh && python GetData/parse_xlsx.py
