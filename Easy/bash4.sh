#!/bin/bash

len () {
echo "Enter your string"
read STRING
expr length $STRING 
}

len