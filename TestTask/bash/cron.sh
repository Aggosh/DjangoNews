#!/bin/bash

crontab ./bash/cron-setting
cron -f &
