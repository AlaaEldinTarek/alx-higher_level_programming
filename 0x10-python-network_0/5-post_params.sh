#!/bin/bash
# Bash scripts that sends a POST request to a given URL.
curl -s -X POST -d "X-School-User-Id: 98" "$1"
