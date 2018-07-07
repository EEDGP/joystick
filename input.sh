#!/bin/bash
spawn ./vibration.sh
expect "Enter effect number, -1 to exit"
send "0"
