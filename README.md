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

