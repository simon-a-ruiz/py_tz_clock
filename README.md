# py_tz_clock

## Time Zone Configuration
1. Open config.yml in your favorite editor
2. Add the new time zone based on the example structures
3. You can find time zones on systemd type systems with `timedatectl list-timezones`

## Usage
### Linux
#### Dirty
`python3 clock.py`

#### Clean
1. Modify the `tz_clock.desktop` file to update the paths to the application
2. Copy the `.desktop` file to `${HOME}/.local/share/applications`
3. Launch from you launcher

Report
======
53 statements analysed.

Statistics by type
------------------

|type     |number |old number |difference |%documented |%badname |
|---------|-------|-----------|-----------|------------|---------|
|module   |1      |1          |=          |100.00      |0.00     |
|---------|-------|-----------|-----------|------------|---------|
|class    |0      |0          |=          |0           |0        |
|---------|-------|-----------|-----------|------------|---------|
|method   |0      |0          |=          |0           |0        |
|---------|-------|-----------|-----------|------------|---------|
|function |2      |2          |=          |100.00      |0.00     |



External dependencies
---------------------
::

    pytz (clock)
    yaml (clock)



Raw metrics
-----------

|type      |number |%     |previous |difference |
|----------|-------|------|---------|-----------|
|code      |78     |74.29 |76       |+2.00      |
|----------|-------|------|---------|-----------|
|docstring |3      |2.86  |3        |=          |
|----------|-------|------|---------|-----------|
|comment   |1      |0.95  |1        |=          |
|----------|-------|------|---------|-----------|
|empty     |23     |21.90 |23       |=          |



Duplication
-----------

|                         |now   |previous |difference |
|-------------------------|------|---------|-----------|
|nb duplicated lines      |0     |0        |=          |
|-------------------------|------|---------|-----------|
|percent duplicated lines |0.000 |0.000    |=          |



Messages by category
--------------------

|type       |number |previous |difference |
|-----------|-------|---------|-----------|
|convention |0      |2        |-2.00      |
|-----------|-------|---------|-----------|
|refactor   |0      |0        |=          |
|-----------|-------|---------|-----------|
|warning    |0      |0        |=          |
|-----------|-------|---------|-----------|
|error      |0      |0        |=          |



Global evaluation
-----------------
Your code has been rated at 10.00/10 (previous run: 9.62/10, +0.38)

