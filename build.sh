#!/bin/sh

protoc --proto_path=./ --proto_path=${GOPATH}/src --go_out=plugins=grpc:. proto/*.proto

# run in python env
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/audio_streaming.proto
