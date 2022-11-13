SHELL := /bin/bash

parse-xlsx:
	source config.sh && python parse-xlsx.py
