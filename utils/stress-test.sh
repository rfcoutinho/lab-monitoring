#!/usr/bin/env bash

set -ex

threads=4
requests=20000

function send_request() {
    for ((i = 0; i <= $requests; i++)); do
        curl -k http://localhost:5000/500 &> /dev/null
    done
}

for ((i = 0; i <= $threads; i++)); do
    send_request&
done