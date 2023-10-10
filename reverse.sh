#!/bin/bash

## Make sure to replace "x" in host IP.

for ip in $(seq  72 91);do
	host x.x.x.$ip |grep "website" |cut -d" " -f1,5
done
